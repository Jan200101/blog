<!--
.. title: Zork segmentation fault
.. slug: zork-segmentation-fault
.. date: 2021-02-18 17:00:55 UTC+02:00
.. tags:	 
.. category:
.. link: 
.. description: a short story about how I fixed Zork crashing
.. type: text
-->

[upstream patch](https://github.com/devshane/zork/pull/14)

# prelude

On May 10th 2020 Štefan Gurský opened a [bug report](https://bugzilla.redhat.com/show_bug.cgi?id=1833823 "Fedora bug report") about Zork crashing

a bunch of back and forth concluded that the issue was somewhere on Fedoras side, but where?

January 30th 2021 J.W.F., a fellow Fedora maintainer, send this into the Fedora Packaging Community Telegram:

> BTW… if anyone here is a pro C programmer, I could use help fixing Fedora's zork package… it has been broken on Fedora since Fedora 30 or 31. It segfaults once you enter any command, e.g. open mailbox

Fast forward to February 4th 021 I decide to join the Telegram group and read the message

I point some people in the right direction with help they need and don't do much more
until February 17th where J.W.F. reminds me of Zork segmentation faulting

Dabbling around with C a lot in my free time I figured to give it a try since this isn't the original Fortran version but instead the [C Port](https://github.com/devshane/zork/ "Ported Zork Source Code")

# Finding the bug

Having had trouble with compiler optimizations in the past I believed it to be an easy bet
And forcing -O2 out of the Fedora C flags did make it compile as intended
but simply disabling optimizations is not optimal, many code paths could be vastly improved by it
so finding the actual bug was the goal.

Attaching GDB didn't prove useful at first
the port decided to keep a lot of Fortran semantics as well as C optimizations which made it hell to read.

After identifying where it crashed I decide to look for oddities

(Full codeblock)
```c
 L200: 
 	i__2 = prplnt; 
 	for (j = 1; j <= i__2; j += 3) { 
 /* 						!LOOK FOR PREPOSITION. */ 
 	    if (lbuf1 == prpvoc_1.pvoc[j - 1] && lbuf2 == prpvoc_1.pvoc[j]) {
 		goto L4000;
 		}
```

the crash happens in this line
```c
if (lbuf1 == prpvoc_1.pvoc[j - 1] && lbuf2 == prpvoc_1.pvoc[j]) {
```

sounds like pvoc isn't big enough
so perhaps its too short?

No amount of changes to it did anything so I one step up we go
  
```c
for (j = 1; j <= i__2; j += 3) {   
```
hmm

perhaps j is simply jumping out of the bounds of pvoc because it increments by +=3?

Nope still crashes, we must go higher

```c 
i__2 = prplnt;
```

prplnt resolves to  
```c
int prplnt = 48;   
```

So thats it

a simply printf after the i__2 is set and... it works?

following this I tried adding some sort of simple safeguard to see if that would fix it
but nothing else I tried exhibited the same behavior

By now I decided to look back at the gdb output and looked closer

## debugger to the rescue
```text
#0  sparse_ (lbuf=0x7ffd54c, lbuf@entry=0x7ffd550, llnt=3, vbflag=vbflag@entry=1) at np1.c:128
        ret_val = -1
        i__1 = 3
        i__2 = <optimized out>
        i = 3
        j = 44617
        obj = <optimized out>
        prep = 0
        lbuf1 = 3258
        lbuf2 = 0
```
i__2 being optimized out sounds fine

but j is way higher than the 48

something went *horribly* wrong

Looking around some more I found that i__1 and i__2 are are variables all across `sparse_` as placeholders for variables...
and gcc decided to optimize it out to a value used in another area

by this point its almost midnight so I made a simple fix, made a commit and gave this patch to J.W.F.

```diff
From d09b4f2e02e0e9c8ea7d13d39a86d2adf7514619 Mon Sep 17 00:00:00 2001
From: Jan200101 <sentrycraft123@gmail.com>
Date: Thu, 18 Feb 2021 00:02:22 +0100
Subject: [PATCH] stop reused integers from being optimized out

Signed-off-by: Jan200101 <sentrycraft123@gmail.com>
---
 np1.c | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/np1.c b/np1.c
index 8c6c21b..5afc130 100644
--- a/np1.c
+++ b/np1.c
@@ -27,7 +27,7 @@ logical vbflag;
     const integer r50wal = 36852;
 
     /* System generated locals */
-    integer ret_val, i__1, i__2;
+    volatile integer ret_val, i__1, i__2;
 
     /* Local variables */
     integer i, j, adj;
-- 
2.29.2
```

and went to sleep

the repository hasn't had a commit for over 4 years so I had my doubts if it was ever going to get fixed so providing a patch to use in the package was the first thing that came to mind.


Half an hour later, after validating the fix does indeed work, he opened a [PR](https://github.com/devshane/zork/pull/14) in hopes getting the issue fixed at the source.

I wasn't exactly descriptive what the problem was when I uploaded the patch so the next day I gave an explanation to what was causing it as well as how I came to the conclusion, in the case I might have been wrong

skip to next month and the fix was included upstream and I was owed a Fedora karma cookie :)