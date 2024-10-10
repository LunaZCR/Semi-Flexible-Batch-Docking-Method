{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "470ae273",
   "metadata": {},
   "source": [
    "### Code Functionality Overview\n",
    "This code is designed to separate and display a receptor-ligand complex in PyMOL. It includes functions to:\n",
    "- Extract and visualize the receptor and ligand from a PDB file.\n",
    "- Identify polar contacts and hydrogen bonds between them, aiding in structural analysis.\n",
    "\n",
    "### Important User Reminders\n",
    "1. **Customization Required**: \n",
    "   - Before running the code, please ensure that you replace the ligand residue name and the PDB file name with your specific values. For example, if your ligand has a different residue name than \"UNL\", modify that in the `split_and_display_pdbqt` function.\n",
    "\n",
    "2. **Ensure Correct Directory**: \n",
    "   - The code should be placed in a directory that is consistent with your PyMOL installation. This is crucial for PyMOL to access the necessary files and execute the commands correctly.\n",
    "\n",
    "3. **Running in Jupyter Notebook**:\n",
    "   - To run this code effectively in a Jupyter Notebook, ensure you have PyMOL installed and accessible from within the notebook environment. You might need to use the appropriate `%load_ext pymol` magic command to load PyMOL functionalities."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "523e695a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing the PyMOL command module\n",
    "from pymol import cmd\n",
    "\n",
    "# ## Function: split_and_display_pdbqt\n",
    "# This function separates the receptor and ligand in a PDBQT file and displays them in PyMOL.\n",
    "# - `ligand_resn`: The residue name of the ligand to be separated (default is \"UNL\").\n",
    "def split_and_display_pdbqt(ligand_resn=\"UNL\"):\n",
    "    cmd.create(\"complex_copy\", \"my_complex\")  # Create a copy of the complex with a new model name\n",
    "    cmd.extract(\"Protein\", f\"complex_copy and not resn {ligand_resn}\")  # Extract the receptor\n",
    "    cmd.extract(\"ligand\", f\"complex_copy and resn {ligand_resn}\")  # Extract the ligand\n",
    "    \n",
    "    # Display the receptor and ligand\n",
    "    cmd.show(\"cartoon\", \"Protein\")  # Show the receptor as a cartoon\n",
    "    cmd.show(\"sticks\", \"ligand\")     # Show the ligand as sticks\n",
    "    print(\"Receptor and ligand have been split and displayed.\")\n",
    "\n",
    "    # Adjust the view\n",
    "    cmd.zoom(\"Protein\")\n",
    "    \n",
    "    # Set background color (white)\n",
    "    cmd.bg_color(\"white\")\n",
    "\n",
    "    # Set colors for the receptor and ligand\n",
    "    cmd.color(\"cyan\", \"Protein\")      # Color for the receptor\n",
    "    cmd.color(\"orange\", \"ligand\")      # Color for the ligand\n",
    "\n",
    "# ## Function: find_polar_contacts_and_hbonds\n",
    "# This function finds polar contacts and hydrogen bonds between the ligand and receptor.\n",
    "# - `ligand`: The name of the ligand object (default is \"ligand\").\n",
    "# - `receptor`: The name of the receptor object (default is \"Protein\").\n",
    "def find_polar_contacts_and_hbonds(ligand=\"ligand\", receptor=\"Protein\"):\n",
    "    print(\"Starting to find polar contacts and hydrogen bonds...\")\n",
    "    # Find polar contacts between nitrogen and oxygen\n",
    "    cmd.dist(\"ligand_polar_contacts\", f\"{ligand} and (elem N+O)\", f\"{receptor} and (elem N+O)\", mode=2, cutoff=3.5)\n",
    "    print(\"Polar contacts have been found.\")\n",
    "\n",
    "    # Find hydrogen bonds\n",
    "    cmd.distance(\"hydrogen_bonds\", f\"{ligand} and (elem O)\", f\"{receptor} and (elem N)\", cutoff=3.5, mode=2)\n",
    "    print(\"Hydrogen bonds have been found.\")\n",
    "\n",
    "# ## Load the Complex\n",
    "# Load the PDB file containing the complex. Make sure to replace the file name with your actual file.\n",
    "cmd.load(\"G007992_AA_506-32-1.pdb\", \"my_complex\")  # Use your actual model name\n",
    "\n",
    "# ## Run the Functions\n",
    "# Separate and display the receptor and ligand.\n",
    "split_and_display_pdbqt(\"UNL\")  # Replace \"UNL\" with your actual ligand residue name if necessary\n",
    "\n",
    "# Find polar contacts and hydrogen bonds.\n",
    "find_polar_contacts_and_hbonds()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
