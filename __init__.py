'''

This is a small program designed to monitor deforestation within a small rectangular area using NDVI difference analysis.

The `GetData` class is used to retrieve Sentinel-2 raster data through the Microsoft Planetary Computer service. The retrieved data can then be stored using the `SaveRaster` function.

All raster files are saved in the `WorkingData` directory along with a JSON database to allow easy accessibility and data management.

The `ProcessData` class is used to compare rasters. Its `detail_compare` method can generate a raster showing the differences between two datasets.

The `Query` class can be used to retrieve stored raster data for comparison and analysis.


'''