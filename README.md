Bus Routes
==========

This project takes the bus route information from Traveline and merges it with Naptan information (e.g. lat/long).

<a href="http://dataunity.github.io/bath-hacked-2014/html/index.html">View the map.</a>

This information is then displayed on a Leaflet.js map.

traveline.py
------------
This python script parses the Traveline xml files and turns them into CSV.

Traveline Data Merge Notebook
-----------------------------
This ipython notebook merges together Traveline data with Naptan data to produce CSV files that can be shown in a map.

index.html
----------
This page displays the bus route info. It loads the CSV data via D3, then uses Leaflet.js to draw the information to a map.
