import strategyHandler
import math
import collections
from tqdm import tqdm

class Scheduler:

    def __init__(self,priorityDict,n_cores):
        self.priorityDict = priorityDict
        self.n_cores = n_cores
        self.updateScheduler(priorityDict)

    def updateScheduler(self,priorityDict):
        self.priorityDict = priorityDict
        priorityDict = {k: v for k, v in sorted(priorityDict.items(), key=lambda item: item[1])}
        self.scheduleList = []

        for s,p in priorityDict.items():
            self.scheduleList.append(s)


        first = True
        for s,p in tqdm(priorityDict.items(),desc='Updating priority dictionary'):
            # if first == True:
            #     no_of_times_to_append = math.floor(32 / p)
            #     append_interval = round(32 / no_of_times_to_append)
            #     for i in range(no_of_times_to_append):
            #         self.scheduleList.insert(i * append_interval, s)
            #     first = False
            no_of_times_to_append = math.floor(len(self.scheduleList)/p)
            append_interval = round(len(self.scheduleList) / no_of_times_to_append)
            for i in range(no_of_times_to_append):
                self.scheduleList.insert(i*append_interval+i,s)



    def getAllSymbols(self,symbols):
        self.scheduleList.append(symbols)

    def getNext(self):
        next = self.scheduleList.pop(-1)
        self.scheduleList.insert(0,next)
        return next