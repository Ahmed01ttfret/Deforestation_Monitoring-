# Deforestation Monitoring Using NDVI Difference

This is a small Python project for monitoring deforestation using NDVI difference analysis on a small rectangular area.

The project retrieves Sentinel-2 raster data from the Microsoft Planetary Computer, stores the raster locally, and compares datasets to detect vegetation changes over time.

## Features

- Retrieve Sentinel-2 raster data
- Store raster datasets locally
- Save raster metadata in a JSON database
- Compare rasters using NDVI difference
- Generate comparison rasters for analysis

## Main Classes

### `GetData`
Used to retrieve Sentinel-2 raster data and save it locally.

### `ProcessData`
Used to compare rasters.  
The `detail_compare` method generates a raster showing the differences between two datasets.

### `Query`
Used to retrieve stored raster data for comparison and analysis.

## Storage

Raster files and metadata are stored inside the `WorkingData` directory.

## Requirements

```bash
pip install rasterio matplotlib scipy pystac-client planetary-computer
```

## Purpose

This project was created as a simple environmental monitoring tool for detecting vegetation changes and possible deforestation over time.
