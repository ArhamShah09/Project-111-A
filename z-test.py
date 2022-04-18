import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["Reading time"], show_hist=False)

population_mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("Population mean : ", population_mean, "Standard deviation : ", stdev)

def sampling() :
    dataSet = []
    for i in range(0, 30) :
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)

    sampleMean = statistics.mean(dataSet)
    return sampleMean

meanList = []
for i in range(0, 100) :
    samplingMean = sampling()
    meanList.append(samplingMean)

meanOfSamples = statistics.mean(meanList)
sampleStdev = statistics.stdev(meanList)
print("Mean of samples : ", meanOfSamples, "Standard deviation of samples : " , sampleStdev)

stdev_1_start = meanOfSamples-sampleStdev
stdev_1_end = meanOfSamples+sampleStdev
stdev_2_start = meanOfSamples-(2*sampleStdev)
stdev_2_end = meanOfSamples+(2*sampleStdev)
stdev_3_start = meanOfSamples-(3*sampleStdev)
stdev_3_end = meanOfSamples+(3*sampleStdev)

fig = ff.create_distplot([meanList], ["Sampling"], show_hist=False)
fig.add_trace(go.Scatter(x = [meanOfSamples, meanOfSamples], y = [0, 0.8], mode = "lines", name = "Sample Mean"))
fig.add_trace(go.Scatter(x = [stdev_1_start, stdev_1_start], y = [0, 0.8], mode = "lines", name = "Standard deviation 1st start"))
fig.add_trace(go.Scatter(x = [stdev_1_end, stdev_1_end], y = [0, 0.8], mode = "lines", name = "Standard deviation 1st end"))
fig.add_trace(go.Scatter(x = [stdev_2_start, stdev_2_start], y = [0, 0.8], mode = "lines", name = "Standard deviation 2nd start"))
fig.add_trace(go.Scatter(x = [stdev_2_end, stdev_2_end], y = [0, 0.8], mode = "lines", name = "Standard deviation 2nd end"))
fig.add_trace(go.Scatter(x = [stdev_3_start, stdev_3_start], y = [0, 0.8], mode = "lines", name = "Standard deviation 3rd start"))
fig.add_trace(go.Scatter(x = [stdev_3_end, stdev_3_end], y = [0, 0.8], mode = "lines", name = "Standard deviation 3rd end"))

df1 = pd.read_csv("sample_2.csv")
data1 = df1["reading_time"].tolist()
mean1 = statistics.mean(data1)
print("Mean of intervention 1 : ", mean1)
z1 = (mean1-meanOfSamples)/sampleStdev
fig.add_trace(go.Scatter(x = [mean1, mean1], y = [0, 0.8], mode = "lines", name = "Mean of group 1"))

print("Z test 1 :", z1)

fig.show()
