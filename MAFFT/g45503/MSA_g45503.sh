#!/bin/bash

#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem=8g
#SBATCH --time=24:00:00
#SBATCH --job-name=g45503_MSA
#SBATCH --output=/gpfs01/home/pcytm7/MAFFT/logs/slurm-%x-%j.out
#SBATCH --error=/gpfs01/home/pcytm7/MAFFT/logs/slurm-%x-%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=pcytm7@nottingham.ac.uk

#source varibles
source $HOME/.bash_profile

#activate conda env
conda activate MAFFT

mafft --auto /gpfs01/home/pcytm7/MAFFT/g45503/g45503_merged.fasta > g45503_out.fasta

conda deactivate 
