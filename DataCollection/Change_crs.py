from pyproj import Transformer



def ChangeCRS(data,_from,_to):
    if _from != _to:
        transformer = Transformer.from_crs(
        _from,
        _to,
        always_xy=True
        )

            
        min_lon, min_lat = transformer.transform(data[0], data[1])
        max_lon, max_lat = transformer.transform(data[2], data[3])

        study_area_2 = [min_lon, min_lat, max_lon, max_lat]
        return study_area_2
    return data
