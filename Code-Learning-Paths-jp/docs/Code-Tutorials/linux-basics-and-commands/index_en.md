---
abstract: Many of the Kubernetes learning paths assume a base level of knowledge of
  Linux and this may not be true for all people. If you're coming from a Windows world,
  then this tutorial is for you. This tutorial also serves to remind others of the
  basic Linux concepts and commands and as a prerequisite to the Kubernetes learning
  path.
authors: ''
completed_date: '2019-03-21'
components:
- docker
- kubernetes
- istio
draft: false
excerpt: Learn Linux basic concepts and commands to start working with containers.
last_updated: '2019-03-21'
meta_description: Learn Linux basic concepts and commands in preparation for learning
  about Kubernetes.
meta_keywords: linux, command-line, basics, kubernetes, docker
meta_title: Linux prereqs for diving into Kubernetes and Docker
primary_tag: containers
pta:
- cloud, container, and infrastructure
pwg:
- containers
related_content:
- slug: https://developer.ibm.com/tutorials/yaml-basics-and-usage-in-kubernetes/
  type: tutorials
- slug: kubernetes-learning-path
  type: series
subtitle: Learn or refresh your memory on Linux basic commands
tags:
- linux
title: 'Linux basics: Prerequisites to learning about containers'
type: tutorial
---

To acquire the skills that you'll need to deploy, administer, and maintain modern cloud technologies, you'll need to know a solid amount of prerequisite information on the topic at hand: Linux&reg; commands and concepts. Since many of the modern cloud technologies leverage the GNU/Linux operating system at their core, this tutorial walks you through a few basics of the Linux Command Line Interface (CLI) and prepares you to use the CLI as you work through several of our [articles](/articles/category/containers/?fa=date%3ADESC&fb=) and [tutorials](/tutorials/category/containers/?fa=date%3ADESC&fb=) on Docker and Kubernetes and our beginner [Kubernetes Learning Path](/series/kubernetes-learning-path). If you are new to Linux, this tutorial should serve as a short introduction to its use. For the previously initiated, I hope that this tutorial reminds you of a few command concepts, and perhaps introduces you to something new.

## Files and directories

We begin with a section that's dedicated to navigating the basic file structure of a standard GNU/Linux operating system. The standard GNU/Linux operating system has a file management hierarchy that organizes the data stored on the computer. Identifying the places where specific data is stored is one of the initial lessons in beginning to understand how the operating system is structured. In an effort to keep from diminishing your existing Linux experience, I'll save the "Introduction to the Linux File System Hierarchy" discussion for another time. Better yet, here's a solid article that covers the [File System Hierarchy](https://www.linux.org/threads/file-hierarchy-standard-fhs.9999/) in great detail. Here, we'll assume that you know your way around a bit, so I'll offer you a few tips (or perhaps a few reminders) on how to easily navigate. You'll need this skill when you're asked to edit files, navigate the file system, make changes, or observe configurations.

### Changing directories with cd

