from CustomMapReduce.InputData import InputData

class PathInputData(InputData):

    def __init__(self, path):
        super().__init__()
        self.path = path


    def read(self):
        return open(self.path).read()