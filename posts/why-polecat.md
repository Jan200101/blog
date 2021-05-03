<!--
.. title: Why Polecat?
.. slug: why-polecat
.. date: 2021-05-02 18:09:47 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: Yet Another Wine Manager
.. type: text
-->

## What is polecat

polecat is a wine manager

similar to other projects like PlayOnLinux or Lutris it allows you to install multiple different wine and DXVK versions and run any of them


## Then how does it differ from those

while POL and lutris target the gaming market polecat is intended to be more generic and allow you to run anything you want

the wine binaries actually come from lutris so there isn't much of a difference between how they act

## If POL/Lutris/XYZ exist why make it?

It all started with lutris

its the goto app for playing non steam games or games that require Windows steam

then when trying to installing a game one day it showed me an empty window

looking into it I found out that the release I had was broken and you couldn't install any games

for the sake of it I opened a PR to fix the issue and created the [lutris-git copr](https://copr.fedorainfracloud.org/coprs/sentry/lutris-git/)

from there it was just a constant stream of issues and troubles which might be because lutris is only actively being worked on by one person: strycore

issues ranging from wrong configurations, absolute symlinks up to broken code due to changes not being done everywhere

## What about POL scripts and Lutris installers?

POL scripts are just glorified bash scripts, literally.

support for it would require some digging into how bash can be invoked


Lutris support is being worked on on the [dev](https://github.com/Jan200101/polecat/tree/dev) branch

![](/images/polecat/unknown.png)

the only part missing being the actual installation part but it will get done within the next decade

## What is it written in?

polecat is written in pure, sadly non portable, C with a minimal amount of dependencies.

many of the smaller things like the command line option parser were written from scratch and designed in a way that allows things to be easily added, removed or updated

![](/images/polecat/2021-05-02_20-53.png)

[source code](https://github.com/Jan200101/polecat)