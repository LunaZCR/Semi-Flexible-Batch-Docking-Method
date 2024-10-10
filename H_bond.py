# Importing the PyMOL command module
from pymol import cmd

# ## Function: split_and_display_pdbqt
# This function separates the receptor and ligand in a PDBQT file and displays them in PyMOL.
# - `ligand_resn`: The residue name of the ligand to be separated (default is "UNL").
def split_and_display_pdbqt(ligand_resn="UNL"):
    cmd.create("complex_copy", "my_complex")  # Create a copy of the complex with a new model name
    cmd.extract("Protein", f"complex_copy and not resn {ligand_resn}")  # Extract the receptor
    cmd.extract("ligand", f"complex_copy and resn {ligand_resn}")  # Extract the ligand
    
    # Display the receptor and ligand
    cmd.show("cartoon", "Protein")  # Show the receptor as a cartoon
    cmd.show("sticks", "ligand")     # Show the ligand as sticks
    print("Receptor and ligand have been split and displayed.")

    # Adjust the view
    cmd.zoom("Protein")
    
    # Set background color (white)
    cmd.bg_color("white")

    # Set colors for the receptor and ligand
    cmd.color("cyan", "Protein")      # Color for the receptor
    cmd.color("orange", "ligand")      # Color for the ligand

# ## Function: find_polar_contacts_and_hbonds
# This function finds polar contacts and hydrogen bonds between the ligand and receptor.
# - `ligand`: The name of the ligand object (default is "ligand").
# - `receptor`: The name of the receptor object (default is "Protein").
def find_polar_contacts_and_hbonds(ligand="ligand", receptor="Protein"):
    print("Starting to find polar contacts and hydrogen bonds...")
    # Find polar contacts between nitrogen and oxygen
    cmd.dist("ligand_polar_contacts", f"{ligand} and (elem N+O)", f"{receptor} and (elem N+O)", mode=2, cutoff=3.5)
    print("Polar contacts have been found.")

    # Find hydrogen bonds
    cmd.distance("hydrogen_bonds", f"{ligand} and (elem O)", f"{receptor} and (elem N)", cutoff=3.5, mode=2)
    print("Hydrogen bonds have been found.")

# ## Load the Complex
# Load the PDB file containing the complex. Make sure to replace the file name with your actual file.
cmd.load("G007992_AA_506-32-1.pdb", "my_complex")  # Use your actual model name

# ## Run the Functions
# Separate and display the receptor and ligand.
split_and_display_pdbqt("UNL")  # Replace "UNL" with your actual ligand residue name if necessary

# Find polar contacts and hydrogen bonds.
find_polar_contacts_and_hbonds()