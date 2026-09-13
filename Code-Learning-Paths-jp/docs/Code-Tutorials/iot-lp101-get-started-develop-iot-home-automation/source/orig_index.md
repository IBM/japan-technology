---
abstract: Get started developing IoT solutions quickly and easily. In just four steps,
  learn how you can build a simple home automation IoT solution. After you connect
  the sensors to the Raspberry Pi, you learn how to set up and configure the Pi. Then,
  you learn how to create Node-RED flows to set up the logic for the home automation
  system. Lastly, you learn how to install your prototyped system and begin using
  it.
also_found_in:
- learningpaths/iot-getting-started-iot-development/
authors: ''
completed_date: '2017-06-30'
draft: false
excerpt: Learn how you can build a simple home automation IoT solution in just four
  steps.
ignore_prod: false
last_updated: '2020-01-31'
meta_description: Learn how you can build a simple home automation IoT solution in
  just four steps.
meta_keywords: IoT, sensors, Node-RED, Raspberry Pi
primary_tag: iot
related_content:
- slug: iot-getting-started-iot-development
  type: learningpaths
- slug: iot-next-steps-iot-development
  type: learningpaths
subtitle: Build a smart doorbell with a Raspberry Pi, some sensors, a buzzer, Node-RED,
  and Apple Home Kit
tags:
- iot
time_to_read: 3-4 hours
title: Get started developing IoT solutions by building a simple home automation system
type: tutorial
---

<!-- <sidebar> <heading>IoT 101: Getting started with IoT development</heading> <p>This article is part of the IoT 101 learning path, a quick-start guide for IoT developers.</p> <ul> <li> [IoT concepts and skills](/articles/iot-key-concepts-skills-get-started-iot)</li> <li> [IoT hardware guide](/articles/iot-lp101-best-hardware-devices-iot-project)</li> <li> [IoT networking guide](/articles/iot-lp101-connectivity-network-protocols/)</li> <li> [IoT platforms](/articles/iot-lp101-why-use-iot-platform/)</li> <li>Tutorial: Build a simple home automation system (this tutorial)</li></ul></sidebar> -->

Sometimes the most effective home automation projects are the ones that solve very simple problems.

Here's my simple home automation IoT solution. I have trouble hearing my door bell when I'm working upstairs wearing headphones, so I'm going to create a smart doorbell system:

* I'm going to add a motion sensor to the front door of my house that will activate whenever someone is at the front door.
* I'll also add a temperature and humidity sensor that I can use to monitor the conditions outside my front door at any time, so I won't forget my coat or umbrella when I leave the house if I need them.
* I'll use the PIR sensor to trigger a relay to turn on a strip of LED lights to make it easier to see to unlock the door when I get home after dark.

I'll expose all of these sensors as [Apple Home Kit](https://developer.apple.com/homekit/) devices. Home Kit is Apple's home automation framework that allows you to read from sensors and control smart devices that are installed in your home by using the Home app from an iPhone or iPad running iOS 10, so I'll be able to see the sensor readings from my phone.

 <figure> <heading refname="homekit">Custom Home Kit Raspberry Pi devices</heading> <img alt="" height="348" src="images/Picture1.jpg" width="196"></img></figure>

I'll step through how I built my home automation solution with Node-RED running on a Raspberry Pi with a handful of inexpensive sensors and actuator. You can use this tutorial to [build your IoT skills](/articles/iot-key-concepts-skills-get-started-iot) and build a similar home automation solution, or you can adapt the concepts as you get started with developing your own IoT solutions.

<video-container> <video-id>h4tZi4I8WyU</video-id> <thumbnail-image-url>images/video1thumbnail.jpg</thumbnail-image-url> <video-title>Home Automation Tutorial - Introduction</video-title> </video-container>

[_Transcript of video_](static/transcript01-intro.txt)

## What you’ll need to build this IoT solution

