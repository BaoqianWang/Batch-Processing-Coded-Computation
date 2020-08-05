#!/usr/bin/ksh
filename1='nodeIPaddress'
ARRAY=()
num_nodes=0
while read LINE
do
    ARRAY+=("$LINE")
    ((num_nodes++))
done < $filename1


#Transfer files to worker.
filename2='common_script_files'
while read line; do
  for ((i=1;i<=num_nodes;i++))
  do
      scp -i ~/AmazonEC21224/.ssh/linux_key_pari.pem  $line ubuntu@${ARRAY[i]}:~
      echo "Transfer $i to $line Done "
  done
done < $filename2


#Transfer worker load to each worker
for ((i=1;i<=num_nodes-1;i++))
do
    scp -i ~/AmazonEC21224/.ssh/linux_key_pari.pem  A_worker$i.h5 ubuntu@${ARRAY[i+1]}:~
    echo "Transfer A_worker$i to ${ARRAY[i+1]} Done "
done


# # Transfer files to master.
# filename2='files_for_master_node'
# while read line; do
# scp -i ~/AmazonEC21224/.ssh/linux_key_pari.pem $line  ubuntu@${ARRAY[1]}:~
# echo "Transfer to $line Done "
# done < $filename2


# #Transfer files to worker.
# filename3='files_for_worker_nodes'
# while read line; do
#   for ((i=2;i<=num_nodes;i++))
#   do
#       scp -i ~/AmazonEC21224/.ssh/linux_key_pari.pem  $line ubuntu@${ARRAY[i]}:~
#       echo "Transfer $i to $line Done "
#   done
# done < $filename3
