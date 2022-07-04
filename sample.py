import pandas as pd
import plotly_express as px
import numpy as np
df=pd.read_csv("data.csv")
height=df["Height"].tolist()
weight=df["Weight"].tolist()
fig=px.line(x=height,y=weight)
fig.show()



#y=mx+c


#hit and trial method
m=0.95
c=-93
y=[]
for x in height:
    y_value=m*x+c
    y.append(y_value)

fig=px.scatter(x=height,y=weight)
fig.update_layout(shapes=[dict(type='line',y0=min(y),y1=max(y),x0=min(height),x1=max(height))])
fig.show()


x=350
y=m*x+c
print(f"weight of someone on the basis of height {x} is {y}")






#computation method usign numpy 
heightarr=np.array(height)
weightarr=np.array(weight)

m,c=np.polyfit(heightarr,weightarr,1)

y=[]
for x in height:
    y_value=m*x+c
    y.append(y_value)

fig=px.scatter(x=height,y=weight)
fig.update_layout(shapes=[dict(type='line',y0=min(y),y1=max(y),x0=min(height),x1=max(height))])
fig.show()


x=450
y=m*x+c
print(f"weight of someone on the basis of height using computational method {x} is {y}")
