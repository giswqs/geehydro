# -*- coding: utf-8 -*-

"""Main module."""

import os
import ee
import folium
from folium import plugins
from add_layer import add_ee_layer
from basemaps import basemaps

ee.Initialize()

if __name__ == '__main__':
    
    dem = ee.Image('USGS/SRTMGL1_003')
    # Set visualization parameters.
    vis_params = {
    'min': 0,
    'max': 4000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

    # Create a folium map object.
    my_map = folium.Map(location=[20, 0], zoom_start=3, height=500)

    # Add custom basemaps
    basemaps['Google Maps'].add_to(my_map)
    basemaps['Google Satellite Hybrid'].add_to(my_map)

    # Add the elevation model to the map object.
    my_map.add_ee_layer(dem.updateMask(dem.gt(0)), vis_params, 'DEM')

    # Add a layer control panel to the map.
    my_map.add_child(folium.LayerControl())

    # Add fullscreen button
    plugins.Fullscreen().add_to(my_map)

    # Display the map.
    # display(my_map)
    my_map
    print("Testing done")
