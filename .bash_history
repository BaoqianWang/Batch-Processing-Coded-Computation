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
