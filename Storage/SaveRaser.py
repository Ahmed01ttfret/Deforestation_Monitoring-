from pathlib import Path
import rasterio as rs
import os
import json

def SaveFile(ndvi, datetime):
    try:
        BASE_DIR = Path(__file__).resolve().parent
        OUTPUT_DIR = BASE_DIR / "WorkingData"
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        data = ndvi['ndvi']
        crs = ndvi['crs']
        transform = ndvi['transform']

        safe_datetime = str(datetime).replace(":", "-").replace("/", "-")

        file_path = OUTPUT_DIR / f"NDVI_{safe_datetime}.tif"

        with rs.open(
            file_path,
            'w',
            driver='GTiff',
            height=data.shape[0],
            width=data.shape[1],
            count=1,
            dtype='float32',
            crs=crs,
            transform=transform,
            nodata=-9999
        ) as dst:
            dst.write(data.astype('float32'), 1)

        SaveToJson(
            _Path=OUTPUT_DIR,
            FileName=f"NDVI_{safe_datetime}.tif",
            DateSaved=safe_datetime
        )

        print('Saved successfully')

    except Exception as e:
        print(f'Failed to save NDVI for {datetime}')
        print(e)


def SaveToJson(_Path, FileName, DateSaved):
    file_path = _Path / "MonitoringData.json"

    if file_path.exists():
        with open(file_path, "r") as f:
            dat = json.load(f)
    else:
        dat = []

    data = {
        'id': len(dat),
        'Path': str(_Path / FileName),
        'FileName': FileName,
        'DateSaved': DateSaved
    }

    dat.append(data)

    with open(file_path, 'w') as f:
        json.dump(dat, f, indent=4)