To build this IoT solution, you'll need to be familiar with basic JavaScript and [MQTT](/articles/iot-mqtt-why-good-for-iot/).

I use a MacBook Pro as my development environment, however any Linux or Windows PC with wifi and equivalent software should be suitable. I used the following software and hardware to build my home automation system.

### Software

* Command-line SSH client
* A text editor such as Sublime Text or Atom
* SD card imaging software ([Etcher](https://www.balena.io/etcher/))
* Web Browser (preferably Google Chrome or Firefox)
* Apple Home app (requires an Apple device such as an iPhone or iPad that runs iOS 10)
* Raspbian Buster (to install on micro SD card for Raspberry Pi)
* [Node-RED](https://nodered.org/), which is installed by default on the Raspberry Pi

### Hardware

* Wireless network router
* Raspberry Pi and accessories:
    * Raspberry Pi Zero W or latest Raspberry Pi
    * 40-pin header
    * Raspberry Pi case
    * Micro USB cable and USB power adapter (such as a phone charger)
    * 8 GB micro SD card and adapter for writing to the card from your computer. Either a blank card or one preinstalled with Raspbian Buster.
    * A starter kit like [this one](https://www.adafruit.com/product/3410) from AdaFruit comes with all of these accessories

I'll be running my home automation device off a USB power supply plugged into the main power, so I won't need to worry about batteries or power management. Running off main power also means that it doesn’t have to be a priority for me to select a low power networking technology like Zigbee that would typically be adopted for commercial home automation systems.

Wifi was my preferred choice of networking technology for this project because I already have a Wifi network in my house, and the range of my home automation system only needs to reach within the local area network (LAN) in my house. Wifi also has the advantage of having a high data throughput, which means I should have no trouble gathering data from the connected sensors. You can read more about selecting networking technologies in my article "[Connecting all the things in the Internet of Things](/articles/iot-lp101-connectivity-network-protocols/)."

I've chosen to use a Raspberry Pi Zero W but you could use any Raspberry Pi with wifi. The Raspberry Pi Zero W is a readily available, small, and inexpensive single-board computer with built-in Bluetooth and wifi, which makes it ideal for IoT solutions that need to hook in with an existing wifi network or integrate with consumer devices by using Bluetooth. The Raspberry Pi is a popular board among hobbyists, so there are many online resources and compatible devices available to support developers. I'll be running the device off a USB power supply plugged into the main power, so I won't need to worry about batteries or power management.

For more detail on the hardware requirements to consider when selecting hardware for IoT projects, read my [IoT Hardware Guide](/articles/iot-lp101-best-hardware-devices-iot-project/).

### Electronic components

* [Passive Infra-read (PIR) Sensor](https://www.adafruit.com/product/189). I've used a Keyestudio pyroelectric sensor but any Arduino-compatible digital PIR sensor should work
* [Piezo buzzer](https://www.adafruit.com/product/1536)
* [DHT-11](https://www.adafruit.com/product/386) or [DHT-22](https://www.adafruit.com/product/385) digital temperature and humidity sensor module
* 5V [relay](https://www.amazon.com/Indicator-Light-Channel-Module-Arduino/dp/B00P7QDJD2) module
* [Jumper wires](https://www.amazon.com/Haitronic-Multicolored-Breadboard-Arduino-raspberry/dp/B01LZF1ZSZ/)
* 12 V [LED strip](https://www.amazon.com/WishShop-Strip-Light-NonwaterProof-White/dp/B01N3KPS10) and [power adapter](https://www.amazon.com/Adapter-Transformers-Supply-Output-Listed/dp/B00DKSI0S8/)
* Small solderless [breadboard](https://www.amazon.com/Gikfun-Solderless-Prototype-Breadboard-Arduino/dp/B0146MGBWI/). A breadboard is optional, because you can always just solder wires together instead if you prefer. <br/>
* These miscellaneous components:
    * A small plastic container to house the device
    * Cable tie
    * Double-sided tape

I've selected an off-the-shelf [Passive Infra-red (PIR)](https://en.wikipedia.org/wiki/Passive_infrared_sensor) sensor to detect motion, and a DHT-11 digital temperature and humidity sensor module to attach to my device. These sensors are both inexpensive digital 5V sensors that are compatible with both Arduino and Raspberry Pi. The Raspberry Pi does not have a hardware analog-to-digital converter on board, so digital sensors are a good choice over analog sensors that would require an additional analog-to-digital converter. The output components I'll be using include a Piezo buzzer element to beep whenever motion is detected during prototyping, and a 5V relay with a 12V LED strip that will be triggered by motion in the final iteration of the system.

### Tools

* Philips head screwdriver
* Hobby knife
* Soldering iron

## 1 Connecting the sensors to the Raspberry Pi device

Follow the steps in this video to connect the PIR sensor, buzzer, and DHT11 temperature and humidity sensor. Use the figures and table that follow the video to help you assemble the circuit.

<video-container> <video-id>y7yWGxtnul8</video-id> <thumbnail-image-url>images/video2thumbnail.jpg</thumbnail-image-url> <video-title>Home Automation Tutorial - Assembling the circuit</video-title> </video-container>

[_Transcript of video_](static/transcript02-assemblecircuit.txt)

If your Raspberry Pi did not come with the GPIO pins attached, you'll need to solder the pins onto the board first. The circuit that I used is shown in the following figure.

 <figure> <heading refname="pi-circuit">Circuit with sensors and buzzer (see Acknowledgements)</heading> <img alt="" height="365" src="images/Picture2.png" width="400"></img></figure>

For each component, the positive pin connects to 5V, the negative pin connects to ground (GND), and the data pin connects to a GPIO pin on the Raspberry Pi pin headers, as shown in . In the following table, the number of the pin in the headers is in the middle column, while the Raspberry Pi GPIO pin identifier is shown in the third column. The pin layout of the Raspberry Pi pins is provided in after the table.

 <table border="0" cellpadding="0" cellspacing="0" class="ibm-data-table" data-widget="datatable"> <caption refname="pi-head-gpio">Raspberry Pi pin headers and GPIO pin numbers</caption> <thead> <tr> <th>Sensor/Device</th> <th>Pin header #</th> <th>GPIO pin #</th></tr></thead> <tbody> <tr> <td> PIR Sensor <br/>(Shown at the upper-left of <br/>) </td> <td> 7 </td> <td> GPIO4 </td></tr> <tr> <td> Piezo Buzzer <br/>(Shown in middle of <br/>) </td> <td> 11 </td> <td> GPIO17 </td></tr> <tr> <td> DHT-11 Sensor <br/>(Shown on the right of <br/>) </td> <td> 40 </td> <td> GPIO21 </td></tr> <tr> <td> Relay <br/>(Shown on the right of <br/>) </td> <td> 13 </td> <td> GPIO22 </td></tr></tbody></table>

When you attach components to the Raspberry Pi GPIO headers, refer to the pin diagram in the following figure.

 <figure> <heading refname="pi-pins">Raspberry Pi GPIO pins (image source: <a href="https://elinux.org/File:Pi-GPIO-header.png">https://elinux.org/File:Pi-GPIO-header.png</a>)</heading> <img alt="" height="595" src="images/Picture3.png" width="348"></img></figure>

## 2 Setting up the Raspberry Pi

 <sidebar> <p>If you have chosen to use a different Raspberry Pi with a wifi adapter that allows you to initially set up the Pi over an Ethernet cable, you can read the [docs](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) for how to set up your Pi without a keyboard, mouse, or monitor</a>.</p></sidebar>

The Pi Zero is tiny, so it does not have full-sized ports for HDMI or USB on board. It is possible to add a mini-HDMI-to-HDMI cable or adapter, and also a micro-USB on-the-go adapter and USB hub to plug in a monitor, USB mouse, and keyboard. After you have the Raspberry Pi set up, however, you won't need those peripheral components, so I prefer to skip the dongles and configure the Pi Zero in headless mode.

Here are the steps to setting up your Raspberry Pi for this tutorial:

* Install the latest Raspian OS on the micro SD card
* Add configuration files on the micro SD card
* Start the Raspberry Pi
* Start and set up Node-RED
* Install additional Node-RED modules

### 2a Install the latest version of the Raspian OS on the micro SD card

If you are using a micro SD card that was preinstalled with Raspbian, you can skip this step. However, if you are starting with a blank card, you'll first need to install the latest version of the Raspbian operating system onto the micro SD card. I'm using an 8 GB micro SD card and setting up the card from my MacBook by using an SD card adapter. You can follow along with the [instructions on the Raspberry Pi website](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).

I am not planning on switching between operating systems, so for this project, I decided to use the Raspbian Buster image, rather than NOOBS. I've installed the [Etcher](https://www.balena.io/etcher/) app, so flashing the image to the SD card is as simple as selecting the downloaded .zip file, selecting the micro SD card, and then clicking **Flash**.

 <figure> <heading refname="etcher">Installing Raspbian to the micro SD card by using Etcher</heading> <img alt="" height="506" src="images/Picture4.png" width="938"></img></figure>

### 2b Add configuration files on the micro SD card

You also need to add some configuration files on the SD card to set up the wireless network settings to connect the Pi to the local network.

You need to add a file named `wpa_supplicant.conf` in the root of the SD card. This file contains the wifi settings, including the network password and SSID. Use a text editor like Sublime Text or Atom to edit the contents of the file, add the following lines and specify your values for the `ssid` and `psk` variables:

<code-listing html-highlight="all-highlighting-off" line-numbering="no"><pre>&lpar;newline&rpar;  network={&lpar;newline&rpar;      ssid="&lpar;less-thanwifi network name&lpar;greater-than"&lpar;newline&rpar;      psk="&lpar;less-thanwifi password&lpar;greater-than"&lpar;newline&rpar;  }</pre></code-listing>

You also need to add a file called `ssh` (the file itself doesn't need to contain any content) to the root level of the SD card. The presence of this file will enable SSH on the Pi when it starts up.

### 2c Start the Raspberry Pi

Now you can insert the micro SD card into the Raspberry Pi Zero W, plug a micro USB cable into the power jack on the Pi, and power it up.

Assuming your wireless router is set up to automatically assign IP addresses to connected devices over DHCP, you won't know which IP address your Pi has been assigned to begin with. However, you can use `mDNS` with the _.local_ special-use domain name to find and connect to the Pi without needing to know the address. The most common implementation of `mDNS` is Apple's Bonjour service. If you are on a Mac, this service will work out of the box. On Linux, this service is provided by Avahi (Zeroconf). On Windows, if you have iTunes installed, you will already have Bonjour installed. If not, the quickest way to get your Pi up and running is to install the [Apple Bonjour print services](https://support.apple.com/kb/DL999?locale=en_US).

By default, the Raspberry Pi is configured with the host name _raspberrypi_ and the default user is _pi_, so you can connect to the Pi by using SSH:

<code-listing html-highlight="all-highlighting-off" line-numbering="no"><pre>&lpar;newline&rpar;ssh pi@raspberrypi.local</pre></code-listing>

After you are connected to the Pi, you can run the `ifconfig` command to find its IP address, or check the startup messages when you run node-red. If you don't want to install Bonjour to use mDNS, you may prefer to check your home router DNS logs to find the IP address of the pi and substitute the IP address for the `raspberrypi.local` host name.

### 2d Starting, setting up Node-RED, and installing Node-RED modules

 <sidebar> <p>View the videos in the [Node-RED Essentials playlist](/videos/node-red-essentials) to learn more about working with Node-RED.</p></sidebar>

Node-RED is a development tool with a visual web interface for wiring together IoT flows that connect physical devices, APIs, and other online services. Node-RED and node.js come installed by default with Raspbian, however the version that is bundled with it is a little old. So, one of the first things I did after I booted up the Raspberry Pi was to update Node-RED and node.js and also install some third-party modules to make it easier to work with the DHT-11 temperature sensor and home kit.

 <sidebar> <p>You can read more about <a href="https://nodered.org/docs/hardware/raspberrypi">running Node-RED on Raspberry Pi</a> in the Node-RED documentation.</p></sidebar>

Node-RED provides a graphical web interface for programming IoT flows. The flows connect nodes that represent physical devices and their attached sensors and actuators, with nodes that implement custom functions as well as nodes that provide interfaces to libraries or services, and specify how messages with data payloads are passed between them. We can add additional kinds of nodes by installing additional (contrib) modules. Modules can be added by using the web interface by going to the menu at the upper-right of the web interface, then selecting 'Manage palette' and searching for contributed modules under the Install tab in the sidebar on the left-hand-side of the screen.

In this video, I SSH into my Raspberry Pi, start and upgrade Node-RED, and then install the node-red-contrib-homekit module that is used for integrating with the Apple [Home Kit](https://www.apple.com/ios/home/), all by using the web user interface.

** Note:** Although the Node-RED UI has changed somewhat since this video was recorded, the steps that you follow are still the same.

 <video-container> <video-id>dQWTYWNgAh4</video-id> <thumbnail-image-url>images/video3thumbnail.png</thumbnail-image-url> <video-title>Home Automation Tutorial - Setting up Node-RED on the Raspberry Pi</video-title> </video-container>

[_Trascript of video_](static/transcript03-setupnodered.txt)

In addition to installing Node-RED modules by using the web interface, you can also install modules by using npm on the command line.

For example, install the homebridge module to allow integration with the Apple Home Kit accessories:

<code-listing html-highlight="all-highlighting-off" line-numbering="no"><pre>&lpar;newline&rpar;sudo npm install &#8209;g homebridge</pre></code-listing>

To make it easier to work with the DHT11 temperature and humidity sensor, you need to install the node-red-contrib-dht-sensor module ([https://flows.nodered.org/node/node-red-contrib-dht-sensor](https://flows.nodered.org/node/node-red-contrib-dht-sensor)). The documentation for this module lists a dependency on the BCM2835 library and the node-red-dht module. So, we'll need to install those modules first. <br/>The installation instructions and the latest version of the BCM2835 library are available at [http://www.airspayce.com/mikem/bcm2835](http://www.airspayce.com/mikem/bcm2835). From the command line on the Raspberry Pi, download and install the library by using the following commands:

<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;  cd ~&lpar;newline&rpar;  wget http://www.airspayce.com/mikem/bcm2835/bcm2835&#8209;1.52.tar.gz&lpar;newline&rpar;  tar xzf bcm2835&#8209;1.52.tar.gz&lpar;newline&rpar;  cd bcm2835&#8209;1.52.tar.gz&lpar;newline&rpar;  ./configure&lpar;newline&rpar;  make&lpar;newline&rpar;  sudo make check&lpar;newline&rpar;  sudo make install</pre></code-listing>

After you install the library, change to the _.node-red_ directory and install the node-dht-sensor and the node-red-contrib-dht modules by using npm.

<code-listing html-highlight="all-highlighting-off" line-numbering="no"><pre>&lpar;newline&rpar;  cd ~/.node&#8209;red&lpar;newline&rpar;  sudo npm install &#8209;&#8209;unsafe&#8209;perm &#8209;g node&#8209;dht&#8209;sensor&lpar;newline&rpar;  sudo npm install &#8209;&#8209;unsafe&#8209;perm &#8209;g node&#8209;red&#8209;contrib&#8209;dht&#8209;sensor</pre></code-listing>

 <figure> <heading>Installing the Node-RED -contrib-dht module from npm</heading> <img alt="" height="626" src="images/Picture5.png" width="940"></img></figure>

You can list the modules that you have installed from within the `.node-red` directory with `npm`:

<code-listing html-highlight="all-highlighting-off" line-numbering="no"><pre>&lpar;newline&rpar;   npm ls &#8209;&#8209;depth=0</pre></code-listing>

I've found it's a good idea to restart Node-RED after I install modules manually:

<code-listing html-highlight="all-highlighting-off" line-numbering="no"><pre>&lpar;newline&rpar;   sudo service nodered restart</pre></code-listing>

After you install the DHT module, you'll see the additional DHT22 node type appear in your Node-RED palette (in the web interface).

## 3 Creating flows with Node-RED

I used Node-RED to set up the logic for my home automation system. I use it to read from and control the components hooked up to the Raspberry Pi's GPIO pins. I split the functions into two flows. The first flow reads from the PIR sensor and triggers the buzzer when motion is detected. It also exposes the PIR sensor reading to the Apple Home Kit (you can read more about the [home kit in the Apple documentation](https://developer.apple.com/documentation/homekit)). The second flow reads from the temperature and humidity sensor and sets up two Home Kit devices, one for the temperature, and one for the humidity, so that I'll be able to see these sensor values from the Home app.

### 3a Create the flow for the PIR motion sensor

Follow the steps in the video to set up a Node-RED flow between the PIR sensor and Buzzer so that whenever the PIR sensor detects movements the buzzer beeps. I also configure an Apple Home Kit node so that the state of the motion sensor can be displayed in the Apple Home app on my phone.

** Note:** Although the Node-RED UI has changed somewhat since this video was recorded, the steps that you follow are still the same.

 <video-container> <video-id>99cgVSt_kGE</video-id> <thumbnail-image-url>images/video4thumbnail.png</thumbnail-image-url> <video-title>Home Automation Tutorial - Building Node-RED flows</video-title> </video-container>

[_Transcript of video_](static/transcript04-buildnoderedflows.txt)

You can import the configuration for the completed flow from the [`MotionSensor.json` file in my GitHub repo](https://github.com/AnnaGerber/Home_Automation_with_Raspberry_Pi_and_HomeKit_Node-red).

To import a flow, go to the hamburger menu at the upper-right of the web interface, and select **Import From > Clipboard** then paste in the configuration for the new flow.

### 3b Create the flow for the DHT11 sensor

Follow the steps in this video to add a second flow for the DHT11 temperature and humidity sensor, and expose the sensors as Apple Home Kit devices so you can read the temperature in degrees Celsius, and the relative humidity as a percentage, from within the Home app.

** Note:** Although the Node-RED UI has changed somewhat since this video was recorded, the steps that you follow are still the same.

 <video-container> <video-id>Sn6rSD9tkuc</video-id> <thumbnail-image-url>images/video5thumbnail.png</thumbnail-image-url> <video-title>Home Automation Tutorial - Building more Node-RED flows</video-title> </video-container>

[_Transcript of video_](static/transcript05-buildnoderedflows2.txt)

You can import the completed temperature and humidity sensor flow from the [`TemperatureAndHumiditySensor.json` file in my GitHub repo](https://github.com/AnnaGerber/Home_Automation_with_Raspberry_Pi_and_HomeKit_Node-red).

You can share any of the flows that you create by exporting them to JSON format. To export a flow, select all of the nodes in the flow first, and then go to the hamburger menu and select **Export** (if you don't select any nodes, the export options are disabled).

 <label name="63outline"></label>

### 3c Create the flow for the LED strip lights

Follow the steps in this video to add a relay to the circuit to turn an LED light strip on and off, and trigger this behavior with the PIR sensor. I also step through setting up a home kit device to view and control the state of the LED strip.

** Note:** Although the Node-RED UI has changed somewhat since this video was recorded, the steps that you follow are still the same.

 <video-container> <video-id>0Z2EHy1e2OM</video-id> <thumbnail-image-url>images/video6thumbnail.jpeg</thumbnail-image-url> <video-title>Home Automation Tutorial - Adding a relay and updating a flow for the LED lights</video-title> </video-container>

[_Transcript of video_](static/transcript06-addrelay.txt)

### 3d Attaching the relay

While the Piezo buzzer was great during prototyping for giving instant feedback on whether my door sensor was working, I found that it wasn't very loud after I put it inside the plastic box I was using as an enclosure, so I decided to remove it from the final version of my circuit. Removing the Piezo buzzer also gave me more space in the enclosure to install my [relay](https://en.wikipedia.org/wiki/Relay), the electrically controlled switch that is used to turn a strip of LED lights on and off again.

The circuit diagram for attaching the relay is shown in . As outlined in Table 1, The PIR motion sensor is attached to pin 7, the DHT11 temperature and humidity sensor is attached on pin 40, and the relay has been added on pin 13.

 <figure> <heading refname="pi-relay">Home automation circuit with relay (see Acknowledgements) </heading> <img alt="" height="608" src="images/Picture6.png" width="888"></img></figure>

Each component needs to be connected to a ground and 5V pin, and while there are plenty of ground pins, there are only two 5V pins on the Pi Zero, so you can either use a small breadboard or solder some wires together to share the 5V connection between all three components.

The LED strip needs to be powered by a separate 12V power supply, and wired up to the normally open (marked NO) terminals on the relay so that activating the relay will close these terminals, which will trigger the LED to light up.

## 4 Installing the home automation system (smart doorbell)

After you create all of the electronic circuits and Node-RED flows, the next step is to install the home automation system. I've bundled all of the wires and components together into an enclosure that is made from a clear plastic container with cutouts for the PIR sensor and cables. (I 3D-printed a custom case and waterproofed it using silicone for a more permanent enclosure.)

This video steps you through connecting the relay and LED strip and bundling the components into a prototype enclosure.

 <video-container> <video-id>VblGDtpZUKI</video-id> <thumbnail-image-url>images/video7thumbnail.jpg</thumbnail-image-url> <video-title>Home Automation Tutorial - Assembling the sensors and Pi into a box</video-title> </video-container>

[_Transcript of video_](static/transcript07-installation.txt)

 <figure> <heading>Installed home automation system prototype</heading> <img alt="" height="384" src="images/Picture7.jpg" width="384"></img></figure>

## Summary and next steps

I've stepped through building the circuits and programming the flows for a basic Raspberry-Pi-based home automation system using Node-RED, with Apple Home Kit integration.

Some obvious improvements to this prototype system would be to add a light sensor and only trigger the LED strip to turn on when the strip is in shade or darkness. I have a Bluetooth Low Energy tag (Chipolo) on my house keys, and there is a Node-RED Chipolo module for reading these tags, so an alternative improvement would be to read the tag to recognize when I am approaching the door to turn the lights on, rather than triggering the lights by motion alone.

Because this home automation system is a prototype, I haven't focused on security, however by default Node-RED is not secured. So before installing this system, the next step would be to add authentication and secure the editor (See [https://nodered.org/docs/security](https://nodered.org/docs/security)).

### Acknowledgements

The author used the circuit diagrams from these fritzing components to create her own circuit diagrams for this tutorial:

* AdaFruit library: <br/>[https://github.com/adafruit/Fritzing-Library/](https://github.com/adafruit/Fritzing-Library/)
* DHT11 sensor module: <br/>[http://fritzing.org/projects/ky-015-temperature-and-humidity-sensor-module](http://fritzing.org/projects/ky-015-temperature-and-humidity-sensor-module)
* PIR Sensor and relay: <br/>[https://github.com/rwaldron/fritzing-components/blob/master/components/keyes-relay.fzpz](https://github.com/rwaldron/fritzing-components/blob/master/components/keyes-relay.fzpz)