#!/usr/bin/python
"""
Example file to construct a complete pyMANGA project file using the default values (keywords) provided for the
respective modules.
"""
import lxml.etree
import lxml.builder

# Import pyMANGA xml constructor classes
from .Resources.Belowground import Belowground
from .Resources.Aboveground import Aboveground
from .PlantDynamics.PlantDynamics import PlantDynamics
from .PlantDynamics.Mortality import Mortality
from .Population.Population import Population
from .TimeLoop.TimeLoop import TimeLoop
from .Output.Output import Output


class CreateXML:
    def __init__(self, project_file_name='setup.xml',
                 bg_keywords=False, ag_keywords=False, pd_keywords=False, mt_keywords=False, pop_keywords=False,
                 tl_keywords=False, op_keywords=False, geom_tags=False, grow_tags=False, param_tags=False,
                 netw_tags=False):
        self.project_file_name = project_file_name
        self.setModules(bg_keywords, ag_keywords, pd_keywords, mt_keywords, pop_keywords,
                        tl_keywords, op_keywords, geom_tags, grow_tags, param_tags, netw_tags)
        self.writeFile()

    def setModules(self, bg_keywords, ag_keywords, pd_keywords, mt_keywords, pop_keywords,
                   tl_keywords, op_keywords, geom_tags, grow_tags, param_tags, netw_tags):
        # Set Below-ground module
        if not bg_keywords:
            bg = Belowground("SimpleTest")
            bg_keywords = bg.getKeywordExample()
        else:
            bg = Belowground(bg_keywords["type"])
        bg.setModule(bg_keywords)
        bg_module = bg.getModule()

        # Set Above-ground module
        if not ag_keywords:
            ag = Aboveground("SimpleTest")
            ag_keywords = ag.getKeywordExample()
        else:
            ag = Aboveground(ag_keywords["type"])
        ag.setModule(ag_keywords)
        ag_module = ag.getModule()

        # Set plant dynamics module
        if not pd_keywords:
            pd = PlantDynamics("SimpleTest")
            pd_keywords = pd.getKeywordExample()
        else:
            pd = PlantDynamics(pd_keywords["type"])
        pd.setModule(pd_keywords)
        pd_module = pd.getModule()

        # Set mortality
        if not mt_keywords:
            mt = Mortality("NoGrowth")
            mt_keywords = mt.getKeywordExample()
        else:
            mt = Mortality(mt_keywords["mortality"])
        mt.setModule(mt_keywords)
        mt_module = mt.getModule()

        # Set population
        if not pop_keywords:
            pop = Population("Random")
            pop_keywords = pop.getKeywordExample()
        else:
            pop = Population(pop_keywords["type"])
        pop.setModule(pop_keywords)
        pop_module = pop.getModule()

        # Set time loop
        tl = TimeLoop("Simple")
        if not tl_keywords:
            tl_keywords = tl.getKeywordExample()
        tl.setModule(tl_keywords)
        tl_module = tl.getModule()

        # Set output
        op = Output("OneFile")
        if not op_keywords:
            op_keywords = op.getKeywordExample()
        op.setModule(op_keywords)
        if geom_tags:
            op.setGeometryOutput(geom_tags)
        if grow_tags:
            op.setGrowthOutput(grow_tags)
        if param_tags:
            op.setParameterOutput(param_tags)
        if netw_tags:
            op.setNetworkOutput(netw_tags)
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

        self.final = lxml.etree.tostring(the_doc, pretty_print=True)

    def writeFile(self):
        with open(self.project_file_name, 'wb') as f:
            f.write(self.final)

