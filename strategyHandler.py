
import dataengine
import concurrent.futures
import strategies.plp as plp
import pandas as pd

class StrategyHandler:


    def __init__(self,token):
        #self.loadStrategies()
        #self.loadSymbols()

        self.engine = dataengine.DataEngine(token)
        self.generateWeightDict()

        #Upon Initialization Call update Priority
        self.updatePriority()


        #executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        #executor.submit(self.engine.streamData())


    def initStrategies(self):
        self.strateList = []
        Plp = plp.PLP()
        self.strateList.append(Plp)

    def loadSymbos(self):
        self.syms = []
        df = pd.read_csv('Data/nasdaq100vol.csv')
        l = df['Symbol'].tolist()[:-1]
        self.syms.append(l)


    def generateWeightDict(self):
        self.priorityDict = {'AAPL':1,'TWTR':5,'BABA':3,'BYND':1}


    def updatePriority(self):
        self.engine.updatePriority(self.priorityDict)

    def requestGlobal(self):
        return self.engine.getContentDict()