#!/bin/bash

read -p "Enter start IP address (e.g., 172.17.9.199): " start_ip
read -p "Enter end IP address (e.g., 172.17.9.202): " end_ip

IFS='.' read -r -a start_ip_parts <<< "$start_ip"
IFS='.' read -r -a end_ip_parts <<< "$end_ip"

online_ips=()
csv_file="bruteforce_ips.csv"

for ((i=${start_ip_parts[3]}; i<=${end_ip_parts[3]}; i++)); do
    current_ip="${start_ip%.*}.$i"
    ping -c 1 -W 1 "$current_ip" > /dev/null
    if [ $? -eq 0 ]; then
        online_ips+=("$current_ip")
    fi
done

for online_ip in "${online_ips[@]}"; do
    username_password=$(shuf -n 1 usernames_passwords.csv)
    username=$(echo "$username_password" | cut -d ',' -f 1)
    password=$(echo "$username_password" | cut -d ',' -f 2)
    echo "$online_ip, $username, $password" >> "$csv_file"
done

echo "CSV file created: $csv_file"

# Rest of your script for SSH brute force checking
