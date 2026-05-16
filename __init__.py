'''

This is a small program designed to monitor deforestation within a small rectangular area using NDVI difference analysis.

The `GetData` class is used to retrieve Sentinel-2 raster data through the Microsoft Planetary Computer service. The retrieved data can then be stored using the `SaveRaster` function.

All raster files are saved in the `WorkingData` directory along with a JSON database to allow easy accessibility and data management.

The `ProcessData` class is used to compare rasters. Its `detail_compare` method can generate a raster showing the differences between two datasets.

The `Query` class can be used to retrieve stored raster data for comparison and analysis.


'''


# from DataCollection import GetData
# from ProcessData.ProcessData import CompareRaster
# from Storage.ReadJson import Query
# from Storage.SaveRaser import SaveFile



# area = [
#     -1.99801489375355,   # min longitude
#     5.2805918587745,     # min latitude
#     -1.930893600920613,  # max longitude
#     5.336964040041853    # max latitude
# ]
# data=GetData.GetData(study_area=area,date="2021-01-01/2023-12-31")
# read=data.Read_files()
# ndvi=data.NDVI(data=read)
 
# SaveFile(ndvi=ndvi,datetime='2020-01-01/2021-12-31')


# raters=Query().Get_rencent_data()

# pro=CompareRaster(raster_a=raters[0]['Path'],raster_b=raters[1]['Path'],download_path='D:\Programming Projects\Geospacial Monitoring')
# pro.detail_compare()