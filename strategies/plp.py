import pandas as pd

'''
detect any price level with significant number of orders. when appeoaching such a heavy level.
When approaching such level:
situation 1: recent trend shows strength -> open a early order with trailing in the direction.  


'''
class PLP:


    def __init__(self):
        self.name = 'PLP'
        self.description = 'detect any price level with significant number of orders. when appeoaching such a heavy level.'

    def scanner(self):
        pass

    def parseSingle(self,data):
        symboldata = pd.DataFrame()

    def getPriority(self):
        pass
