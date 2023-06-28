#!/usr/bin/python
import lxml.builder

E = lxml.builder.ElementMaker()


class Belowground:
    def __init__(self, module_name):
        self.module_name = module_name

    def getKeywordExample(self):
        keywords = []
        if self.module_name == "FixedSalinity":
            keywords = {"type": "FixedSalinity", "min_x": "0", "max_x": "23", "salinity": "0.025 0.035"}
        if self.module_name == "SymmetricZOI":
            keywords = {"type": "FixedSalinity", "x_resolution": "66", "y_resolution": "66",
                        "x_1": "0", "x_2": "22", "y_1": "0", "y_2": "22"}
        return keywords

    def setModule(self, keywords):
        if self.module_name == "Default":
            self.setDefault()
        if self.module_name == "FixedSalinity":
            self.setFixedSalinity(keywords)
        if self.module_name == "SymmetricZOI":
            self.setSZoi(keywords)
        if self.module_name == "NetworkFixedSalinity":
            self.setNetworkFixedSalinity(keywords)

    def getModule(self):
        return self.module

    def setDefault(self):
        self.module = E.belowground(
            E.type('Default'))

    def setFixedSalinity(self, keywords):
        self.module = E.belowground(
                        E.type(keywords['type']),
                        E.min_x(keywords['min_x']),
                        E.max_x(keywords['max_x']),
                        E.salinity(keywords['salinity'])
                    )
    def setNetworkFixedSalinity(self, keywords):
        self.module = E.belowground(
                        E.type(keywords['type']),
                        E.f_radius(keywords['f_radius']),
                        E.min_x(keywords['min_x']),
                        E.max_x(keywords['max_x']),
                        E.salinity(keywords['salinity'])
                    )

    def setSZoi(self, keywords):
        self.module = E.belowground(
            E.type(keywords['type']),
            E.x_resolution(keywords['x_resolution']),
            E.y_resolution(keywords['y_resolution']),
            E.domain(
                E.x_1(keywords['x_1']),
                E.x_2(keywords['x_2']),
                E.y_1(keywords['y_1']),
                E.y_2(keywords['y_2'])
            )
        )


