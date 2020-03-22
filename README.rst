========
geehydro
========


.. image:: https://img.shields.io/pypi/v/geehydro.svg
        :target: https://pypi.python.org/pypi/geehydro

.. image:: https://img.shields.io/conda/vn/conda-forge/geehydro.svg
        :target: https://anaconda.org/conda-forge/geehydro

.. image:: https://img.shields.io/travis/giswqs/geehydro.svg
        :target: https://travis-ci.com/giswqs/geehydro

.. image:: https://readthedocs.org/projects/geehydro/badge/?version=latest
        :target: https://geehydro.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python package for mapping inundation dynamics using Google Earth Engine


* PyPI: https://pypi.python.org/pypi/geehydro
* Conda-forge: https://anaconda.org/conda-forge/geehydro
* Documentation: https://geehydro.readthedocs.io
* Free software: MIT license


Important Note
--------------
This package is no longer being actively maintained. Please use the `geemap <https://github.com/giswqs/geemap>`__ package instead. 


Installation
------------

The **geehydro** Python package is built upon the `folium <https://github.com/python-visualization/folium>`__ package and
implements several methods for interacting with Earth Engine data layers, such as ``Map.addLayer()``, ``Map.setCenter()``, and ``Map.centerObject()``.


To install **geehydro**, run this command in your terminal:

.. code:: python

  pip install geehydro


**geehydro** is also available on `conda-forge <https://anaconda.org/conda-forge/geehydro>`__. If you have Anaconda_ or Miniconda_ installed on your computer, you can create a conda Python environment to install geehydro:

.. code:: python

  conda create -n gee python
  conda activate gee
  conda install -c conda-forge geehydro


If you have installed **geehydro** before and want to upgrade to the latest version, you can run the following command in your terminal:

.. code:: python

  pip install -U geehydro
  

To install the development version from GitHub, run the following command in your terminal:

.. code:: python

  pip install git+https://github.com/giswqs/geehydro
  

.. _Anaconda: https://www.anaconda.com/distribution/#download-section
.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html
