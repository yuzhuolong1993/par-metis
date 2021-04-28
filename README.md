# par-metis

## Install parmetis and openmpi
Check [Install.txt](Install.txt) to install parmetis

## Download and preprocess dataset
- `python process_input.py papers`
- `python process_input.py products`

## Run parmetis
`parmetis` takes six parameters: 
- `parmetis <graph-file> <op-type> <nparts> <adapth-factor> <ipc2redist> <dbglvl> <seed>`

For example, to partition `paper.graph` into 8 parts with single-process, multi-process, and multi-node:
- Single-process: `parmetis paper.graph 1 8 1 1 6 1`

- Multi-process: `mpirun -n 4 parmetis paper.graph 1 8 1 1 6 1`

- Multi-node: `mpirun --host [ip_1],[ip_2],[ip_3],[ip_4] -np 4 parmetis paper.graph 1 8 1 1 6 1`