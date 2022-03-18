---
also_found_in:
- learningpaths/get-started-containers/
authors: ''
check_date: '2021-12-03'
completed_date: '2019-04-02'
components:
- docker
draft: false
excerpt: Learn about Docker commands, Dockerfiles, and using Docker with container
  registries.
last_updated: '2020-12-03'
meta_description: Learn container basics and Docker commands, write a Dockerfile,
  build Docker images, create a working container instance, and use the Quay container
  registry.
meta_keywords: docker container, dockerfile, docker image, container tutorial, docker
  tutorial
meta_title: 'Container basics: Write a Dockerfile and build Docker images'
primary_tag: containers
related_content:
- slug: accessing-dockerhub-repos-in-iks
  type: tutorials
- slug: docker-dev-db
  type: tutorials
- slug: introduction-to-containers-with-nodejs-and-kubernetes-on-openshift
  type: videos
related_links:
- title: Install Docker
  url: https://docs.docker.com/get-docker/
- title: Best practices for writing Dockerfiles
  url: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- title: How to use Docker volumes
  url: https://docs.docker.com/storage/volumes/
- title: Red Hat Quay container registry
  url: https://quay.io/
subtitle: Docker commands, Dockerfiles, and using Docker with container registries
time_to_read: 45 minutes
title: 'Containerization: Starting with Docker'
---

If you are starting your journey into the containerized world, the first thing you'll come across is <a href="(https://www.docker.com/" target="_blank" rel="noopener noreferrer nofollow">Docker</a>. This tutorial gives you a quick start by providing you with the tools to play with Docker, Dockerfiles, and the Red Hat Quay container registry.

## Prerequisites

