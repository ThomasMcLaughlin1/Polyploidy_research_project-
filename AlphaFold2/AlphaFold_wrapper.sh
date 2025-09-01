## This is Lab code


#PBS -N Alphafold-OOD-JOB
#PBS -q default
#PBS -l select=1:ncpus=8:ngpus=1:mem=300gb:scratch_local=30gb:gpu_cap=compute_75
#PBS -l walltime=24:00:00
#PBS -m ae

cd $PBS_O_WORKDIR

###############################################
#change paths
OUTPUTS_DIR=/storage/praha1/home/brays/AlphaFold/Tom/
# here you can set one file, directory or wildcard for files inside dir, e.g. '/dir/ecto/ry/ will process all files in the path, '/dir/*.fasta' will process all *.fasata files in dir    
FASTA_INPUTS=/storage/praha1/home/brays/AlphaFold/Tom/
###############################################

#choose one of the Alfafold prediction method
METHOD="AF_MONOMER_REDUCED_DBS"
#METHOD="AF_MONOMER_FULL_DBS"
#METHOD="AF_MULTIMER_FULL_DBS"
#METHOD="AF_MULTIMER_REDUCED_DBS"

# load methods
source ./lib.sh

# execute method
$METHOD

# copy results from scratch
mkdir -p $OUTPUTS_DIR
cp -r  $SCRATCHDIR/* $OUTPUTS_DIR/ &&  rm -r $SCRATCHDIR/*
