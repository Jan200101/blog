---
author: "Jan Drögehoff"
title: "Automating GitLab labeling"
date: "2022-03-29"
tags: ["Python", "GitLab", "Bot"]
---

# Automation with GitLab

Automating processes is something that can improve any development process by taking over the more mundane tasks for you.

For GitLab that would include managing Labels when, for example, a merge request gets opened or merged.

Anyone familiar with Github Actions might think that using Pipelines is the go  to solutions, as did I, but you really can't find any useful information on the topic and you can't really do anything without an access token.

So what else?

# Automating with Bots

The next best solution is to make a bot account.

For GitLab there are many different ways to interact with their API though but many tend to bring the entire kitchen sink with them.

For what I had intended something that does most of the work for me is better, so I went with [gidgetlab](https://gitlab.com/beenje/gidgetlab), an awesome library based on its github counter-part, [gidgethub](gidgethub).

# Automation Rules

To automate a process you need to define a set of rules on how it needs to act upon certain inputs.

I looked through how the repository I was intending to deploy the bot on was doing their commits and the format was relatively simple:

- Titles start with an issue number
- Descriptions contain `Related to #1`

The first one is simple and can easily be done with a simple regex: `^(?:#|)(\d+)\s`

It will find any number at the start of the title, no matter if it contains a # or not, and puts it within a group.

The second rule was a bit more complicated.

How are we suppose to understand sentence structures and human language?

The easiest way, that I believe is also used by Github, is to use proximity.

First we look for a keyword like `related`, find all words within a short radius and check if they are  number or issue reference using this regex `^#(\d+)$`,

Since we explicitly split by words it *should* only contain a number and nothing else.

So now we defined what we are doing to detect and how.

What now?

# event handling

GitLab events are distributed via webhooks, thus gidgetlab exposes a webserver using aiohttp.

thankfully it abstracts all the handling for us so we can simply do

```py
bot = GitLabBot("Automation")

@bot.router.register("Merge Request Hook")
async def merge(event, gl, *args, **kwargs):
    print("Merge Request Hook was send")
```

through the `event` object we can now receive every piece of information, including the state(open, closed, merged), title and description.

Once we parse that information we must simply send an API request to modify the labels in the referenced issues.

Yet again gidgetlab comes to the rescue and provides us with the `gl` object with which we can send API requests out to the right server, so even if the bot is deployed on multiple GitLab instances it would work out of the box.

`/projects/{event.project_id}/issues/{issue}` is the endpoint we need to view or modify a specific issue and since GitLab has nice API we can simply send a list of strings under `add_labels``and `remove_labels` to only deal with the labels we handle and nothing else.

If everything goes right we should now have a bot that reacts towards events automatically.

## Source Code

My original implementation was a simple script to deal with this [gist](https://gist.github.com/Jan200101/d8e1ecc6820a3d1725f103cfc0a5255a).

But I wasn't happy with it since it doesn't scale well, so I ended up writing a small application that lets you run and manage multiple instances and dynamically load addons [Lab-Bot](https://gitlab.com/modular-gitlab-bot/lab-bot).