import requests as rq
import planetary_computer
from pystac_client import Client
import rasterio
from rasterio.windows import from_bounds

from DataCollection.Change_crs import ChangeCRS


class GetData:
    def __init__(self,study_area,date, input_crs='EPSG:4326'):
        print("provide input crs if it's not EPSG:4326")
        self.study_area=study_area
        self.input_crs=input_crs
        if self.input_crs !='EPSG:4326':self.study_area=ChangeCRS(data=self.study_area,_from=self.input_crs,_to='EPSG:4326')
        self.date=date
        self.static_url = "https://planetarycomputer.microsoft.com/api/stac/v1"


    def Search(self):
        catalog=Client.open(self.static_url,modifier=planetary_computer.sign_inplace)
        search=catalog.search(
            collections=['sentinel-2-l2a'],
            bbox=self.study_area,
            datetime=self.date,
            query={"eo:cloud_cover": {"lt": 10}},
            limit=1,
            max_items=5
        )
        return search.items()
    

    def Read_files(self):
        
        Items=list(self.Search())
        if Items:
            result={}
            red_band_url = Items[0].assets["B04"].href
            nir_band_url = Items[0].assets["B08"].href
            study_area_2=ChangeCRS(data=self.study_area,_from=self.input_crs,_to='EPSG:32630') # pystac and sentinel uses different crs. crs was changed to ensure acurate clipping.
            with rasterio.open(red_band_url) as src:
                window = from_bounds(*study_area_2, transform=src.transform)
                red = src.read(1, window=window)
                crs = src.crs
                transform = src.transform
                result['red']={'data':red,'crs':crs,'transform':transform}

            with rasterio.open(nir_band_url) as src:
                window = from_bounds(*study_area_2, transform=src.transform)
                nir = src.read(1, window=window)
                
                result['nir']={'data':nir,'crs':crs,'transform':transform}

            return result

        else:
            print('No clear images found in this 5-day window')

    def NDVI(self,data):
        red=data['red']['data'].astype("float32")
        nir=data['nir']['data'].astype("float32")

        ndvi=(nir - red) / (nir + red + 1e-6)
        return {'ndvi':ndvi,"crs": data['red']['crs'],"transform": data['red']['transform']}
    





