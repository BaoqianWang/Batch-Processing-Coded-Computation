#!/usr/bin/ksh
ARRAY=()
while read LINE
do
    ARRAY+=("$LINE")
done < nodeIPaddress
sleep 1
echo "start HCMM..."
#mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]} python3 hcmm.py

echo "start BPCC..."
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]} python3 bpcc.py
