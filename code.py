import statistics
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
stddeviation = statistics.stdev(data)

first_std_deviation_start, first_std_deviation_end = mean - stddeviation, mean + stddeviation
second_std_deviation_start, second_std_deviation_end = mean - (2 * stddeviation), mean + (2 * stddeviation)
third_std_deviation_start, third_std_deviation_end = mean - (3 * stddeviation), mean + (3 * stddeviation)

data_in_one_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
data_in_two_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
data_in_three_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data is in 1 standard deviation".format(len(data_in_one_std_deviation) * 100.0/len(data)))
print("{}% of data is in 2 standard deviation".format(len(data_in_two_std_deviation) * 100.0/len(data)))
print("{}% of data is in 3 standard deviation".format(len(data_in_three_std_deviation) * 100/len(data)))

fig = ff.create_distplot([data], ["Reading Score"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.50], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.50], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.50], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.50], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.50], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.50], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.50], mode="lines", name="Mean"))
fig.show()