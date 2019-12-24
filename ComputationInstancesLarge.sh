#!/usr/bin/ksh
ARRAY=()
while read LINE
do
    ARRAY+=("$LINE")
done < nodeIPaddress
sleep 1
echo "start Batch Overhead..."
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_batch_pvalue_overhead.py 10000 200000 50 1201 1201 1201 1201 1201 1201 384 384 384 384 384 384 1324 1324 1324 1324 1324 4 4 4 4 4 4 2 2 2 2 2 2 5 5 5 5 5 >> 13batchOverhead1000020
sleep 1
echo "start Batch..."
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_batch_pvalue.py 10000 200000 20 50 1221 1221 1221 1221 1221 1221 478 478 478 478 478 478 1291 1291 1291 1291 1291 >> 13batchTheory1000020
sleep 1
echo "start Load..."
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_hcmm.py 10000 200000 50 734 734 734 734 734 734 287 287 287 287 287 287 776 776 776 776 776 >> 13load10000
sleep 1
echo "start HCMM"
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_hcmm.py 10000 200000 50 1076 1076 1076 1076 1076 1076 421 421 421 421 421  421  1138 1138 1138 1138 1138 >> 13hcmm10000
sleep 1
echo "start Uncoded..."
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_hcmm.py 10000 200000 50 589 589 589 589 589 589 589 589 589 589 589 589 589 589 589 589 589  >> 13uncoded10000
sleep 1

