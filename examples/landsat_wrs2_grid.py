'''
<table class="ee-notebook-buttons" align="left"><td>
<a target="_blank"  href="https://colab.research.google.com/github/giswqs/geehydro/blob/master/examples/geehydro-tutorials.ipynb">
    <img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run in Google Colab</a>
</td><td>
<a target="_blank"  href="https://github.com/giswqs/geehydro/tree/master/examples/geehydro-tutorials.ipynb"><img width=32px src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a></td><td>
<a target="_blank"  href="https://nbviewer.jupyter.org/github/giswqs/geehydro/blob/master/examples/geehydro-tutorials.ipynb"><img width=26px src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" />Notebook Viewer</a></td><td>
<a target="_blank"  href="https://mybinder.org/v2/gh/giswqs/geehydro/master?filepath=Folium%2Fee-api-folium-setup.ipynb"><img width=58px src="https://mybinder.org/static/images/logo_social.png" />Run in binder</a></td></table>
'''

# %%
# !pip install geehydro

# %%
import ee
import folium
import geehydro

# %%
ee.Authenticate()
ee.Initialize()

# %%
Map = folium.Map(location=[40, -100], zoom_start=4)
Map.setOptions('HYBRID')

# %%
dataset = ee.FeatureCollection('projects/google/wrs2_descending')
empty = ee.Image().byte()

# %%
Map.setCenter(-78, 36, 8)
Map.addLayer(empty.paint(dataset, 0, 2), {}, 'Landsat WRS-2 grid')
Map.setControlVisibility(layerControl=True, fullscreenControl=True, latLngPopup=True)
Map

# %%
