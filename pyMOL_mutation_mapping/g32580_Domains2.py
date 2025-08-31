from pymol import cmd
import numpy as np
import re

#keeping only letters, numbers, and underscores
def sanitize_name(name):
    # Replace any non-alphanumeric char with underscore
    return re.sub(r'[^a-zA-Z0-9_]', '_', name)

# Setting structure names
diploid_structure = "g32580_diploids_multiallelic_protein"
tetraploid_structure = "g32580_tetraploids_multiallelic"

# Defining Domains
domains = [
    (1, 233, "APE_like_endonuclease", "Brown"),
    (234, 421, "Tower", "Orange"),
    (422, 538, "Fingers", "Blue"),
    (539, 751, "Palm", "Red"),
    (752, 845, "Thumb", "Green"),
    (846, 1032, "Wrist", "Pink"),
    (1033, 1179, "Thumb", "Green"),
]

# Defining mutations 
mutations = [
    (35, "Cyan", "Magenta"),
    (505, "Cyan", "Magenta"),
    (710, "Cyan", "Magenta"),
    (788, "Cyan", "Magenta"),
    (806, "Cyan", "Magenta"),
    (828, "Cyan", "Magenta"),
    (889, "Cyan", "Magenta"),
    (1010, "Cyan", "Magenta"),
    (1011, "Cyan", "Magenta"),
    (1084, "Cyan", "Magenta"),
]

# Defining binding site residues
mg_binding = [37, 536, 539, 540, 541, 581, 586, 640]
dttp_binding = [500, 503, 511, 581, 582, 583, 584, 585, 688]

# find overlapping residues
overlap = list(set(mg_binding) & set(dttp_binding))
mg_only = list(set(mg_binding) - set(overlap))
dttp_only = list(set(dttp_binding) - set(overlap))

# Hide everything 
cmd.hide("everything", "all")

# Showing and color domains
for start, end, domain_name, color in domains:
    for structure in [diploid_structure, tetraploid_structure]:
        sel = structure + " and resi " + str(start) + "-" + str(end)
        sel_name = domain_name + "_" + structure
        cmd.select(sel_name, sel)
        cmd.show("cartoon", sel_name)
        cmd.color(color, sel_name)

# Showing and color mutations
cmd.set("stick_radius", 0.25)
for resi, dip_color, tet_color in mutations:
    sel_dip = diploid_structure + " and resi " + str(resi)
    sel_dip_name = "mut_dip_" + str(resi)
    cmd.select(sel_dip_name, sel_dip)
    cmd.show("sticks", sel_dip_name)
    cmd.color(dip_color, sel_dip_name)

    sel_tet = tetraploid_structure + " and resi " + str(resi)
    sel_tet_name = "mut_tet_" + str(resi)
    cmd.select(sel_tet_name, sel_tet)
    cmd.show("sticks", sel_tet_name)
    cmd.color(tet_color, sel_tet_name)

# Showing and label binding residues
def highlight_binding_sites(residues, color, label, structure):
    for resi in residues:
        sel_name_raw = label + "_" + structure + "_" + str(resi)
        sel_name = sanitize_name(sel_name_raw)
        sel = structure + " and resi " + str(resi)
        cmd.select(sel_name, sel)
        cmd.show("sticks", sel_name)
        cmd.color(color, sel_name)

# Mg2+ 
for structure in [diploid_structure, tetraploid_structure]:
    highlight_binding_sites(mg_only, "yellow", "Mg2+", structure)

# dTTP 
for structure in [diploid_structure, tetraploid_structure]:
    highlight_binding_sites(dttp_only, "purple", "dTTP", structure)

# Overlapping sites
for structure in [diploid_structure, tetraploid_structure]:
    highlight_binding_sites(overlap, "hotpink", "Mg2+ & dTTP", structure)

# Defining structure and coordinating residues
structure = "g32580_diploids_multiallelic_protein"
residues = [37, 536, 539, 540, 541, 581, 586, 640]

# Creating selection of coordinating oxygen atoms (sidechain + backbone)
oxy_selection = "(" + structure + " and resi " + "+".join(str(r) for r in residues) + \
                " and name OD1+OD2+OE1+OE2+O)"

# Getting atom coordinates
coords = []
model = cmd.get_model(oxy_selection)
for atom in model.atom:
    coords.append(atom.coord)

# Getting the average centroid position
if coords:
    average_pos = np.mean(coords, axis=0)
    print("Estimated Mg2+ position:", average_pos.tolist())

    # Place Mg2+ pseudoatom at that position
    cmd.pseudoatom("mg_site", pos=average_pos.tolist(), elem="MG", name="MG")
    cmd.show("spheres", "mg_site")
    cmd.color("tv_orange", "mg_site")

    # drawing dashed distances to coordinating residues
    for resi in residues:
        sel_res = structure + " and resi " + str(resi) + " and name OD1+OD2+OE1+OE2+O"
        cmd.distance("dist_" + str(resi), "mg_site", sel_res)

else:
    print("No coordinating atoms found")

# Zoom on everything
cmd.zoom("all")

