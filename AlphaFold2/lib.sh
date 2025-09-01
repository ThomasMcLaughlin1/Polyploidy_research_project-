## This is lab code 

# common routines for alphafold job

mkdir -p $SCRATCHDIR/tmp  # tmp directory, some jobs need >1GB

HOSTNAME=`hostname`
if [[ $HOSTNAME =~ adan.* ]]; then
    STORAGE=/storage/vestec1-elixir/projects
else
    STORAGE=/storage/brno11-elixir/projects
fi

LIST_FILES=`find $FASTA_INPUTS -maxdepth 1 -type f -exec echo '"{}"' \; | tr '\n' ',' | sed -e "s/,$//"`

export TMPDIR=/scratch
export TF_FORCE_UNIFIED_MEMORY=1
export XLA_PYTHON_CLIENT_MEM_FRACTION=10.0

#monomer reduced
function AF_MONOMER_REDUCED_DBS {
  singularity exec --nv -B $STORAGE/alphafold/alphafold.db-2.3.1/:/alphafold.db --pwd /app/alphafold -B $SCRATCHDIR:/scratch -B /$SCRATCHDIR/tmp:/tmp \
    /storage/brno11-elixir/projects/alphafold/AF2.3.2.sif  \
      python /app/alphafold/run_alphafold.py \
        --fasta_paths=$LIST_FILES \
        --output_dir=/scratch \
        --data_dir=/alphafold.db \
        --uniref90_database_path=/alphafold.db/uniref90/uniref90.fasta \
        --mgnify_database_path=/alphafold.db/mgnify/mgy_clusters_2022_05.fa \
        --template_mmcif_dir=/alphafold.db/pdb_mmcif/mmcif_files \
        --max_template_date=2020-05-14 \
        --obsolete_pdbs_path=/alphafold.db/pdb_mmcif/obsolete.dat \
        --use_gpu_relax \
        --model_preset=monomer \
        --db_preset=reduced_dbs \
        --small_bfd_database_path=/alphafold.db/small_bfd/bfd-first_non_consensus_sequences.fasta \
        --pdb70_database_path=/alphafold.db/pdb70/pdb70 
}

#monomer full
function AF_MONOMER_FULL_DBS {
  singularity exec --nv -B $STORAGE/alphafold/alphafold.db-2.3.1/:/alphafold.db --pwd /app/alphafold -B $SCRATCHDIR:/scratch -B /$SCRATCHDIR/tmp:/tmp \
    /storage/brno11-elixir/projects/alphafold/AF2.3.2.sif  \
      python /app/alphafold/run_alphafold.py \
        --fasta_paths=$LIST_FILES \
        --output_dir=/scratch \
        --data_dir=/alphafold.db \
        --uniref90_database_path=/alphafold.db/uniref90/uniref90.fasta \
        --mgnify_database_path=/alphafold.db/mgnify/mgy_clusters_2022_05.fa \
        --template_mmcif_dir=/alphafold.db/pdb_mmcif/mmcif_files \
        --max_template_date=2020-05-14 \
        --obsolete_pdbs_path=/alphafold.db/pdb_mmcif/obsolete.dat \
        --use_gpu_relax \
        --model_preset=monomer \
        --db_preset=full_dbs \
        --bfd_database_path=/alphafold.db/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
        --uniref30_database_path=/alphafold.db/uniref30/UniRef30_2021_03 \
        --pdb70_database_path=/alphafold.db/pdb70/pdb70
}

#multimer full
function AF_MULTIMER_FULL_DBS {
  singularity exec --nv -B $STORAGE/alphafold/alphafold.db-2.3.1/:/alphafold.db --pwd /app/alphafold -B $SCRATCHDIR:/scratch -B /$SCRATCHDIR/tmp:/tmp \
    /storage/brno11-elixir/projects/alphafold/AF2.3.2.sif  \
      python /app/alphafold/run_alphafold.py \
        --fasta_paths=$LIST_FILES \
        --output_dir=/scratch \
        --data_dir=/alphafold.db \
        --uniref90_database_path=/alphafold.db/uniref90/uniref90.fasta \
        --mgnify_database_path=/alphafold.db/mgnify/mgy_clusters_2022_05.fa \
        --template_mmcif_dir=/alphafold.db/pdb_mmcif/mmcif_files \
        --max_template_date=2020-05-14 \
        --obsolete_pdbs_path=/alphafold.db/pdb_mmcif/obsolete.dat \
        --use_gpu_relax \
        --model_preset=multimer \
        --db_preset=full_dbs \
        --bfd_database_path=/alphafold.db/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
        --uniref30_database_path=/alphafold.db/uniref30/UniRef30_2021_03 \
        --pdb_seqres_database_path=/alphafold.db/pdb_seqres/pdb_seqres.txt \
        --uniprot_database_path=/alphafold.db/uniprot/uniprot.fasta
}
#multimer reduced
function AF_MULTIMER_REDUCED_DBS {
  singularity exec --nv -B $STORAGE/alphafold/alphafold.db-2.3.1/:/alphafold.db --pwd /app/alphafold -B $SCRATCHDIR:/scratch -B /$SCRATCHDIR/tmp:/tmp \
    /storage/brno11-elixir/projects/alphafold/AF2.3.2.sif  \
      python /app/alphafold/run_alphafold.py \
        --fasta_paths=$LIST_FILES \
        --output_dir=/scratch \
        --data_dir=/alphafold.db \
        --uniref90_database_path=/alphafold.db/uniref90/uniref90.fasta \
        --mgnify_database_path=/alphafold.db/mgnify/mgy_clusters_2022_05.fa \
        --template_mmcif_dir=/alphafold.db/pdb_mmcif/mmcif_files \
        --max_template_date=2020-05-14 \
        --obsolete_pdbs_path=/alphafold.db/pdb_mmcif/obsolete.dat \
        --use_gpu_relax \
        --model_preset=multimer \
        --db_preset=reduced_dbs \
        --small_bfd_database_path=/alphafold.db/small_bfd/bfd-first_non_consensus_sequences.fasta \
        --pdb_seqres_database_path=/alphafold.db/pdb_seqres/pdb_seqres.txt \
        --uniprot_database_path=/alphafold.db/uniprot/uniprot.fasta
}





