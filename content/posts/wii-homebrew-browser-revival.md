---
author: "Jan Drögehoff"
title: "Wii Homebrew Browser revival"
date: "2021-03-18"
tags: ["C", "Wii", "devkitPro"]
description: "restoring the Homebrew Browser to its glory"
---

[hbb source code](https://github.com/Jan200101/hbb)

# introduction

Back during the big days of Wii Homebrew a user named teknecal decided to take it upon himself and create the Wii Homebrew Browser (HBB from now on)

for the time it was a fantastic piece of software beloved by many, including me

Then it 2012 it received its last update followed by its eventual death.

Fast forward to 2020 Modern Vintage Game released his [Homebrew Wars video about the Xbox and Wii](https://youtu.be/F0EZQsFulJs) and teknecal finally decides to release the source code of the HBB.

The OpenShopChannel team has since created a backup of the source code in a [github repository](https://github.com/OpenShopChannel/HomebrewBrowser) as well as a [fork](https://github.com/OpenShopChannel/OSCHomebrewBrowser) to keep it up to date with bug fixes and links to their own servers.

# spring cleaning

February 2021 I finally dusted off my Wii and set it back up again.

After a bit of cleanup as well as the creation of a new nand backup (you never know) I decided to look at what cool programs there still are and to my surprise there is still some development being done for the Wii.

After looking through some classics like [OpenTTD](https://wiibrew.org/wiki/OpenTTD) I noticed the text saying "Downloadable via the Homebrew Browser" and installed it having had such a great memory using it, but sadly its time had come

the servers were down (or very disfunctional) and I couldn't even start the program :(

Determined to put the project into a state where it can compile and actually run using the modern devkitPPC toolchain I went looking for the source code and noticed CompuCat, a member of the ForTheUsers group, asking for permission to use the code and create  HBB successor, sadly it fell on deaf ears.

Not being one to give up I joined the ForTheUsers Discord and instantly talked to people in the development chat asking if there are any existing efforts to make a new HBB or at least revive it.

Promptly I was informed about the OpenShopChannel (OSC from now on), a project formerly intended to hack the Wii Shop channel and keep it updated but downscaled to keeping HBB running.

The OSC had released a modified version of the original HBB dol file with simple edit to point to their servers something that wasn't enough for me and being told to simply use OSC instead and talk to the team since they apparently got it to compile in their private repository (later I had been told it was made private by accident) I went to make my own out of spite.

I make a lot of things out of spite simply because I am not happy with the state of how things are, so one night I sat down, set up devkitPPC and began working


# reviving a dead codebase

the beginning was a nightmare

the source code wasn't even remotely in a condition to compile it

assets were lying around both in source code form as well as converted C code (and some were missing and had to be recreated from the C code)

various source code of dependencies were stored in-tree as well as a static archive of libpng

binaries across the root of the project folder

a mess in every sense

but I continued and started with some simpler things:
I readded -fcommon (since the defaule behavior changed with GCC 10), fixed the Makefile and removed loads of inline declarations.

Since connecting to a dead server isn't going to show me if I am actually making progress and I didn't want to set one up myself, I grepped the OSC binary to see where their server is: hbb1.oscwii.org

a quick replacing and everything worked but was far from where I wanted to go

next I replaced in the in-tree version of libpngu with the upstream variant in the [GRRLIB repo](https://github.com/GRRLIB/GRRLIB/tree/master/GRRLIB/lib) and made sure I find functions that matched the behavior of the old ones

at this point I grew annoyed at all the object files sitting around and finally added the conversion from binary file to object file so I don't have 2 copies of the same file sitting around

not wanting to rework the code responsible for it yet I simple added a make target to translate all png files to C code
```make
%.c : %.png
	@echo $(notdir $<) 
	@raw2c $<
```

following that I finally went and started replaced the behemoth that was GRRLIB

HBB used an outdated version with a different API as well as extensions copied from the GRRLIB forum like FreeType support.

two days later I was finally done and everything was working as intended and overall more than 1000 lines had to be changed to ensure everything worked as it used to

along the way some interesting results came up

![](/images/hbb/unknown1.png)

![](/images/hbb/IMG_20210306_215457.jpg)

![](/images/hbb/IMG_20210306_220231.jpg)

Afterwards everything was well... except

![](/images/hbb/unknown.png)

Something was obviously wrong somewhere

dhtdht, OSC lead, simply truncated the descriptions to 334 characters and it worked again
but that isn't a solution I am happy with, the issue must occur somewhere else

The first cause I found was this

```c
char text_description[500];

strcpy(text_description, homebrew_list[current_app].app_description);

for(s = strlen(text_description); s < 400; s++) {
	text_description[s] = text_white[0];
	l = s;
}
```

looking at where the description comes from it was obvious we had a stack overflow which had caused the actual texture with the text to have some bad data that manifested itself as corruption like visuals.

But that didn't solve all of it

during the launch of the application for some reason applications caused invalid memory reads for reasons not sure

After some digging I found that in total HBB only had a buffer of 2000 bytes for everything it was send

```c
char cmd_line [2000];
```

the app in the image has a description longer than 2000 characters but that shouldn't be a big deal right?
its only a buffer that we copy somewhere else later

but the copying code calculated using the buffer contents, not the max size of the place we will store it in

```c
strncpy(homebrew_list[array_count].app_name, cmd_line, strlen(cmd_line) - hbb_string_len);
```

we had caused an overflow

a variable was added to check what the max amount of bytes is we can copy over
```c
hbb_null_len = (strlen(cmd_line) - hbb_string_len + 1) > sizeof(homebrew_list[array_count].app_author) ? sizeof(homebrew_list[array_count].app_author) : strlen(cmd_line) - hbb_string_len + 1;  
```

Some other part of the code had problems if I set an incorrect size to copy over so this had to do

some more cleaning of the code had been done including the replacement of 6 different images showing the ratings 0 to 5 being replaced with code and the gray star being replaced with the image being grayscaled which changed the looks a bit but works way better

Being near the end I finally moved from raw2c to bin2o and made all PNGs into objects and had to replace 500 different references to the previous files with the new ones.

Finally done with my changes I made a PR to OSC and left them to their devices
