#!/bin/sh
# pass the ssh public key of host to ec2 instances


filename='nodeIPaddress'
while IFS= read -r line
do
echo $line
echo "Execution Done!" 
ssh  -n ubuntu@$line 'ls'
done < $filename
