---
author: "Jan Drögehoff"
title: "The state of multi-GPU support in Linux distros"
date: "2024-02-16"
description: "and its problems"
tags: ["GPU", "GNOME", "KDE"]
---


For a long time Multi-GPU support on Linux has been rather poor.  
These days things things tend to be a lot better, common Desktop Environments such as GNOME, KDE, Cinnamon and many more allow the end-user to launch games on more powerful hardware, if available, or let applications request it ahead of time by setting the `PrefersNonDefaultGPU` key in their desktop file to `true`.

The [Desktop entry spec](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) describes the key as followed:
> PrefersNonDefaultGPU	If true, the application prefers to be run on a more powerful discrete GPU if available, which we describe as “a GPU other than the default one” in this spec to avoid the need to define what a discrete GPU is and in which cases it might be considered more powerful than the default GPU. This key is only a hint and support might not be present depending on the implementation. 

Seems reasonable, but this will be important later.

Some  developers such as the KDE team have created their own solution for this, but most rely on switcheroo-control, which exposes a list of GPUs over DBUS with relevant information such as:
- Device Name
- If the GPU is considered the default
	+ this is established by the kernel at boot time and can be switched using the kernel switcheroo interface
- a list of Environment Variables needed to run on this GPU
	+ for the proprietary Nvidia drivers there is a hardcoded set of environment variables and support for more than 2 Nvidia GPUs is not possible
	
This information is then iterated upon to find the GPU to use and all was good in the world.

---

But its rarely ever so easy and there have been [many](https://github.com/linuxmint/cinnamon/issues/10699) [*many*](https://github.com/ValveSoftware/steam-for-linux/issues/8069) [*__many__*](https://github.com/flathub/com.valvesoftware.Steam/issues/784) and [many](https://gitlab.gnome.org/GNOME/gnome-shell/-/issues/4796) [more](https://github.com/flathub/com.valvesoftware.Steam/issues/784) bugs reported against it not working as intended.  

So what went wrong?  
Lets look at the spec again

> PrefersNonDefaultGPU	If true, the application prefers to be run on a more powerful discrete GPU if available, which we describe as “a GPU other than the default one” in this spec to avoid the need to define what a discrete GPU is and in which cases it might be considered more powerful than the default GPU. This key is only a hint and support might not be present depending on the implementation. 

when support for Discrete GPUs was implemented the spec was taken a bit too seriously.

It appears this part was taken at face value
> the application prefers to be run on a more powerful discrete GPU [...] which we describe as “a GPU other than the default one”

and discrete GPUs are identified by which GPU is the default GPU.  
Intended for Laptops that make use of Nvidia Optimus or similar, this breaks Desktop Systems by potentially trying to use an integrated GPU over the discrete GPU because it believes we *must* have booted with the integrated GPU.

Okay... what now?  
Most people recommend removing `PrefersNonDefaultGPU` from the desktop file to prevent this issues either by hand or [proposing it developers do it](https://github.com/ValveSoftware/steam-for-linux/issues/9940)  
but this is hardly a solution, when updates to the packages can always just revert the change, breaking things once again.

The best solution would be finding out how to actually detect detect if a GPU is discrete or not, but how can we do this?

Well, it depends on the device, or more specifically, the driver.

#### amdgpu:
this is trival on amdgpu devices:
- query device information
- check if the device has the `AMDGPU_IDS_FLAGS_FUSION` flag set, if so its not a discrete GPU
	+ the [kernel driver sets this flag](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/gpu/drm/amd/amdgpu/amdgpu_kms.c?id=4f5e5092fdbf5cec6bedc19fbe69cce4f5f08372#n887) for any AMD APU, letting us easily identify them

#### nouveau:
this gets a little more complicated, but still managable:
- query device info by sending manual drm commands
- check what device platform it is:
	+ If its an IGP (Integrated GPU) or SOC (System on a Chip) its not discrete
	+ Otherwise its discrete
		* While this could be considered broken, since we shouldn't assume anything we don't know about is discrete, its easier to manage, especially considering Nvidia GPUs in consumer end-devices tend to either be in a single GPU system or discrete.
		

#### nvidia:
Due to its proprietary nature, there isn't really a good way to find this information without poke the device with a proprietary libary.

The workaround for this is to consider ANY device using the nvidia drivers to be discrete.  
I am only aware of the Tegra4Linux project as a Linux System that makes use of an integrated Nvidia GPU but because it is a single GPU System, this does not affect this.

#### i915:
its very much possible to detect if a device using the i915 uses but it involves a ton of poking the device with raw commands.  
This isn't exactly something I want to do, as its an incredibly opaque process and could break easily.

So I went looking for an alterantive and found one: the PCI device ID  
In short: integrated Intel GPUs always tend to be `0000:00:02.0`

I've asked around on a few Discords asking people for their lspci output and of roughly 20 datasets all of them matched this pattern, so this is what I've used.  
Could it be done better? yes, but this is a fine stepping stone to improve the state of things.

---


Okay, we know how to detect Discrete GPUs now, how do we make Desktop Environments consider this?  
The most direct way would be proposing code to each Distro which implements everything outlined above.  
But this is quite a lot, so it would be easier to add it to switcheroo-control and add this new capability to the Desktop Environments

and so I did: [` Improve discrete GPU detection using switcheroo-control `](https://gitlab.freedesktop.org/hadess/switcheroo-control/-/merge_requests/69)  
this is not the initial version I proposed, which was based on heuristics, but the revised version which follows the described behavior above.

Then August 2023 hit and RedHat no longer hat any interested in funding development on switcheroo-control and hadess, the creator of switcheroo-control, was assigned [new responsibilities](https://www.hadess.net/2023/08/new-responsibilities.html) and no longer able to work on switcheroo-control.  
<sup>they could have worked on it in their spare time, but a RedHat employee shouldn't have to donate their time to a company pumped with so much money.</sup>

Around the time of this post the Merge Request was cleaned up, remade onto a new branch so it can be cleanly discussed and receive a fresh description containing all changes in detail.

To help drive this changes were proposed to [GNOME](https://gitlab.gnome.org/GNOME/gnome-shell/-/merge_requests/3193), [KDE](https://invent.kde.org/frameworks/kio/-/merge_requests/1556) and [Cinnamon](https://github.com/linuxmint/xapp/pull/178).  
<sup>If there is any system you would like to see supported, feel free to reach out to me on Discord: **jan200101**</sup>

On Fedora developers can make use of this [COPR Repository](https://copr.fedorainfracloud.org/coprs/sentry/switcheroo-control_discrete/) to test these changes  
The Bazzite distrobution graciously ship these changes in their stable repository so users of it can already test these changes.
