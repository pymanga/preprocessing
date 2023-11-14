import os


class CreateNewFile:
    def __init__(self, basic_setup_dir, filename, replacements, new_setup_dir):
        self.basic_setup_dir = basic_setup_dir
        self.filename = filename
        self.replacements = replacements
        self.new_setup_dir = new_setup_dir

        self.openFile()
        self.recplacePlaceholder()
        self.writeFile()

    def openFile(self):
        with open(self.basic_setup_dir + '/' + self.filename, 'r') as file:
          self.filedata_original = file.read()

    def recplacePlaceholder(self):
        self.filedata_new = self.filedata_original
        for r in self.replacements:
            # Credits @Jack Aidley: https://stackoverflow.com/a/17141572
            # Read in the file
            self.filedata_new = self.filedata_new.replace(r, str(self.replacements[r]))

    def writeFile(self):
        # Create new setup directory
        if not os.path.exists(self.new_setup_dir):
            os.makedirs(self.new_setup_dir)

        # Write the file out again
        with open(self.new_setup_dir + "/" + self.filename, 'w') as file:
            file.write(self.filedata_new)
        file.close()
