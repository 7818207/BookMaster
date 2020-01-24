if __name__ == '__main__':
    
    import strategyHandler
    handler = strategyHandler.StrategyHandler('MTdrNGcwbHJldWpsY2UwOGVnOGd0bDFvNWQ')
    import scannable
    syms = scannable.getSymbols()
    prior = {}

    for s in syms:
        prior[s] = 32

    handler.priorityDict = prior

    handler.updatePriority()


    handler.engine.streamData()
    
    
    

#request one very fastly
import random
arglist = [random.choice(handler.engine.urllist), handler.engine.getHttpClient(), handler.engine.scheduler.getNext(), handler.engine.token,
          handler.engine.ContentDict]
import dataengine as de
de.getSingle(arglist)