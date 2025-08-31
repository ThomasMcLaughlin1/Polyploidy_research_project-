# Polyploidy Research Project

#  Description  
This repository contains a collection of scripts and templates for analysing protein sequences and structures in the context of polyploidy research. Tools include workflows for structure prediction, sequence alignment, docking, mutation mapping, and consensus sequence generation.

# Contents

- [Description](#Description)
- [Features](#features (workflow))
- [Data](#Data)
- [Prerequisites](#Prerequisites)
- [Installation](#installation)
- [Contributing](#contributing)
- [References](#References)

# Features  

- AlphaFold Script Template 
Template for running AlphaFold to predict protein structures.

- MAFFT Alignment Script 
Automates multiple sequence alignments with MAFFT for comparative genomics and phylogenetic analyses.

- HADDOCK3 Docking Script 
Workflow for protein–protein docking simulations using HADDOCK3.

- PyMOL Mutation Mapping Scripts
Maps and visualizes mutations onto 3D protein structures in PyMOL.

- Multiallelic Consensus Sequence Generator 
Creates consensus sequences that account for multiallelic variation using AF values 

# Data 
- Input FASTA files for alignments
- AlphaFold output not included as .pdb files are large
- Haddock3 docked complex files not incuded as also included large .pdb files

# Prerequisites
- AlphaFold (V2.3.1)
- pyMOL (v 3.1.5.1)
- MAFFT (v7.525)
- python ≥ 3.8

# Installation 
git clone https://github.com/ThomasMcLaughlin1/Polyploidy_research_project-.git
cd Polyploidy_research_project-
 
# Contributing 
Contributions are welcome! Please:

Fork the repository

Create a feature branch (git checkout -b feature-name)

Commit changes (git commit -m "Add new feature")

Push to your branch (git push origin feature-name)

Open a Pull Request

# References 
Jumper et al., 2021. Highly accurate protein structure prediction with AlphaFold. Nature.

Katoh & Standley, 2013. MAFFT multiple sequence alignment software version 7. Mol Biol Evol.

van Zundert et al., 2016. The HADDOCK3 Web Server: Integrative Modeling of Biomolecular Complexes. J Mol Biol.

Schrödinger, LLC. The PyMOL Molecular Graphics System.
