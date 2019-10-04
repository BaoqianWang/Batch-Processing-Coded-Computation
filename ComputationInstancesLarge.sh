#!/usr/bin/ksh
ARRAY=()
while read LINE
do
    ARRAY+=("$LINE")
done < nodeIPaddress
sleep 1
echo "start Batch..."
#mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_batch_pvalue.py 20000 1000 20 100 1824 1824 1824 1824 1824 1824 1617 1617 1617 1617 1617 1617 2527 2527 2527 2527 2527>> batch20000_17
sleep 1
echo "start Batch Overhead..."
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_batch_pvalue_overhead.py 20000 1000 100 1208 1184 1207 1208 1208 1184 1198 1198 1198 1198 1198 1198 1083 1151 1119 1152 1118 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 >> batchOverhead20000_17
sleep 1
echo "start Batch Overhead..."
#mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_batch_pvalue_overhead.py 20000 1000 100 1710 1710 1710 1710 1710 1710 1693 1693 1693 1693 1693 1693 1735 1735 1735 1735 1735 1710 1710 1710 1710 1710 1710 1693 1693 1693 1693 1693 1693 1735 1735 1735 1735 1735 >> batchZeroOverhead20000_17
sleep 1
echo "start Load Batch Overhead..."
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrix_batch_pvalue_overhead.py 20000 1000 100 1316 1316 1316 1316 1316 1316 1167 1167 1167 1167 1167 1167 1823 1823 1823 1823 1823 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2  >> batchLoadOverhead20000_17
sleep 1
echo "start Load..."
mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrixmul_hcmm_continue.py 20000 1000 100 1097 1097 1097 1097 1097 1097 972 972 972 972 972 972 1519 1519 1519 1519 1519 >> load20000_17
sleep 1
echo "start HCMM"
#mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrixmul_hcmm_continue.py 20000 1000 100 1607 1607 1607 1607 1607 1607  1425 1425 1425 1425 1425 1425 2227 2227 2227 2227 2227>> hcmm20000_17
sleep 1
echo "start Uncoded..."
#mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]},ubuntu@${ARRAY[12]},ubuntu@${ARRAY[13]},ubuntu@${ARRAY[14]},ubuntu@${ARRAY[15]},ubuntu@${ARRAY[16]},ubuntu@${ARRAY[17]},ubuntu@${ARRAY[18]} python3 matrixmul_hcmm_continue.py 20000 1000 100 1177 1177 1177 1177 1177 1177 1177 1177 1177 1177 1177 1177 1177 1177 1177 1177 1177 >> uncoded20000_17
sleep 1


