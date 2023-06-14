#!/usr/bin/python
import lxml.builder

E = lxml.builder.ElementMaker()


class TimeLoop:
    def __init__(self, module_name):
        self.module_name = module_name

    def getKeywordExample(self):
        keywords = []
        if self.module_name == "Simple":
            keywords = {"type": "Simple", "t_start": "0",
                        "t_end": "5e8", "delta_t": "1e6"}
        return keywords

    def setModule(self, keywords):
        if self.module_name == "Simple":
            self.setDefault(keywords)

    def getModule(self):
        return self.module

    def setDefault(self, keywords):
        self.module = E.time_loop(
            E.type(keywords['type']),
            E.t_start(keywords['t_start']),
            E.t_end(keywords['t_end']),
            E.delta_t(keywords['delta_t'])
        )
