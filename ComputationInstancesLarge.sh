#!/usr/bin/ksh
ARRAY=()
while read LINE
do
    ARRAY+=("$LINE")
done < nodeIPaddress

sleep 1
echo "start HCMM..."###########################################################################

# python3 create_encoded_matrix_direct.py --create --scenario hcmm
#
# echo "HCMM worker load creation done"
#
# ./transfer_worker_load.sh
#
# echo "HCMM worker load transfer done"

# mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},\
# ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},\
# ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]} python3 hcmm.py --scenario hcmm >> hcmm_50k_0811_large_2

sleep 1
echo "start Uncoded..." ###########################################################################
#
# python3 create_encoded_matrix_direct.py --scenario uncoded
#
# echo "Uncoded worker load creation done"
#
# ./transfer_worker_load.sh
#
# echo "Uncoded worker load transfer done"


mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},\
ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},\
ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]} python3 hcmm.py --scenario uncoded >> uncoded_50k_0811_large_2

sleep 1
echo "start LoadBalanced..." ###########################################################################

# python3 create_encoded_matrix_direct.py  --scenario load_balanced
#
# echo "LoadBalanced worker load creation done"
#
#
# ./transfer_worker_load.sh
#
# echo "LoadBalanced worker load transfer done"

# mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},\
# ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},\
# ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]} python3 hcmm.py --scenario load_balanced >> load_balanced_50k_0811_large_2

sleep 1
echo "start BPCC-1..." ###########################################################################
#
# python3 create_encoded_matrix_direct.py  --scenario batch_theory
# ./transfer_worker_load.sh
#
# echo "BPCC-1 worker load creation done"

mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},\
ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},\
ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]} python3 bpcc.py --scenario batch_theory >> bpcc_theory_50k_0811_large_2

echo "BPCC-1 worker load transfer done"

sleep 1
echo "start BPCC-2..." ###########################################################################

# python3 create_encoded_matrix_direct.py  --scenario batch_overhead
#
# echo "BPCC-2 worker load creation done"
#
# ./transfer_worker_load.sh
#
# echo "BPCC-2 worker load transfer done"

# mpirun --mca plm_rsh_no_tree_spawn 1 --mca btl_base_warn_component_unused 0  --host ubuntu@${ARRAY[1]},ubuntu@${ARRAY[2]},ubuntu@${ARRAY[3]},\
# ubuntu@${ARRAY[4]},ubuntu@${ARRAY[5]},ubuntu@${ARRAY[6]},ubuntu@${ARRAY[7]},ubuntu@${ARRAY[8]},ubuntu@${ARRAY[9]},\
# ubuntu@${ARRAY[10]},ubuntu@${ARRAY[11]} python3 bpcc.py --scenario batch_overhead >> bpcc_overhead_50k_0811_large_2
