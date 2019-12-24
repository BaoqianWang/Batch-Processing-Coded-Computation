exit
ls
rm id_rsa.pub 
mv linux_key_pari.pem .ssh/
ls
cat id_rsa_u1.pub >>.ssh/authorized_keys 
cd .ssh
ls
scp -i linux_key_pari.pem ubuntu@172.31.36.19
ls
ssh-keygen -t rsa
ls
scp -i linux_key_pari.pem id_rsa.pub  ubuntu@172.31.36.19:~/id_rsa_u2.pub
ssh ubuntu@172.31.36.19
ping 10.230.194.117
ping 10.230.194.117.sudo iptables -L -v
sudo iptables -L -v
ssh ubuntu@172.21.19.172
ls
scp -i linux_key_pari.pem id_rsa.pub ubuntu@172.31.19.173:~/ 
ssh ubuntu@172.31.19.173
ls
clear
cd ..
ls
mpirun --host ubuntu@172.31.42.40,ubuntu@172.31.19.173 ./hello 
mpirun --host ubuntu@172.31.19.173 ./hello 
ls
cd .ssh
ls
cat id_rsa.pub >> authorized_keys 
cd ..
ls
mpirun --host ubuntu@172.31.42.40,ubuntu@172.31.19.173 ./hello 
ls
python 
sudo apt-get install python-minimal
ls
sudo apt-get install python3
python3
pip install mpi4py
sudo apt-get install python-pip
ls
cd .ssh
ls
cat id_rsa.pub  authorized_keys 
cat id_rsa.pub >>  authorized_keys 
ls
ssh ubuntu@172.31.42.40
ls
sudo pip install mpi4py
sudo apt-get install libopenmpi-dev
sudo pip install mpi4py
ls
exit
ls
s
ls
cat batch20000_17 
ls
sudo apt-get install ksh 
./LoginAllNodes.sh 
ls
mv nodeIPaddressBackup nodeIPaddress
ls
./LoginAllNodes.sh 
nano nodeIPaddress 
./ComputationInstancesLarge.sh 
ssh 18.224.4.151
ls
./ComputationInstancesLarge.sh 
cat hcmm10000_5 
rm hcmm10000_5 
ls
cat load20000_17 
ls
mv load20000_17 hcmm20000_17
cat batch20000_17 
cat batchOverhead20000_17 
mv batchOverhead20000_17 
rm batchOverhead20000_17 
cat batchZeroOverhead20000_17 
ls
rm batchLoadOverhead20000_17 
ls
./ComputationInstancesLarge.sh 
cls
cat batch20000_17 
ls
./ComputationInstancesLarge.sh 
ls
git init 
git commit -m 'first' 
git add .
git commit -m 'first' 
git remote add origin https://github.com/herculesPaulWang/AmazonEC2LargeScale.git
git push -u origin master
ls
cat 3batchOverhead1000020 
ls
./LoginAllNodes.sh 
ls
./ComputationInstancesLarge.sh 
ls
cat 3batchTheory1000020 
cat 3batchOverhead1000020 
