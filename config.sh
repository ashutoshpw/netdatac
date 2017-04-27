#!/bin/bash
echo "Enter your email where you want to receive alerts: "
read  email
echo "$email" > /root/.forward
echo "Enter your ADMIN Panel IP Address: "
read  ip
ipco="ufw allow from '$ip' to any port 19999"
eval $ipco
