---
author: "Jan Drögehoff"
title: "Application Launcher"
date: "2021-02-22"
description: "Creating an application independent program launcher"
tags: ["C++", "Qt", "Steam"]
---

# executable hell

a lot of applications these days are distributed in multiple executable files

especially game mods

launching these programs directly is fine and good but for things like mods for steam games that require a third party executable thats where the problems come in, especially on Linux.

My local install of Modern Warfare 2 with IW4x installed has 3 executables

```text
iw4mp.exe  iw4sp.exe  iw4x.exe 
```

It gets away with this on steam by having 2 different titles for singleplayer and multiplayer

but launching iw4x with the Proton environment is where it gets annoying

I can replace the mp executable but that means I need to deal with moving it when I want to play regular MP

launching it directly without steam can be done in this case but other games may depend on steam running, which wine itself cannot tell if it is

# wrapping around binaries

I copied together some boilerplate code from my other projects [polecat](https://github.com/Jan200101/polecat) and [OFLauncher](https://github.com/Jan200101/OFLauncher) to create a simple Qt application.

the logic is quite simple

```cpp
QDirIterator it(".", {"*" EXE}, QDir::Files);
while (it.hasNext())
{
    it.next(); // we want the filename so lets ignore the output
    QString filename = it.fileName();

    if (!isExe(filename.toStdString().c_str()) || filename.compare(prgm) == 0) continue;

    addButton(filename);

}
```
we iterate over all files in the current directory and check if they are executable files.

On linux we can simply check the executable bit but on Windows there isn't such a straight forward way so we just check if it ends with .EXE

```c
#define EXE ".exe"

int isExe(const char* path)
{
#ifdef _WIN32
    size_t pathlen = strlen(path);

    return strncmp(path + (pathlen - strlen(EXE)), EXE, strlen(EXE)+1) == 0;
#else
    struct stat sb = getStat(path);

    return (sb.st_mode & S_IXUSR) != 0;
#endif
}
```

to be cheap we don't store the executable names or paths ourselves

every executable gets a button added with its name

```cpp
void MainWindow::addButton(const QString name)
{
    QPushButton* button = new QPushButton(this->centralwidget);
    button->setText(name);

    connect(button, &QPushButton::clicked, this, [=]{replaceProcess(name);});

    this->verticalLayout->addWidget(button);
}
```

that button gets a lambda function hooked up to its clicked event giving us access to the name without having to store it ourselves

```cpp
void MainWindow::replaceProcess(QString name)
{
    char* exec = new char[strlen(this->argv[0]) - strlen(this->prgm) + name.size()];
    strcpy(exec, this->argv[0]);
    strcpy(exec+(this->prgm-this->argv[0]), name.toStdString().c_str());
    this->argv[0] = exec;

    if (execvp(exec, this->argv) == -1)
        printf("execvp() %s\n", strerror(errno));
}
```

we keep all but argv[0] the same so we can retain commandline arguments.

argv[0] needs to be modified since many programs expect it to contain its own executable name

the resulting executable is rather simplistic in design but it does its job as advertised

![](/images/steam-wrapper/Screenshot_20210502_195444.png)

[source code](https://github.com/Jan200101/steam-wrapper)