from CustomMapReduce.InputData import InputData
from CustomMapReduce.PathInputData import PathInputData
from CustomMapReduce.Worker import Worker
import os
from threading import Thread

class LineCountWorker(Worker):

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir,name))

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0], workers[1:]

    for worker in rest:
        first.reduce(worker)

    return first.result

def mapReduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

print(mapReduce('/home/bharat/Code_Repositories/Python/Python/CustomMapReduce/data'))