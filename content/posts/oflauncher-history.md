---
author: "Jan Drögehoff"
title: "OFLauncher history"
summary: "Open Source Launcher for the Open Fortress mod"
date: "2022-02-10"
tags: ["C", "C++", "Qt"]
---

# 2020

After continuing some work on getting the updated UI ported to Linux I started experimenting with the idea of a launcher

first designs were rather simple and naive in nature

![](/images/oflauncher/unknown.png)

![](/images/oflauncher/unknown1.png)

after talking a bit about this in a Discord server I am in a friend of mine decided to create a mockup for a launcher

![](/images/oflauncher/unknown2.png)

Implementing it was a bit rough and since I wanted to use OpenFortress assets some things needed to be changed

![](/images/oflauncher/unknown3.png)

after that I stopped wanting to work on any of it and concluded any work on OpenFortress

the old source code has been archived on [this branch](https://github.com/Jan200101/OFLauncher/tree/2019) for the sake of archival

# 2021

After a lot of events (including getting banned from the OpenFortress server due to me being confused with another person) I came back and looked at what was there

A User called VoxelTek had posted a link to their Linux script to install OpenFortress

having seen his script I opened a [PR](https://github.com/VoxelTek/OF-Linux-Script/pull/1) to make it a shell script instead of calling shell commands in python

the response

> you might be better off creating your own project.

lead to me doing exactly that

[ofman](https://github.com/Jan200101/ofman) was a shells script inspired by [r2mod_cli](https://github.com/foldex/r2mod_cli)

![](/images/oflauncher/2021-05-02_20-08.png)

from there on I remembered that I the plan to make a launcher in the past so I archived ofman and created [OFLauncher](https://github.com/Jan200101/OFLauncher)

since I can't simply pull together a bunch of binaries to do the heavy lifting

there isn't a lot I can say about most parts except for the SVN code

### SVN

when adding support SVN I just used the standard svn library
which created simple yet powerful code

```c
int svn_checkout(char* path, char* url)
{
    err = svn_client_checkout(NULL, url, path, &rev, true, ctx, pool);

    return handle_error();
}

int svn_update(char* path)
{
    svn_revnum_t tmp;

    err = svn_client_update(&tmp, path, &rev, true, ctx, pool);

    return handle_error();
}
```

([source code](https://github.com/Jan200101/OFLauncher/tree/svn-lib))


but during development I used

the [M cross environment](https://mxe.cc) to compile the program for the Windows platform

which didn't build svn with serf to there was no support for fetching over http/https

without support I had to fall back to either loading a svn dll or calling the svn binary

I had no conscistent place to get a free libsvn.dll from so I resorted to calling the svn binary which resulted in interesting code

```c
int svn_checkout(char* path, char* url)
{
    char exec[PATH_MAX] = {0};
    strcpy(exec, "\"");
#ifdef _WIN32
    strcat(exec, "\"");
#endif
    strcat(exec, SVN);
    strcat(exec, "\" " SVN_CHECKOUT " \"");
    strcat(exec, url);
    strcat(exec, "\" \"");
    strcat(exec, path);
    strcat(exec, "\"");
#ifdef _WIN32
    strcat(exec, "\"");
#endif

    return system(exec);
}
```

You might wonder about the windows preprocessors and I can only link you this SO post [https://stackoverflow.com/a/9965141](https://stackoverflow.com/a/9965141)

### Qt

Since having a graphical interface was a goal of the original launcher I took the design and asked anyone for feedback on it

I thought I had lost the code for the original so I had recreated a similar design from scratch

![](/images/oflauncher/unknown4.png)

with the help of some players I iterated over designs and ended up with this

![](/images/oflauncher/Screenshot_20210502_202148.png)

at this point the launcher was already beyond a simple design and checked your installation to adapt the UI

![](/images/oflauncher/unknown5.png)

and with that it was pretty much done

here is a video of version thats a bit older in action

{{< youtube vhsZu3XaZWE >}}

after this OF was temporarily shut down due to a request by Valve and OFLauncher lost its purpose...


## 2022

May 26, 2022 OpenFortres was released again

With it came the release of the Toast Versioning System (TVN) initially available as a Python library called OFToast, now pytoast by int-72h, a developer for the OpenFortress project. [Github](https://github.com/int-72h/pytoast)

It provided all the utitlities for dealing with TVN information as well as creating repos for it.


The first implementation of an installer using it was of-jam (formerly oflauncher-rei, [Github](https://github.com/int-72h/oflauncher-rei)), a simplistic Python GUI that did the job.

Along the way it gained many new features and overhauls leaving us with this

![](/images/oflauncher/oftoast.png)


Following that initial implementation was murse ([SourceHut](https://git.sr.ht/~welt/murse)) by one of the creators of the versioning system, welt.

It was written in go and improved speed while also making the process way more reliable and stable, getting rid of any bugs the python implementation had.

The only major difference to the Python implementation was that it lacked a Graphical User Interface and did not provide any way of launching the game.
As of September 29, 2022 murse is the official implementation to be used on Windows and Linux


OFLauncher was left for dead simply because of all the cruft that it had developed over time.
In its place a new launcher was born, OFQT.
It included a pure C library for handling tvn information, various frontends for it and various sub libraries intended to make the lifes of frontends easier.


![](/images/oflauncher/ofqt1.png)

It takes its core design from OFLauncher but refines it a bit to unify the launcher elements into the footer and leave space in the middle for future updates, in this case an RSS feed with changelogs.

Because of the direct access to the update information OFQT can now accurately display what is going on and give an accurate bar on how far it is in processing data

![](/images/oflauncher/ofqt2.png)

For launching it has 3 different approaches that can be changed at compile time:

- Direct

Launches the Source SDK 2013 directly with the right options
On Linux this requires a special Environment variable "SteamEnv" to make it use the Steam Runtime

- Steam Naive

Launches OF using steam://rungameid/11677091221058336806
The ID for OF has been static for a while, though no one is quite sure why it is this number

- Steam

passes commandline arguments to Steam to launch the Source SDK 2013 with specific flags
