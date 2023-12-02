## Overview ... 

Control the sphero RVR with python code and HCSRO4 ultrasonic sensors. These sensors help the RVR know where it is going by sending out pulse signals and receiving those signals back, effectively telling the RVR how close it is to an object so that it can avoid colliding with the objects. 

The pi can be ssh'd into from the mac with the following commands: 

1. ssh pi@<raspberrypi_ip_address>

2. ssh pi@raspberrypi.local

The raspberrypi IP address can be found by logging into the raspberry pi and typing: 

hostname -I into the pi's terminal

Once connected to the raspberry pi from the mac, python code can be ran by navigating to the directory that has contains the python code and running: 

python3 <filename.py>

in this case we want to run the SpheroSRO4.py file, so the command would be: 

cd cs2340

python3 SpheroSRO4.py 

Special permissions may need to be enabled by pasting these commands into the terminal before running the script: 

sudo chown root:$USER /dev/gpiomem
sudo chmod g+rw /dev/gpiomem



