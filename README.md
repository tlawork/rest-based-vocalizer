# rest-based-vocalizer by Todd Lindstrom

This is just a very simple flask rest API application that sits on a computer
and will vocalize for your smart home. It was developed for the Raspberry Pi
though it may function on other computers as well as long as the dependencies 
are met.

It is straight off-the-shelf python3 with a few pip installs so it should work
on other platforms.  The instructions below hold for the RPI-B - its an older
model but its a model that has a builtin headphone adapter - which I took 
advantage of.  

omxplayer is used to play MP3 files - it can output through the HDMI port as well
if you dont use -o local ---> but then you would need an HDMI-> headphone splitter.

# RPI Install

1. install latest Raspian OS
2. Make sure you are getting good internet connection and computer is setup to
the proper locale and keyboard language (you are on your own here - google is your friend)
3. sudo apt update
4. sudo apt upgrade

Now that everything is ready - we need to install a few things

~~~/bash
sudo apt install python3 omxplayer python-espeak pulseaudio python3-pip 
sudo -H pip3 install speake3 flask
~~~

I decided not to use a virtual environment as this RPI is only doing 1 thing - if you want
to use a virtual environment - then please do so.

# GIT GRAB

Grab this repository and put it on your machine at a location where it can be accessed by the root environment - I used the following commands to prepare this:

~~~/bash
sudo mkdir /localview
sudo chmod 0777 /localview
cd /localview
git clone xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
~~~

# Edit /etc/rc.local

Based on my location of /localview/rest-based-vocalizer

I added `sudo /localview/rest-based-vocalizer/startup &` to my /etc/rc.local file.

# HOW TO MAKE THE MP3 FILES

I will finish this section shortly - for now copy the sample mp3 from audio-example
into the audio folder.

