#!/usr/bin/python
import lxml.builder

E = lxml.builder.ElementMaker()


class PlantDynamics:
    def __init__(self, module_name):
        self.module_name = module_name

    def getKeywordExample(self):
        keywords = {"type": "Bettina"}
        return keywords

    def setModule(self, keywords):
        if self.module_name == "SimpleTest":
            self.setDefault()
        if self.module_name == "Bettina":
            self.setBettina(keywords)
        if self.module_name == "Kiwi":
            self.setKiwi(keywords)
        if self.module_name == "BettinaNetwork":
            self.setBettinaNetwork(keywords)

    def getModule(self):
        return self.module

    def setDefault(self):
        self.module = E.type('SimpleTest')

    def setBettina(self, keywords):
        self.module = E.type(keywords['type'])

    def setKiwi(self, keywords):
        pass

    def setBettinaNetwork(self, keywords):
        pass

