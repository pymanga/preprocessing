#!/usr/bin/python
import lxml.builder

E = lxml.builder.ElementMaker()


class Aboveground:
    def __init__(self, module_name):
        self.module_name = module_name

    def getKeywordExample(self):
        keywords = []
        if self.module_name == "SimpleAsymmetricZOI":
            keywords = {"type": "SimpleAsymmetricZOI", "x_resolution": "100", "y_resolution": "100",
                        "x_1": "0", "x_2": "22", "y_1": "0", "y_2": "22"}
        return keywords

    def setModule(self, keywords):
        if self.module_name == "Default":
            self.setDefault()
        if self.module_name == "SimpleAsymmetricZOI":
            self.setAZoi(keywords)

    def getModule(self):
        return self.module

    def setDefault(self):
        self.module = E.aboveground(
            E.type('Default'))

    def setAZoi(self, keywords):
        self.module = E.aboveground(
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

