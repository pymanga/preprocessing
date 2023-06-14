#!/usr/bin/python
import lxml.builder

E = lxml.builder.ElementMaker()


class Population:
    def __init__(self, module_name):
        self.module_name = module_name

    def getKeywordExample(self):
        keywords = []
        if self.module_name == "Random":
            keywords = {"name": "Avicennia", "species": "Avicennia",
                        "type": "Random", "n_individuals": "10",
                        "n_recruitment_per_step": "1",
                        "x_1": "0", "x_2": "22", "y_1": "0", "y_2": "22"}
        if self.module_name == "GroupFromFile":
            keywords = {}
        return keywords

    def setModule(self, keywords):
        if self.module_name == "Default":
            self.setDefault(keywords)
        if self.module_name == "Random":
            self.setRandom(keywords)
        if self.module_name == "GroupFromFile":
            self.setGroupFromFile(keywords)

    def getModule(self):
        return self.module

    def setDefault(self, keywords):
        pass

    def setRandom(self, keywords):
        self.module = E.group(
            E.name(keywords['name']),
            E.species(keywords['species']),
            E.distribution(
                E.type(keywords['type']),
                E.n_individuals(keywords['n_individuals']),
                E.n_recruitment_per_step(keywords['n_recruitment_per_step']),
                E.domain(
                    E.x_1(keywords['x_1']),
                    E.x_2(keywords['x_2']),
                    E.y_1(keywords['y_1']),
                    E.y_2(keywords['y_2'])
                )
            )
        )

    def setGroupFromFile(self, keywords):
        pass