#!/usr/bin/python
import lxml.builder

E = lxml.builder.ElementMaker()


class Output:
    def __init__(self, module_name):
        self.module_name = module_name

    def getKeywordExample(self):
        keywords = {"type": "OneFile", "output_each_nth_timestep": "1",
                    "output_times": "[5e8]", "allow_previous_output": "True",
                    "output_dir": "Benchmarks/TestOutputs/"}
        return keywords

    def setModule(self, keywords):
        self.module = E.output(
            E.type(keywords['type']),
            E.output_each_nth_timestep(keywords['output_each_nth_timestep']),
            E.output_times(keywords['output_times']),
            E.allow_previous_output(keywords['allow_previous_output']),
            E.output_dir(keywords['output_dir'])
        )

    def getModule(self):
        return self.module

    def setGeometryOutput(self, tags):
        output = self.module
        for i in range(len(tags)):
            output.append(E.geometry_output(tags[i]))
        self.module = output

    def setGrowthOutput(self, tags):
        output = self.module
        for i in range(len(tags)):
            output.append(E.growth_output(tags[i]))
        self.module = output

    def setParameterOutput(self, tags):
        output = self.module
        for i in range(len(tags)):
            output.append(E.parameter_output(tags[i]))
        self.module = output

    def setNetworkOutput(self, tags):
        output = self.module
        for i in range(len(tags)):
            output.append(E.network_output(tags[i]))
        self.module = output

