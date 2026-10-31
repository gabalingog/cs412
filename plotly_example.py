import math
import plotly
import plotly.graph_objs as go

x = [x/10 for x in range(100)]
y = [math.sin(c) for c in x]

fig = go.Scatter(x=x, y=y)
plotly.offline.plot({"data":[fig]})