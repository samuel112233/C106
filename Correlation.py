import csv
import plotly.express as px
import numpy as np 

def getDataSource(dataPath):
    iceCream=[]
    temperature=[]
    with open(dataPath) as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
            iceCream.append(float(row['Ice-cream']))
            temperature.append(float(row['Temperature']))
    return {'x':iceCream,'y':temperature}

def findCorrelation(dataSource):
    Correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation',Correlation[0,1])

def setup():
    dataPath='./IceTemp.csv'
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
setup()
