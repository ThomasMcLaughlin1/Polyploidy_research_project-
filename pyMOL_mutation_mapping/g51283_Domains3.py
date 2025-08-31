from pymol import cmd
import numpy as np

# Setting structure names
diploid_structure = "g51283_diploids_biallelic_protein"
tetraploid_structure = "g51283_tetraploids_multiallelic"

# Defining Domains
domains = [
    (4, 163, "Toprim", "brown"),
    (187, 245, "DOMII", "orange"),
    (500, 601, "DOMII", "orange"),
    (246, 305, "DOMIII", "blue"),
    (432, 499, "DOMIII", "blue"),
    (306, 421, "DOMIV", "red"),
    (624, 663, "Zinc_Ribbon_Domain", "purple"),
]

# Defining mutations
mutations = [
    (44, "Sele", "Magenta"),
    (49, "Sele", "Magenta"),
    (89, "Sele", "Magenta"),
    (151, "Sele", "Magenta"),
    (496, "Sele", "Magenta"),
]

# Hiding everything initially
cmd.hide("everything", "all")

# Showing the entire protein backbone in default color
cmd.show("cartoon", diploid_structure)
cmd.show("cartoon", tetraploid_structure)
cmd.color("gray80", diploid_structure)  
cmd.color("gray80", tetraploid_structure)

# Mapping and color domains for start, end, domain_name, color indomains
    # Diploid structure
    sel_dip = f"{diploid_structure} and resi {start}-{end}"
    cmd.select(f"{domain_name}_dip", sel_dip)
    cmd.color(color, f"{domain_name}_dip")
    
    #Tetraploid structure  
    sel_tet = f"{tetraploid_structure} and resi {start}-{end}"
    cmd.select(f"{domain_name}_tet", sel_tet)
    cmd.color(color, f"{domain_name}_tet")

# Highlighting mutations as sticks
cmd.set("stick_radius", 0.25)
for resi, dip_color, tet_color in mutations:
    # Diploid mutations
    sel_dip = f"{diploid_structure} and resi {resi}"
    cmd.select(f"mut_dip_{resi}", sel_dip)
    cmd.show("sticks", f"mut_dip_{resi}")
    cmd.color(dip_color, f"mut_dip_{resi}")
    
    # Tetraploid mutations
    sel_tet = f"{tetraploid_structure} and resi {resi}"
    cmd.select(f"mut_tet_{resi}", sel_tet)
    cmd.show("sticks", f"mut_tet_{resi}")
    cmd.color(tet_color, f"mut_tet_{resi}")

#Mn2+ COORDINATION SETUP
def place_mn2(name, residues, color):
    selection = "(" + diploid_structure + " and resi " + "+".join(str(r) for r in residues) + \
                " and name OD1+OD2+OE1+OE2+O)"
    model = cmd.get_model(selection)
    coords = [atom.coord for atom in model.atom]
    if coords:
        avg = np.mean(coords, axis=0)
        cmd.pseudoatom(name, pos=avg.tolist(), elem="MN", name="MN")
        cmd.color(color, name)
        cmd.show("spheres", name)
        for resi in residues:
            atom_sel = f"{diploid_structure} and resi {resi} and name OD1+OD2+OE1+OE2+O"
            cmd.distance(f"dist_{name}_{resi}", name, atom_sel)
    else:
        print(f"No atoms found for {name}")

# Adding both Mn2+ ions
place_mn2("Mn_cation", [12, 131, 133, 397], "tv_orange")
place_mn2("Mn_structural", [350, 395, 520], "tv_blue")

#Highlighting catalytic Tyr346
for structure in [diploid_structure, tetraploid_structure]:
    sel = f"{structure} and resi 346"
    name = f"catTyr_{structure}"
    cmd.select(name, sel)
    cmd.show("sticks", name)
    cmd.color("yellow", name)

# Zooming into Mn2+ region
cmd.zoom("Mn_cation or Mn_structural", buffer=6)
