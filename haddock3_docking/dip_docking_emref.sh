#!/bin/bash

#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=40
#SBATCH --mem=160g
#SBATCH --time=24:00:00
#SBATCH --job-name=g32580_docking
#SBATCH --output=/gpfs01/home/pcytm7/L1RT_HADDOCK3/dip_run2/logs/slurm-%x-%j.out
#SBATCH --error=/gpfs01/home/pcytm7/L1RT_HADDOCK3/dip_run2/logs/slurm-%x-%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=pcytm7@nottingham.ac.uk

# Ensure log directory exists
mkdir -p /gpfs01/home/pcytm7/L1RT_HADDOCK3/dip_run2/logs

# Clean previous results if they exist
rm -rf /gpfs01/home/pcytm7/L1RT_HADDOCK3/dip_run2/results/diploid/

# Move to docking run directory
cd /gpfs01/home/pcytm7/L1RT_HADDOCK3/dip_run2

# Load singularity
module load singularity

# Set environment variables for optimal performance
export OMP_NUM_THREADS=40

# Run HADDOCK3 in local mode
singularity exec haddock3_mpi.sif haddock3 dip_run_emref_fullyflex.toml
