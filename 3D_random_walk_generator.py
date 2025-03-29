#%%

import random 
import plotly.graph_objects as go
import matplotlib.pyplot as plt

#generate list of three empty lists
walks = [[i for i in range(0)] for j in range(3)]
x_position, y_position, z_position = 0,0,0 
nstep = 100000

for _ in range(nstep):
    
    x_step = 1 if random.randint(0,1) else -1
    y_step = 1 if random.randint(0,1) else -1
    z_step = 1 if random.randint(0,1) else -1
    
    x_position += x_step
    y_position += y_step
    z_position += z_step
    
    walks[0].append(x_position)
    walks[1].append(y_position)
    walks[2].append(z_position)

fig = go.Figure( data=[go.Scatter3d(x=walks[0], y=walks[1], z=walks[2],
                                    mode='markers', marker=dict(size=6,color='black') )])
fig.show()

