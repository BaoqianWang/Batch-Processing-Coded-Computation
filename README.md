# Batch-Processing-Coded-Computation
**Author: Baoqian Wang**

Implementation of Batch Processing Coded Computation Used in the paper [BPCC](https://arxiv.org/abs/1912.12559) and Heterogeneous Coded Matrix Multiplication  [HCMM](https://arxiv.org/pdf/1701.05973.pdf)


## Code structure

- `bpcc.py`: runnable main script for Batch Processing Coded Computation scheme.

- `hcmm.py`: runnable main script for Heterogeneous Coded Matrix Multiplication.

- `create_encoded_matrix.py`: create encoded matrix.

- `LT_code.py`: implementation of LT_code for encoding and decoding.

- `computation_configuration.json`: json file that specifies the parameter configurations, in particular, 
    1) `num_iteration`: number of times to run the BPCC and HCMM. As we are using Monte Carlo simulation, more iterations means more accurate result.
     called once at the beginning of each training session
    2) `A_dimension`: dimension of matrix A [m, n], m rows and n columns. 
    3) `A_hat_dimension`: dimension of matrix A hat (encoded A) [m, n], m rows and n columns.
    4) `worker_node_load_index`: load index of encoded matrix A hat for each worker.
    5) `worker_batch_p_value`: number of rows computed by each worker node.
    6) `interval`: when creating the encoded matrix, how many rows are written into file every time.
    7) 'delta': parameter to create code.
    7) 'C': parameter to create code.

### Usage
- First configure the parameters in `computation_configuration.json` file.
- Run `create_encoded_matrix.py` to generate encoded matrix.
- Run `bpcc.py (hcmm.py)` using (num_workers is specifed through parameter `worker_node_load_index`):
    `mpirun -n [num_workers + 1]' bpcc.py (hcmm.py)`


## Paper citation

If you used this environment for your experiments or found it helpful, consider citing the following papers:

BPCC:
<pre>
@article{wang2019batch,
  title={On Batch-Processing Based Coded Computing for Heterogeneous Distributed Computing Systems},
  author={Wang, Baoqian and Xie, Junfei and Lu, Kejie and Wan, Yan and Fu, Shengli},
  journal={arXiv preprint arXiv:1912.12559},
  year={2019}
}
</pre>

HCMM:
<pre>
@article{reisizadeh2019coded,
  title={Coded computation over heterogeneous clusters},
  author={Reisizadeh, Amirhossein and Prakash, Saurav and Pedarsani, Ramtin and Avestimehr, Amir Salman},
  journal={IEEE Transactions on Information Theory},
  volume={65},
  number={7},
  pages={4227--4242},
  year={2019},
  publisher={IEEE}
}
</pre>
