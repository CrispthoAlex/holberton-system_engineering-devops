# 0x04. Loops, conditions and parsing
![](https://www.youtube.com/watch?v=BC2neyc5GcI&feature=youtu.be)
## Background Context

## Resources
#### Read or watch:

* [Loops sample](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
* [Variable assignment and arithmetic](http://tldp.org/LDP/abs/html/ops.html)
* [Comparison operators](http://tldp.org/LDP/abs/html/comparison-ops.html)
* [File test operators](http://tldp.org/LDP/abs/html/fto.html)
* [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

#### man or help:

* ``env``
* ``cut``
* ``for``
* ``while``
* ``until``
* ``if``

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* How to create SSH keys
* What is the advantage of using ``#!/usr/bin/env bash`` over ``#!/bin/bash``
* How to use ``while, ``until`` and ``for`` loops
* How to use ``if``, ``else``, ``elif`` and ``case`` condition statements
* How to use the ``cut`` command
* What are files and other comparison operators, and how to use them

# More Info
### Shellcheck
[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code SC2034, [you can browse](https://github.com/koalaman/shellcheck/wiki/SC2034).