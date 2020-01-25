# -*- coding: utf-8 -*-

"""Main module."""

import os
import ee
import folium
from folium import plugins


def addLayer(self, ee_object, vis_params={}, name='Layer untitled', shown=True, opacity=1):

    image = None

    if not isinstance(ee_object, ee.Image) and not isinstance(ee_object, ee.ImageCollection) and not isinstance(ee_object, ee.FeatureCollection) and not isinstance(ee_object, ee.Feature) and not isinstance(ee_object, ee.Geometry):
        err_str = "\n\nThe image argument in 'addLayer' function must be an instace of one of ee.Image, ee.Geometry, ee.Feature or ee.FeatureCollection."
        raise AttributeError(err_str)

    if isinstance(ee_object, ee.geometry.Geometry) or isinstance(ee_object, ee.feature.Feature) or isinstance(ee_object, ee.featurecollection.FeatureCollection):
        features = ee.FeatureCollection(ee_object)

        width = 2

        if 'width' in vis_params:
            width = vis_params['width']

        color = '000000'

        if 'color' in vis_params:
            color = vis_params['color']

        image_fill = features.style(
            **{'fillColor': color}).updateMask(ee.Image.constant(0.5))
        image_outline = features.style(
            **{'color': color, 'fillColor': '00000000', 'width': width})

        image = image_fill.blend(image_outline)
    elif isinstance(ee_object, ee.image.Image):
        image = ee_object
    elif isinstance(ee_object, ee.imagecollection.ImageCollection):    
        image = ee_object.median()
    

    map_id_dict = ee.Image(image).getMapId(vis_params)
    folium.raster_layers.TileLayer(
        tiles = map_id_dict['tile_fetcher'].url_format,
        attr = 'Google Earth Engine',
        name = name,
        overlay = True,
        control = True,
        show=shown,
        opacity=opacity
    ).add_to(self)
    
# Add EE drawing method to folium.
folium.Map.addLayer = addLayer



# Modifies the Google Maps basemap
# A mapTypeId to set the basemap to. Can be one of "ROADMAP", "SATELLITE", "HYBRID" or "TERRAIN" to select one of the standard Google Maps API map types
def setOptions(self, mapTypeId='HYBRID', styles={}, types=[]):
    # Add custom basemaps to folium
    basemaps = {
        'ROADMAP': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Maps',
            overlay = True,
            control = True
        ),
        'SATELLITE': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Satellite',
            overlay = True,
            control = True
        ),
        'TERRAIN': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Terrain',
            overlay = True,
            control = True
        ),
        'HYBRID': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Satellite',
            overlay = True,
            control = True
        ),
        'ESRI': folium.TileLayer(
            tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr = 'Esri',
            name = 'Esri Satellite',
            overlay = True,
            control = True
        )
    }

    try:
        basemaps[mapTypeId].add_to(self)
    except:
        print('Basemap can only be one of "ROADMAP", "SATELLITE", "HYBRID", "TERRAIN", or "ESRI"')

folium.Map.setOptions = setOptions

# show the map
def setControlVisibility(self, layerControl=True, fullscreenControl=True, latLngPopup=True):

    if layerControl:
        folium.LayerControl().add_to(self)
    if fullscreenControl:
        plugins.Fullscreen().add_to(self)
    if latLngPopup:
        folium.LatLngPopup().add_to(self)

folium.Map.setControlVisibility = setControlVisibility


def setCenter(self, lon, lat, zoom=10):
    self.fit_bounds([[lat, lon], [lat, lon]], max_zoom=zoom)
    
folium.Map.setCenter = setCenter


def centerObject(self, ee_object, zoom):
    # try:    

    lat = 0
    lon = 0
    bounds = [[lat, lon], [lat, lon]]
    if isinstance(ee_object, ee.geometry.Geometry):    
        centroid = ee_object.centroid()
        lon, lat = centroid.getInfo()['coordinates']
        bounds = [[lat, lon], [lat, lon]]
    elif isinstance(ee_object, ee.featurecollection.FeatureCollection):    
        centroid = ee_object.geometry().centroid()
        lon, lat = centroid.getInfo()['coordinates']
        bounds = [[lat, lon], [lat, lon]]
    elif isinstance(ee_object, ee.image.Image):  
        geometry = ee_object.geometry()  
        print(geometry.getInfo())
        coordinates = geometry.getInfo()['coordinates'][0]
        bounds = [coordinates[0][::-1], coordinates[2][::-1]]
    elif isinstance(ee_object, ee.imagecollection.ImageCollection):  
        geometry = ee_object.geometry()  
        coordinates = geometry.getInfo()['coordinates'][0]
        bounds = [coordinates[0][::-1], coordinates[2][::-1]] 
    else:
        bounds = [[0, 0], [0, 0]]      

    print(bounds)
    self.fit_bounds(bounds, max_zoom=zoom)

    # except:
    #     print("Failed to centerObject")

folium.Map.centerObject = centerObject



if __name__ == '__main__':

    ee.Initialize()
    
    dem = ee.Image('USGS/SRTMGL1_003')
    # Set visualization parameters.
    vis_params = {
    'min': 0,
    'max': 4000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

    # Create a folium map object.
    Map = folium.Map(location=[20, 0], zoom_start=3, height=500)

    # # Add custom basemaps
    # basemaps['Google Maps'].add_to(my_map)
    # basemaps['Google Satellite Hybrid'].add_to(my_map)

    # Add the elevation model to the map object.
    Map.addLayer(dem.updateMask(dem.gt(0)), vis_params, 'DEM')

    # Add a layer control panel to the map.
    Map.add_child(folium.LayerControl())

    # Add fullscreen button
    plugins.Fullscreen().add_to(Map)

    # Display the map.
    # display(my_map)
    Map
    print("Testing done")
