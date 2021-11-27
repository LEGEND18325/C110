import csv
from numpy.core.fromnumeric import mean
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

file=pd.read_csv('AverageData.csv')
data=file['average'].tolist()

figure=ff.create_distplot([data],['average'],show_hist=False)
figure.show()


list=[]

for i in range(0,100):
    randomIndex= random.randint(0,len(data))
    value= data[randomIndex]
    list.append(value)

meanOfSampleData=statistics.mean(list)
standardDeviationOfSampleData=statistics.stdev(list)

print('mean Of Sample Data '+str(meanOfSampleData))
print('starndard Deviation Of Sample Data '+str(standardDeviationOfSampleData))

def data(counter):
    createList=[]
    for i in range(0,counter):
     randomIndex= random.randint(0,len(data))
     value= data[randomIndex]
     createList.append(value)

    meanOfSampleData=statistics.mean(createList)
    standardDeviationOfSampleData=statistics.stdev(createList)
    return meanOfSampleData,standardDeviationOfSampleData


def showFigure(data2):
    file=data2
    meanOfFile=statistics.mean(file)
    figure=ff.create_distplot([file],['average'],show_hist=False)
    figure.add_trace(go.Scatter(x=[meanOfFile,meanOfFile],y=[0,1],mode='lines',name='Mean'))
    figure.show()



def setup():
    list=[]
    for i in range(0,1000):
        randomData=data(100)
        list.append(randomData)

    showFigure(list)
    mean=statistics.mean(list)
    standard=statistics.stdev(list)

    print('mean Of Sampling Distribution '+str(mean))
    print('starndard Deviation Of Sampling Distribution  '+str(standard))

setup()

 


