#!/bin/bash
# Code for finding proper IP Address of the Cloud Instance
# This script is used to check and update your GoDaddy DNS server to the IP address of your current internet connection.
# Special thanks to mfox for his ps script
# 
#
# First go to GoDaddy developer site to create a developer account and get your key and secret
#
# https://developer.godaddy.com/getstarted
# Be aware that there are 2 types of key and secret - one for the test server and one for the production server
# Get a key and secret for the production server

domain="ryanrobotics.com"   # your domain
name="@"     # name of A record to update
key="9uFzACPZFdL_WDBsFX6PQJ6zGzRQp11Pm3"     # key for godaddy developer API
secret="KgHEPrsHVJUmrCS5W43yUC"   # secret for godaddy developer API


headers="Authorization: sso-key $key:$secret"

# echo $headers

result=$(curl -s -X GET -H "$headers" \
 "https://api.godaddy.com/v1/domains/$domain/records/A/$name")

dnsIp=$(echo $result | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b")
# echo "dnsIp:" $dnsIp

# Get public ip address there are several websites that can do this.
ret=$(curl -s GET "http://ipinfo.io/json")
currentIp=$(echo $ret | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b")
# echo "currentIp:" $currentIp
if [ "$dnsIpa" = "$currentIp" ];
# if [[ "$dnsIp" =! "$currentIp" ]];
 then
#       echo "Ips are not equal"
        request='[{"data":"'$currentIp'","ttl":3600}]'
#       echo $request
        nresult=$(curl -i -s -X PUT \
 -H "$headers" \
 -H "Content-Type: application/json" \
 -d $request "https://api.godaddy.com/v1/domains/$domain/records/A/$name")
#       echo $nresult
fi

# Run programr 
# python ./src/programr/clients/events/majordomo/client.py --config ./bots/ryan/config.yaml --cformat yaml --logging ./bots/ryan/logging.yaml

python ./src/programr/clients/restful/flask/client.py --config ./bots/ryan/config.yaml --cformat yaml --logging ./bots/ryan/logging.yaml