* Docker account. [Free pricing plans](https://www.docker.com/pricing/) are available.
* [Red Hat Quay.io](https://quay.io/) account. [Free trials](https://quay.io/plans/) are available for 30 days.

## Estimated time

Completing this tutorial should take you approximately 45 minutes.

## Docker

The first thing you need to do is install Docker. There are a few ways to do this, but the first and best place to is by going to the main <a href="https://docs.docker.com/get-docker/" target="_blank" rel="noopener noreferrer nofollow">Docker documentation site</a>. Try to use and maintain the most current version of Docker, and install it for your particular operating system.

At the time of writing this tutorial, there are two main editions of Docker. I'd like to take a moment to discuss the different versions here. There is Docker Community Edition, or `docker-ce`, and Docker Enterprise Edition, or `docker-ee`. They both have advantages and are aimed at different use cases. I strongly suggest after you walk through this tutorial, that you revisit whether `docker-ce` or `docker-ee` is the better fit for you.

The following steps and commands should work on either version, so let's proceed.

### Docker CLI

After you have `docker` installed, bring up a command prompt. During the installation, there is a sanity check that the documentation may ask you to run. We are going to run the following again to make sure everything is working as expected.

```
docker run hello-world
```

You should see something similar to the following output. (If you get an error or something that looks nothing like the below, your installation is not set up correctly and you should resolve this before going any farther.)

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

Congratulations! You have a working `docker` instance. Let's start playing with it.

The next command I'd like you to try is the following. Depending on your internet access, it could take a little time to run, but luckily it will be cached on your machine, after which we'll revisit in a bit.

```
docker run -it centos:latest /bin/bash
```

As this runs, let's talk about what's happening. When you run the `docker` command. You're telling Docker that you want the `latest` copy from the public Docker hub and run it with the shell of `/bin/bash`.
The command runs off to the Internet, sees the version you have, checks against either the SHA of your cached image, or if you don't have it, pulls it down from Docker Hub.
For clarity's sake, the `-it` runs it as `interactive` and creates a `tty` for the container.
You should see the following now.

```
Unable to find image 'centos:latest' locally
latest: Pulling from library/centos
a02a4930cb5d: Pull complete
Digest: sha256:184e5f35598e333bfa7de10d8fb1cebb5ee4df5bc0f970bf2b1e7c7345136426
Status: Downloaded newer image for centos:latest
[root@2de726a5fcb8 /]#
```

Congratulations! You now have your second running Docker container. Go ahead and type `exit`, and run that `docker` command again.

```
[root@2de726a5fcb8 /]# exit
exit
$ docker run -it centos:latest /bin/bash
[root@583c6cec5d41 /]#
```

Notice how the roots `@2de726a5fcb8` and `@583c6cec5d41` are different? It's because when you spin up containers this way they are ephemeral. Ephemeral means they only live for the time that they are running, so as soon as you exit it goes away. I'll show you how to do longer lived containers in a little while.

Now let's play around in the container for a second. With a <a href="https://www.centos.org/" target="_blank" rel="noopener noreferrer">CentOS machine</a>, you have `yum` so let's install something.

```
[root@583c6cec5d41 /]# yum install vim

[-- snip --]

Transaction Summary
=======================================================================================================
Install  1 Package (+32 Dependent packages)

Total download size: 19 M
Installed size: 63 M
Is this ok [y/d/N]: y

[-- snip --]

  perl-podlators.noarch 0:2.5.1-3.el7                  perl-threads.x86_64 0:1.87-4.el7
  perl-threads-shared.x86_64 0:1.43-6.el7              vim-common.x86_64 2:7.4.160-5.el7
  vim-filesystem.x86_64 2:7.4.160-5.el7                which.x86_64 0:2.20-7.el7

Complete!
[root@583c6cec5d41 /]#
```

Now you can run `vim` in your container! Try it out.

```
[root@583c6cec5d41 /]# vim
```

If you don't know how to exit `vim`, type: `:q` and you should see your command prompt again.

Now type `exit` again.

```
[root@583c6cec5d41 /]# exit
exit
$ docker run -it centos:latest /bin/bash
[root@86f1f3872cbe /]# vim
bash: vim: command not found
[root@86f1f3872cbe /]# exit
exit
$
```

And just to reinforce, when your container is gone, any and all changes inside it are gone too.

### Dockerfile

Okay, so we can spin up a container and make changes to it, but how do we keep changes around? There are a few ways, and I encourage you to discover them yourself. However, I'll walk you through the most common way, which is by using a `Dockerfile`.

Back at your command prompt, make a new directory and change the directory by using your `$EDITOR` of choice to open a new file called `Dockerfile`.

```
$ mkdir docker-tutorial
$ cd docker-tutorial
$ $EDITOR Dockerfile
```

I'll hit the highlights of `Dockerfiles` here, but I strongly suggest you take a look at the <a href="https://docs.docker.com/develop/develop-images/dockerfile_best-practices/" target="_blank" rel="noopener noreferrer nofollow">Best practices for writing Dockerfiles</a> documentation to get a taste of their power.

In your `Dockerfile`, write out the following:

```
FROM centos:latest
RUN yum install vim -y && mkdir /vim
WORKDIR /vim
ENTRYPOINT ["vim"]
```

Save the file and make sure it's called `Dockerfile`.

Let's talk about what the four previous lines mean.

* `FROM`       : creates a layer from the `centos`:`latest` Docker image
* `RUN`        : builds your container by installing `vim` into it and creating a directory called `/vim`
* `WORKDIR`    : informs the container where the working directory should be for it
* `ENTRYPOINT` : is the command that is run when the container starts, instead of `/bin/bash` like how we did above

Now let's build this locally. Run the following in the directory that the `Dockerfile` is located and let's see this come
together:

```
$ docker build .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM centos:latest
 ---> 1e1148e4cc2c
Step 2/4 : RUN yum install vim -y && mkdir /vim
 ---> Running in ebd37633ab31
Loaded plugins: fastestmirror, ovl
Determining fastest mirrors
 * base: mirror.fileplanet.com
 * extras: mirror.ash.fastserv.com
 * updates: www.gtlib.gatech.edu
Resolving Dependencies

[-- snip --]

Step 4/4 : ENTRYPOINT ["vim"]
 ---> Running in 82618eb1e891
Removing intermediate container 82618eb1e891
 ---> eda2652aa25e
Successfully built eda2652aa25e
$
```

**Note**: You should have a different hash `eda2652aa25e`, so please keep that in mind.

Congratulations! You have built your first `Dockerfile` and customized Docker container.

Let's give it a run now. Go ahead and run the following command:

```
$ docker run -it eda2652aa25e
```

You should see `vim` start up! Remember, `:q` is how to quit it, and then you should see your command prompt again. You can run this as many times as you'd like and you'll have a new instance of `vim` each time; but you can't actually save anything or read anything because it's a container right? Let's fix this.

We are going to add a bind mount and volumes to mount the local directory into the container. If you'd like to read more about mounts and volumes, I suggest starting with the <a href="https://docs.docker.com/storage/volumes/" target="_blank" rel="noopener noreferrer nofollow">Docker documentation about how to use volumes</a>. It's one of the harder concepts, but it's worth your time.

On your command line, create a file called `hello`, then save the words `hello world` in it.

```
$ EDITOR hello
```

Now let's mount the local directory into our container.

```
$ docker run -it -v ${PWD}:/vim eda2652aa25e
```

Inside of `vim`, type `:e hello`. You should see `hello world` come up! As you can see, you opened the file that you created on the host machine, created a container with `vim` inside, mounted the directory, and was able to open the file!

If you'd like, you can type `i` and type something out. Then type `:wq` when you're done. The container should close out and then you can type the following on your command line:

```
$ cat hello
hello world
I added this line from my container
$
```

**Note**: Obviously, `I added this line from my container` is what I wrote. You will see whatever you write.

Awesome! Now let's start figuring out how to share this container to the world.

## Container registries

I'm going to introduce you to Red Hat offering called Quay.io. It's a cloud-based, open source public container registry that has some neat nice-to-haves built into it. You can host your own if you want to, but this example just uses the public one.

First, go to <a href="https://quay.io/" target="_blank" rel="noopener noreferrer nofollow">Quay.io</a> and create an account.

Now, let's log in, and get ourselves situated.

```
$ docker login quay.io
Username: jjasghar
Password:
Login Succeeded
```

My username is `jjasghar`. Change the username to be yours. Wonderful, you're now loggged in.

If we want to create a container and push it to Quay, it's actually quite easy. I'll show you the commands and then explain them.

```
$ docker build -t quay.io/jjasghar/vim .  
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM centos:latest
latest: Pulling from library/centos
Digest: sha256:76d24f3ba3317fa945743bb3746fbaf3a0b752f10b10376960de01da70685fbd
Status: Downloaded newer image for centos:latest
 ---> 0d120b6ccaa8
 Step 2/4 : RUN yum install vim -y && mkdir /vim
  ---> Running in 4818f1e81f74
  CentOS-8 - AppStream                            3.2 MB/s | 5.8 MB     00:01
  CentOS-8 - Base                                 1.2 MB/s | 2.2 MB     00:01
  CentOS-8 - Extras                               3.6 kB/s | 8.6 kB     00:02
  Dependencies resolved.
  ================================================================================
   Package             Arch        Version                   Repository      Size

[-- snip --]

Complete!
Removing intermediate container 4818f1e81f74
 ---> d566a180f683
Step 3/4 : WORKDIR /vim
 ---> Running in 8b9b16611a82
Removing intermediate container 8b9b16611a82
 ---> 06166d346df4
Step 4/4 : ENTRYPOINT ["vim"]
 ---> Running in 63856bad104f
Removing intermediate container 63856bad104f
 ---> dc5de217e843
Successfully built dc5de217e843
Successfully tagged quay.io/jjasghar/vim:latest
$ docker push quay.io/jjasghar/vim:latest
The push refers to repository [quay.io/jjasghar/vim]
10c0147b9d97: Pushed
291f6e44771a: Pushed
latest: digest: sha256:cf98f2fb8f268020a59363d4ccf2e5963783ce8628478899274485fc7d874bf0 size: 741
```

As you can see, I built the container like we did earlier, but I added `-t quay.io/jjasghar/vim:latest` as the "tag." I tell `docker` that I'm sending it to a different registry, then to the default Docker Hub, and to _my_ namespace.

After the build is done, I just use `docker push quay.io/jjasghar/vim:latest` and it's up! (By default, when you push your first container to Quay.io, you must make it public).

Check out the <a href="https://quay.io/repository/jjasghar/vim?tab=settings" target="_blank" rel="noopener noreferrer nofollow">`https://quay.io/repository/jjasghar/vim?tab=settings`</a> website (substitute `jjasghar` with your namespace) and click __Make public__. Now you can pull to any machine that can talk to the Internet!

Next, let's pull your container down by running the following command:

```
$ docker run -v ${PWD}:/vim -it quay.io/jjasghar/vim:latest
Unable to find image 'quay.io/jjasghar/vim:latest' locally
1: Pulling from jjasghar/vim
a02a4930cb5d: Already exists
209873925a88: Pull complete
Digest: sha256:831fcbac319dda1aab3d022c408ecc5cc1c1b825bcd90fc7694c3d4f0ef4eb9a
Status: Downloaded newer image for quay.io/jjasghar/vim:latest
# and you should see vim now
```

Success! You now know how to create a container and published it to Quay.io.

## Summary

Thanks for walking through this with me. Hopefully, you feel more comfortable with some generic `docker` commands, how `Dockerfiles` work, and finally how to use a container registry. If you have any questions or thoughts, never hesitate to reach out to me via Twitter <a href="https://twitter.com/jjasghar/" target="_blank" rel="noopener noreferrer nofollow">@jjasghar</a>.

So now that you completed this tutorial and know how to use Docker and container registries, what's next? You can further your personal learning with containers and orchestration by going through our [Kubernetes learning path](/series/kubernetes-learning-path). If you're interested in experimenting with Docker some more, try the following tutorials:

* [Gain access to your Docker Hub public and private repos](/tutorials/accessing-dockerhub-repos-in-iks/)
* [Create a database in a Docker container for local development](/tutorials/docker-dev-db/)