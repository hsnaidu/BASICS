import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector
import numpy as np

# Function to handle polygon selection
values = []
def onselect(verts):
    print("Selected Polygon Vertices:", np.round(verts, 1))
    values.append(verts)
    
    return values

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_title("Draw a shape and close the window")

# Create the polygon selector
selector = PolygonSelector(ax, onselect)

plt.show()

