#!/usr/bin/python
"""
Example file to construct a complete pyMANGA project file using the default values (keywords) provided for the
respective modules.
"""
import lxml.etree
import lxml.builder

# Import pyMANGA xml constructor classes
from Constructors.Resources.Belowground import Belowground
from Constructors.Resources.Aboveground import Aboveground
from Constructors.PlantDynamics.PlantDynamics import PlantDynamics
from Constructors.PlantDynamics.Mortality import Mortality
from Constructors.Population.Population import Population
from Constructors.TimeLoop.TimeLoop import TimeLoop
from Constructors.Output.Output import Output

"""
Write the below-ground section of the project file.
"""

project_file_name = 'setup.xml'

# Set Below-ground module
bg = Belowground("FixedSalinity")
#keywords = bg.getKeywordExample()  #print(keywords.items())
keywords = {"type": "FixedSalinity", "min_x": "0", "max_x": "23", "salinity": "0.025 0.035"}
bg.setModule(keywords)
bg_module = bg.getModule()

# Set Above-ground module
ag = Aboveground("SimpleAsymmetricZOI")
keywords = ag.getKeywordExample()
print(keywords)
ag.setModule(keywords)
ag_module = ag.getModule()

# Set plant dynamics module
pd = PlantDynamics("Bettina")
keywords = {"type": "Bettina"}
pd.setModule(keywords)
pd_module = pd.getModule()

# Set mortality
mt = Mortality("NoGrowth")
keywords = {"mortality": "NoGrowth"}
mt.setModule(keywords)
mt_module = mt.getModule()

# Set population
pop = Population("Random")
keywords = pop.getKeywordExample()
pop.setModule(keywords)
pop_module = pop.getModule()

# Set time loop
tl = TimeLoop("Simple")
keywords = tl.getKeywordExample()
tl.setModule(keywords)
tl_module = tl.getModule()

# Set output
op = Output("OneFile")
keywords = op.getKeywordExample()
op.setModule(keywords)
op.setGeometryOutput(["h_stem", "r_stem", "r_root"])
op.setGrowthOutput(["salinity"])
op.setParameterOutput(["kf_sap", "lp"])
op.setNetworkOutput(["psi_osmo", "partner"])
op_module = op.getModule()


# Build full xml
E = lxml.builder.ElementMaker()
the_doc = E.MangaProject(
        E.random_seed('354745'),
        E.resources(
            ag_module,
            bg_module,
            ),
        E.plant_dynamics(
            pd_module,
            mt_module
        ),
        E.population(pop_module),
        tl_module,
        op_module,
        E.visualization(E.type("NONE "))
        )

final = lxml.etree.tostring(the_doc, pretty_print=True)


with open(project_file_name, 'wb') as f:
    f.write(final)
