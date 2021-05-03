<!--
.. title: OpenFortress Launcher history
.. slug: openfortress-launcher-history
.. date: 2021-02-18 14:09:31 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

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

## SVN

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

## Qt

Since having a graphical interface was a goal of the original launcher I took the design and asked anyone for feedback on it

I thought I had lost the code for the original so I had recreated a similar design from scratch

![](/images/oflauncher/unknown4.png)

with the help of some players I iterated over designs and ended up with this

![](/images/oflauncher/Screenshot_20210502_202148.png)

at this point the launcher was already beyond a simple design and checked your installation to adapt the UI

![](/images/oflauncher/unknown5.png)

and with that it was pretty much done

here is a video of version thats a bit older in action

<iframe src="https://www.youtube.com/embed/vhsZu3XaZWE" title="YouTube video player" frameborder="0" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe>

since then the OpenFortress people have created a system that improves the way assets can be downloaded by indexing them into an SQLite database with [a program](https://github.com/openfortress/launcher-packer)

maybe I'll add that too at some point