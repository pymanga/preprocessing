#!/usr/bin/python
import lxml.builder

E = lxml.builder.ElementMaker()


class Mortality:
    def __init__(self, module_name):
        self.module_name = module_name

    def getKeywordExample(self):
        keywords = {"mortality": "NoGrowth"}
        return keywords

    def setModule(self, keywords):
        if self.module_name == "NoGrowth":
            self.setNoGrowth(keywords)
    def getModule(self):
        return self.module

    def setNoGrowth(self, keywords):
        self.module = E.mortality(keywords['mortality'])