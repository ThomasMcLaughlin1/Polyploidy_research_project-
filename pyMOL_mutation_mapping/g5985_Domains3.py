from pymol import cmd

# Setting structure names
diploid_structure = "g5985_diploids_biallelic_protein"
tetraploid_structure = "g5985_tetraploids_multiallelic_protein"

# Defining Domains (start, end, name, color)
domains = [
    (24, 141, "TM_Domain", "Brown"),
    (141, 238, "A_Domain", "Orange"),
    (239, 332, "TM_Domain", "Brown"),
    (350, 497, "N_Domain", "Red"),
    (309, 637, "P_Domain", "Green"),
    (646, 836, "TM_Domain", "Brown"),
]

# Defining mutations (resi, dip_color, tet_color)
mutations = [
    (58, "Cyan", "Magenta"),
    (731, "Cyan", "Magenta"),
]

# Hiding everything initially
cmd.hide("everything", "all")

# Showing the entire protein backbone in default color (gray)
cmd.show("cartoon", diploid_structure)
cmd.show("cartoon", tetraploid_structure)
cmd.color("gray80", diploid_structure) 
cmd.color("gray80", tetraploid_structure)

# Mapping and color domains 
for start, end, domain_name, color in domains:
    # Diploid structure
    sel_dip = f"{diploid_structure} and resi {start}-{end}"
    cmd.select(f"{domain_name}_dip", sel_dip)
    cmd.color(color, f"{domain_name}_dip")

    # Tetraploid structure
    sel_tet = f"{tetraploid_structure} and resi {start}-{end}"
    cmd.select(f"{domain_name}_tet", sel_tet)
    cmd.color(color, f"{domain_name}_tet")

# Defining catalytic residue for labeling
catalytic_resi = 342
cmd.select("cat_res_dip", f"{diploid_structure} and resi {catalytic_resi}")
cmd.select("cat_res_tet", f"{tetraploid_structure} and resi {catalytic_resi}")
cmd.show("sticks", "cat_res_dip or cat_res_tet")
cmd.color("Yellow", "cat_res_dip or cat_res_tet")
cmd.label("cat_res_dip", "'Asp342'")
cmd.label("cat_res_tet", "'Asp342'")

# Highlight mutations as sticks
cmd.set("stick_radius", 0.25)
for resi, dip_color, tet_color in mutations:
    sel_dip = f"{diploid_structure} and resi {resi}"
    cmd.select(f"mut_dip_{resi}", sel_dip)
    cmd.show("sticks", f"mut_dip_{resi}")
    cmd.color(dip_color, f"mut_dip_{resi}")

    sel_tet = f"{tetraploid_structure} and resi {resi}"
    cmd.select(f"mut_tet_{resi}", sel_tet)
    cmd.show("sticks", f"mut_tet_{resi}")
    cmd.color(tet_color, f"mut_tet_{resi}")

#Mg2+ pseudoatom with coordination line

def add_mg2_pseudoatom_and_distances(model_prefix, model_name):
    def get_first_atom_coords(selection):
        model = cmd.get_model(selection)
        if len(model.atom) == 0:
            raise ValueError(f"No atoms found for selection: {selection}")
        return model.atom[0].coord

    # Getting coordinates of CA atoms for residues 600 and 607
    coord1 = get_first_atom_coords(f"{model_name} and resi 600 and name CA")
    coord2 = get_first_atom_coords(f"{model_name} and resi 607 and name CA")
    midpoint = [(a + b) / 2 for a, b in zip(coord1, coord2)]

    # Creating Mg2+ pseudoatom at midpoint
    pseudo_name = f"Mg2_{model_prefix}"
    cmd.pseudoatom(object=pseudo_name, pos=midpoint, color="green", label="Mg2+")
    cmd.show("spheres", pseudo_name)
    cmd.set("sphere_scale", 0.5, pseudo_name)

    # Drawing dashed from Mg2+ pseudoatom to coordinating oxygens
    coord_atoms = [
        f"{model_name} and resi 600 and name OD1",
        f"{model_name} and resi 600 and name OD2",
        f"{model_name} and resi 607 and name OD1",
        f"{model_name} and resi 607 and name OD2",
    ]

    for i, coord_atom_sel in enumerate(coord_atoms):
        if cmd.count_atoms(coord_atom_sel) > 0:
            dist_name = f"Mg2_dist_{model_prefix}_{i+1}"
            cmd.distance(dist_name, pseudo_name, coord_atom_sel)
            cmd.set("dash_color", "green", dist_name)
            cmd.set("dash_width", 2.0, dist_name)

# Adding for diploid and tetraploid structures
add_mg2_pseudoatom_and_distances("dip", diploid_structure)
add_mg2_pseudoatom_and_distances("tet", tetraploid_structure)

# Create a selection combining catalytic residue and Mg2+ pseudoatoms
cmd.select("active_site", f"resi {catalytic_resi} and ({diploid_structure} or {tetraploid_structure}) or Mg2_dip or Mg2_tet")

# Zooming tightly on the active site selection
cmd.zoom("active_site", buffer=8)


