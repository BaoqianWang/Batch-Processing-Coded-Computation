#!/bin/sh
# pass the ssh public key of host to ec2 instances


filename='nodeIPaddress'
while IFS= read -r line
do
echo $line
echo "Execution Done!"
#ssh -i /home/baoqian/.ssh/linux_key_pari.pem -n ubuntu@$line 'sudo apt-get -y install python3-pip &&sudo pip3 install numpy && sudo pip3 install mpi4py'
ssh -i ~/AmazonEC21224/.ssh/linux_key_pari.pem -n ubuntu@$line ' sudo apt-get -y install python3-tables '
done < $filename
