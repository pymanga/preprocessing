"""
Example file to sequentially change a value in the pyMANGA project file with a simple loop.
"""
from Constructors.CreateXML import CreateXML

# CreateXML(project_file_name="setup.xml")

for sal in list(range(0, 100, 15)):
    CreateXML(project_file_name='se_' + str(sal) + ".xml",
              bg_keywords={'type': 'FixedSalinity', 'min_x': '0', 'max_x': '22', 'salinity': str(sal / 1000) + ' ' +
                                                                                             str(sal / 1000)},
              ag_keywords=False,
              pd_keywords=False,
              mt_keywords=False,
              pop_keywords=False,
              tl_keywords=False,
              op_keywords=False,
              geom_tags=False,
              grow_tags=False,
              param_tags=False,
              netw_tags=False)