The `cd` command is used to change from the current directory in the [terminal shell](http://www.linuxcommand.org/lc3_lts0010.php) to the desired directory. This command is used very often when navigating the directory structure of a GNU/Linux file system. The syntax is as follows:

```
$ cd [directory]
```

The `[directory]` parameter refers to the desired or targeted directory that you wish to change to, and the **path** through the file system hierarchy to this directory can be provided in a number of ways:

1. [Absolute path](#absolute-path)
1. [Relative path](#relative-path)
1. [Tilde expansions](#tilde-expansions)
1. [Special inodes](#special-inodes)

#### Absolute path

The **absolute path** is the "full pathway" from the [root directory](https://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/the-root-directory.html) (commonly denoted as `/`) to the targeted directory or file where it exists in the file system hierarchy.  Here's a quick example that displays the absolute path:

With the username `jsmith`, on a standard GNU/Linux operating system, the absolute path to her [home directory](https://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/home.html) would be:

```
/home/jsmith
```

_Quick tip: On a standard GNU/Linux operating system, you can get to your home directory by typing `cd` at the command prompt, with no target directory specified._

The example provided above is a rather short path to the targeted directory, but in many cases, the path to a directory can be very long. In this article, we're going to use the file system hierarchy illustrated below:

![file_hierarchy](https://media.github.ibm.com/user/37987/files/b9750700-387e-11e9-94a0-d5a6bb78151c)

With this directory structure, the absolute path to the `pacific_rose` file would be the following:

```
/home/jsmith/grocery_store/foods/produce/fruits/apples/pacific_rose
```

#### Relative path

The true power of a GNU/Linux operating system is in its command line interface (CLI). Performing tasks on Linux often takes you to the CLI where commands are entered. Typing full paths on the command line each time you need them can get tiresome, and this is where relative paths provide us with some support.

A **relative path** is defined as the path to a target directory (or file) _relative_ to the current working directory. Again, let's use the example above. If the current working directory is the `/home/jsmith/grocery_store/foods/produce/` directory, getting to the `fruits` directory is quite simple:

```
$ cd fruits
```

Since the current working directory contains the `fruits` subdirectory, the above command works because is it using a relative path. You can almost characterize this as an 'assumption' that the operating system makes, whenever an absolute path is not specified alongside the `cd` command. Now that you have navigated to the `fruits` directory, you can see the full path to this directory with the `pwd` command:

```
$ pwd
/home/jsmith/grocery_store/foods/produce/fruits
```

The `pwd` (or print working directory) command is handy for viewing the current working directory, which is often displayed in the absolute path format. This shows us how the absolute path and the relative path can be used to navigate the file system hierarchy.

#### Tilde expansions

To make navigating the file hierarchy even easier (especially the file hierarchy created under a user's home directory), standard GNU/Linux operating systems with the **Bash Shell** provide us with [tilde expansions](https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html) to help us as well. To illustrate what a tilde expansion is, let's take a look at this example:

```
$ cd ~
```

The tilde `~` character in the above command maps to the value of the `$HOME` [environment variable](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html#sect_03_02_01), which is normally set to the current user's home directory. This means that the value of this variable changes based on the user who is currently logged in.  On the same system, the `cd ~` command for Jane Smith would take her to the `/home/jsmith` directory, whereas for Mark Jones (logged in with the username `mjones`), the same command would take him to `/home/mjones` directory.

Here are a couple examples of the tilde expansions in use:

* `~` - maps to the $HOME directory
* `~/grocery_store` - the `grocery_store` subdirectory that exists in the $HOME directory
* `~mjones/grocery_store` - the `grocery_store` subdirectory that exists _specifically_ in the $HOME directory of the `mjones` user

#### Special inodes

To dig a level deeper, let's briefly talk about _inodes_. As defined by [Ian D. Allen](http://teaching.idallen.com/dat2330/04f/notes/links_and_inodes.html), _"On Unix, the collection of data that makes up the contents of a directory or a file isn't stored under a name; the data is stored as part of a data structure called an inode."_ In short, directories and files are names that map to _inode numbers_, and there are a number of "special inodes" that can be used to navigate the file system hierarchy. To illustrate, here are a few examples:

The `..` (double-dot) inode can be used to change to the **parent directory** (one level up) in the file system hierarchy:

```
$ cd ..
```

You can also move up multiple levels in the file system hierarchy by concatenating `..` (double-dot) inodes together:

```
$ pwd
/home/jsmith/grocery_store/foods/produce/fruits
$ cd ../ ../
$ pwd
/home/jsmith/grocery_store/foods
$
```

Here, we move up the file system hierarchy from the `fruits` directory to the `foods` directory (two levels above).

The `-` (dash) allows you to change to the previous working directory:

```
$ cd -
```

In case you need to navigate from one directory to another and then back, the `-` (dash) can be used to take you back to the previous working directory, no matter where in the file system hierarchy you are currently working in.

### Changing directories with pushd/popd

This brings us to a second way that Linux users can navigate the file system hierarchy- the `pushd`, `popd`, and `dirs` commands. Together, these 3 shell built-ins allow you to manipulate the [directory stack](https://www.gnu.org/software/bash/manual/html_node/The-Directory-Stack.html#The-Directory-Stack), which is a list of recently visited directories. The data structure used for storing this list of recently visited directories is truly a stack or LIFO (last in, first out) data structure. `pushd` changes the current directory to the targeted directory and adds this new directory to the stack, while `popd` removes the directory listed at the top of the stack, then changes directories to the directory at the top of the stack.

In my personal experience, the `pushd` and `popd` commands are the ones I most often see in automation scripts as a way of creating a "breadcrumb trail" of directories visited. Having this list available helps when an automated task requires you to make changes to files (and directories) in a specific way or in a specific order. A previously visited directory can be _"popped"_ off of the stack and easily revisited.

The `dirs` command is a command I've utilized on fewer occasions, but it also very handy. It allows you to view the directory stack itself to see the list of recently visited directories. This command also has a number of options that allow you to "manage" the stack as needed. Here's an example of using the `pushd`, `popd`, and `dirs` commands:

Starting from the `/home/jsmith/grocery_store/foods/`, we'll use `pushd` to change to the `produce` directory:

```
$ pushd produce
```

The current directory is now the `/home/jsmith/grocery_store/foods/produce` directory, and since we've used `pushd` to change into this directory, it has been added to the directory stack, as show by the `dirs` command:

```
$ dirs
/home/jsmith/grocery_store/foods/produce /home/jsmith/grocery_store/foods
$
```

Notice that the list of directories, from left to right, are listed by most recently visited. We'll use `pushd` again, to move into the `meats` directory, then view the directory stack again:

```
$ pushd /home/jsmith/grocery_store/foods/meats
$ dirs
/home/jsmith/grocery_store/foods/meats /home/jsmith/grocery_store/foods/produce /home/jsmith/grocery_store/foods
$
```

The directory list has now grown to 3 recently visited directories. Now, if we use the `popd` command, the directory listed at the top of the stack is removed, and the current directory is changed back to `/home/jsmith/grocery_store/foods/produce`, as it is now the directory listed at the top of the directory stack:

```
$ popd
$ pwd
/home/jsmith/grocery_store/foods/produce
```

Another glance that the directory stack will show us that the list is back down to two recently visted directories:

```
$ dirs
/home/jsmith/grocery_store/foods/produce /home/jsmith/grocery_store/foods
$
```

For a list of options that are available to the `pushd`, `popd`, and `dirs` commands, take a look at the [Directory Stack Builtins](https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html#Directory-Stack-Builtins) chapter of the GNU.org Bash manual.

In the articles and tutorials to come, easily navigating directory structures will certainly be a handy skill to carry along with you, and hopefully, this brief introduction on navigating the file system hierarchy has intrigued you enough to dive in a little deeper.

### Creating directories

We've covered navigation, now let's quickly cover the creation of directories, which can be achieved with the `mkdir` command:

```
$ mkdir [target]
```

Here in this example, `[target]` is the name for the directory that you wish to create. Upon execution, `mkdir` creates this directory in the current working directory (since a full path was not specified). You can also create new directories at any level of the file system hierarchy, as long as the full path can be determined and your user account has the permissions to do so. For example:

```
$ mkdir /home/jsmith/grocery_store/foods/produce/veggies
```

This creates the `veggies` directory inside the `home/jsmith/grocery_store/foods/produce` directory. Often, you may need to create multiple directories at the same level in the file system hierarchy, and there are even cases where an entirely new directory structure needs to be created. This is where the `-p` command option is quite handy. Here's a _more advanced_ example:

```
$ mkdir -p /home/jsmith/grocery_store/foods/meats/{beef,fish,chicken,pork/{bacon,sausage}}
```

There are a couple of concepts at play in this example. First, the `-p` option allows us to create the "path" specified, whether the directories in the path were previously created or not. Using the parentheses, you can create multiple directories at the same time. Here, we've created the `beef`, `fish`, `chicken`, and `pork` subdirectories inside the `meats` directory (which was _not_ previously created). Furthermore, we continued to create two more subdirectories underneath the `pork` directory as well- the `bacon` and `sausage` subdirectories.  With this, you can readily see the power of the command-line at work, creating whole new directory structures with just one command.

For more information on the `mkdir` command, have a look at [this lifewire article on how to create directories using mkdir](https://www.lifewire.com/create-directories-linux-mkdir-command-3991847).

### Viewing Files and Directories

We discussed how to navigate and create directories on a standard GNU/Linux operating system. Now, let's talk about how we can list directories, view, and edit files. Besides GUI-based applications, there are a couple of ways to view files and directories directly from the CLI.

#### Viewing directory contents with ls

The `ls` command can be used in a variety of ways to view the contents of a directory. A simple `ls` at the command prompt displays (horizontally) the contents of the current working directory:

```
$ ls
```

There are a couple of commonly used command options as well. For instance, adding a `-l` flag to the command, which displays the contents of the target directory, including the file/directory name, permissions, owner, modify date, and file/directory size:

```
$ ls -l
```

The `-a` option displays the contents of the directory, including [hidden files](https://www.ghacks.net/2009/04/16/linux-tips-view-hidden-files/), which are files primarily used for the customization and personalization of your desktop, and for application configurations:

```
$ ls -a
```

**Lesser known command options for ls**

The `ls` command options we've covered so far are the most widely used. However, there are a few more options that can be just as handy as well. Here's a quick list:

| ls commmand | Description |
|-------------|-------------|
| `ls -lh` | Combining `-l` with `-h` allows you to display the file/directory sizes in "human readable" format. |
| `ls -F`  | Appends a `/` to the subdirectories listed in the output |
| `ls -R`  | Recursively lists the contents of the subdirectories |
| `ls -r`  | Displays the output in reverse order |
| `ls -lS` | Displays the output ordered by file size, with the largest files displayed _first_ |
| `ls -ltr`| Combining the `-l`, `-t`, and `-r` options display the output ordered by modification date, with the most recent displayed _last_ |


#### Viewing files with cat

One of the simplest commands for viewing the contents of a file is the `cat` command. `cat`, short for _"concatenate"_, is used to not only view the contents of a file but also for creating files by redirecting the output:

```
$ cat pacific_rose
This is a test file.
$
```

Here, the `pacific_rose` file contains the 'This is a test file.' text. `cat` displays the contents of this file directly in the terminal window, which is the quick and easy way to see what's inside.

Combined with a [redirection operator](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection), you can use `cat` to create files as well:

```
$ cat > granny_smith
```

The command above creates a new file called `granny_smith` inside the current working directory.

```
$ cat apple1.txt apple2.txt apple3.txt > three_apples.txt
```

As mentioned, `cat` is short for _"concatenate"_, and the example above illustrates how you can combine the contents of multiple files into a single file using the `>` redirection operator. 

Here's a list of command flags (or options) that might also be handy to use with the `cat` command:

* `cat -n` will display the line numbers alongside the file output.
* `cat -e` will display the line endings and line spaces, usually with the `$` character, in the file output.
* `cat -T` will display the tab separated lines in the file output.

For more tips on how to use the `cat` command, check out this [LINFO article on the cat command](http://www.linfo.org/cat.html).

#### Viewing files with more/less

Two additional ways to view files directly in the terminal are with the `more` and `less` commands. Both `more` and `less` allow you to view the contents of a file, pausing the file output as it fills up the screen buffer. You can choose to pause there or view the remaining output by pressing any key to continue. However, the `less` command is slightly different. Though it provides the same functionality as the `more` command for viewing files, with `less` you also have the ability to move _backwards_ through the output, where the `more` command only allows forward viewing of the output.

#### Terminal text editors (vim/emacs/pico)

While learning by doing, your Linux-based study often requires you to make changes in order to create, update, and/or remove information from configuration files. Each of these actions can be achieved through the use of text editors made available on most Linux operating systems. They include:

* vi/vim
* emacs
* pico

Each editor has its own set of advantages, disadvantages, and features. Instead of advocating for any one editor over others, here's a short list of resources that will give you tips/tricks for each one:

**vi/vim:**
* [Learn vim For the Last Time: Tutorial and Primer](https://danielmiessler.com/study/vim/)

**emacs**
* [Absolute Beginners Guide to emacs](http://www.jesshamrick.com/2012/09/10/absolute-beginners-guide-to-emacs/)

**pico**
* [Basic Pico Commands](https://www.cs.colostate.edu/helpdocs/pico.html)

### File permissions

As you begin to cover more material on your [learning path](/series/kubernetes-learning-path/), you will eventually stumble upon the need to understand file permissions. As Linux users, we have fine-grained control over what you as a user can do to the files stored on a Linux operating system. In many cases, files and directories are expected to have a certain level of permissions set in order for them to function- making a script executable, for example. So, let's briefly cover file permissions.

```
$ ls -l
-rw-r--r--  1 jdoe  staff  0 Mar 15 08:30 brisket.txt
-rw-r--r--  1 jdoe  staff  0 Mar 15 08:30 ground.txt
-rw-r--r--  1 jdoe  staff  0 Mar 15 08:30 ribs.txt
-rw-r--r--  1 jdoe  staff  0 Mar 15 08:30 tar_tar.txt
```

In this sample directory listing, the file permissions are denoted by the `-rw-r--r--` data provided for each file contained in the directory. Permissions are set on files and directories for 3 account roles: user, group, and others (i.e. everyone else). The permissions that can be granted are read (r), write (w), and execute (x). To illustrate, let's take a look at the following table, that describes how permissions are applied to each file, based on the accounts and groups access it:

If we're reading the file permissions for the `brisket.txt` file from left to right (and omitting the first `-` character), the file permissions are as follows:

| user | group | others |
|------|-------|--------|
|  rw (read/write) |   r (read)  |   r  (read)  |

Full access permissions to a file or directory would be denoted as `rwx`. In this example, the user `jdoe` has read and write permissions, the `staff` group has read permissions, and all others have read permissions.  To understand the UGO (user, group, others) concept, I encourage you to read through this [article on Getting to Know Linux File Permissions](https://www.linux.com/learn/getting-know-linux-file-permissions) for a more in-depth look.

#### Changing permissions with chmod

There are cases where the permissions applied to a file need to be modified. This is where the `chmod` command comes into play. As mentioned previously, bash scripts can be made executable (i.e. having the ability to 'run' by calling the script itself on the command line) by altering the permissions:

```
$ ls -l script_to_run.sh
-rw-r--r--  1 jdoe  staff  0 Mar 15 13:33 script_to_run.sh
$ chmod u+x script_to_run.sh
$ ls -l script_to_run.sh
-rwxr--r--  1 jdoe  staff  0 Mar 15 13:33 script_to_run.sh
```
In the above example, the `script_to_run.sh` now has the `+x` attribute added for the user.  This means that the script is now "executable" by the `jdoe` user.

```
$ chmod ug+x script_to_run.sh
$ ls -l script_to_run.sh
-rwxr-xr--  1 jdoe  staff  0 Mar 15 13:33 script_to_run.sh
```

The above example used both `u` (user) and `g` (group) with the `chmod` command, which illustrates how you can also combine the account roles together to modify the file permissions in parallel. The `+` character adds the executable attribute, and in contrast, the `-` character removes it:

```
$ ls -l script_to_run.sh
-rwxr-xr--  1 jdoe  staff  0 Mar 15 13:33 script_to_run.sh
$ chmod ug-x script_to_run.sh # note the - character here
$ ls -l script_to_run.sh
-rw-r--r--  1 jdoe  staff  0 Mar 15 13:33 script_to_run.sh
```
As you see, `chmod` is a very handy command for fine-tuning your file permissions as needed.

## Basic Docker commands

We covered a whirlwind of command-line examples that will give you a good start with navigating the file system, viewing and creating files and directories, and customizing your terminal shell while using a standard GNU/Linux operating system. However, since this tutorial is meant to be a primer for delving into more advanced Docker, Kubernetes, and Istio tutorials and code patterns, let's briefly list out a few Docker commands to get you started:

### Building Docker images

| Command | Description |
|---------|-------------|
| `docker images` | Lists the locally stored images |
| `docker rmi [IMG]` | Removes the `[IMG]` image from the local image repository |
| `docker build -t [TAG] .` | Builds a docker image from the Dockerfile in the current working directory and tags it as `[TAG]` |

### Running Docker images

| Command | Description |
|---------|-------------|
| `docker run --name [CNT]` | Runs a container and names it is as `[CNT]` |
| `docker run -it` | Attaches to the terminal session of the container |
| `docker rm -f $(docker ps -aq)` | Delete all containers |
| `docker ps` | List the running containers |

### Shipping Docker images

| Command | Description |
|---------|-------------|
| `docker pull` | Pulls an image from the container registry |
| `docker push [IMG]` | Pushes the image named [IMG] to registry |

## Basic Kubernetes commands

Now that we have covered a few of the basic Docker commands, we'll take a look at a few handy Kubernetes commands to help you along the way. Kubernetes employs `kubectl`, a command-line internface tool for running commands against Kubernetes clusters. Below, you'll find a short list of frequently used commands to update and/or extract data from your Kubernetes deployment:

### Listing Kubernetes resources

| Command | Description |
|---------|-------------|
| `kubectl get services` | Lists all kubernetes services inside the current namespace |
| `kubectl get pods --all-namespaces` | Lists all pods across _all_ namespaces |
| `kubectl get pods -o wide` | Generates more detailed pods output from the current namespace |
| `kubectl describe nodes [node-name]` | Gives a brief description of the node `[node-name]` |
| `kubectl describe pods [pod-name]` | Gives a brief description of the pod `[pod-name]` |

### Manipulating Kubernetes resources

| Command | Description |
|---------|-------------|
| `kubectl create deployment foo --image=foo` | Deploys a single instance of `foo` |
| `kubectl create -f ./local-manifest.yaml` | Creates resources via a Kubernetes manifest file named `local-manifest.yaml` |
| `kubectl delete -f ./bar.json` | Deletes the pod as defined in the file named `bar.json` |
| `kubectl delete pod,service silver gold` | Deletes all pods and services with the names `silver` and `gold` |

For a full list of `kubectl` commands see: https://kubernetes.io/docs/reference/kubectl/cheatsheet/.

## Summary

This tutorial is meant to serve as a command-line warmup, "breaking the ice" as you continue to learn about container technologies like [Docker](https://www.docker.com/), [Kubernetes](https://kubernetes.io/), and [Istio](https://istio.io/). It can be a worthwhile exercise to revisit the basics prior to picking up a new skill, and I hope that the topics covered in this tutorial either refreshed your memory or helped you to pick up something new.

## Next steps

After you complete this tutorial, make sure to check out the next steps in the [Kubernetes Learning Path](/series/kubernetes-learning-path/). You can also check out these resources and code patterns if you feel comfortable to play around with containers.

* [Start creating Kubernetes clusters](https://cloud.ibm.com/docs/containers?topic=containers-cs_cluster_tutorial#cs_cluster_tutorial)
* Connect, manage and secure microservices at scale. [Run Istio on the IBM Cloud Kubernetes Service](https://www.ibm.com/cloud/info/istio).
* [Manage Docker container images in a fully managed private registry](https://cloud.ibm.com/kubernetes/catalog/registry?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)
* Code pattern:[ Using Istio across private and public clusters](/patterns/istio-for-multi-clusters-across-iks-and-icp/)
* Code pattern: [Run a Drupal website on Kubernetes](/patterns/run-drupal-website-on-kubernetes/)