"""
This file is an example on how to create pyMANGA project files to run a local sensitivity analysis.

The basis is a folder with all files required for the setups, i.e. a species file and a pyMANGA project file.
In these files all parameters that are going to be changed need to be replaced by placeholders, e.g. "%aa%" to replace
the FON parameter aa.

In this example, all model calls are written to a python file that can be called to run all setups sequentially.
"""

import itertools
import os
from ReplaceInFiles.CreateNewFile import CreateNewFile

# Define path to pyMANGA
path_to_manga = 'path/to/MANGA.py'
absolute_path = os.getcwd()

# Define path to basic setup
basic_setup_dir = "../SimpleExample/FON"

# Define files that will be changed
species_file = "Avicennia.py"
project_file = "FON.xml"

# Create dictionary with parameters
parameter_ref = {"%aa%": [10],
                 "%bb%": [1],
                 "%fmin%": [0.1]}

# Create parameter combinations
pp = [0.5, 1, 1.5]

parameters = {}
for key in parameter_ref:
    parameters[key] = [parameter_ref[key][0] * i for i in pp]

# Iterate through parameter combinations
keys = list(parameters)
runfile_object = open('runmangajobs.py', 'a')

for values in itertools.product(*map(parameters.get, keys)):
    # Extract parameter combination for setup
    setup = dict(zip(keys, values))
    print("setup: ", setup)

    # Create new setup name based on parameter values
    new_setup_name = "FON"
    for k, v in setup.items():
        n = k.replace("%", "") + "_" + str(round(v, 2)).replace(".", "-")
        new_setup_name += "_" + n
    project_file_name = new_setup_name + "/FON.xml"
    new_species_dir = absolute_path + "/" + new_setup_name + "/" + species_file

    # Replace parameters in species file
    CreateNewFile(basic_setup_dir=basic_setup_dir,
                  filename=species_file,
                  replacements=setup,
                  new_setup_dir=new_setup_name)

    # Replace parameters in project file
    CreateNewFile(basic_setup_dir=basic_setup_dir,
                  filename=project_file,
                  replacements={"%output_dir%": new_setup_name,
                                "%species%": new_species_dir},
                  new_setup_dir=new_setup_name)

    # Write setup call to script
    runfile_object.write('os.system("py ' + path_to_manga + ' -i ' + project_file_name + '")\n')

runfile_object.close()
