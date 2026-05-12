

from matplotlib import pyplot as plt
import rasterio


class CompareRaster:
    def __init__(self, raster_a, raster_b, download_path):
        self.raster_a = raster_a
        self.raster_b = raster_b
        self.download_path = download_path

        self.result = None
        self.profile = None

    def compare(self):
        with rasterio.open(self.raster_a) as src1:
            raster1 = src1.read(1)
            self.profile = src1.profile

        with rasterio.open(self.raster_b) as src2:
            raster2 = src2.read(1)

        self.result = raster1 - raster2
        return self.result

    def save_result(self):
        if self.result is None:
            self.compare()

        with rasterio.open(self.download_path / "difference.tif", "w", **self.profile) as dst:
            dst.write(self.result, 1)

    def detail_compare(self):
        if self.result is None:
            self.compare()

        raster = self.result

        loss = raster < -0.4
        gain = raster > 0.4

        fig, ax = plt.subplots(figsize=(12,8))

        img = ax.imshow(raster, cmap='RdYlGn')
        plt.colorbar(img, ax=ax)

        ax.contour(loss, colors='blue', linewidths=2)
        ax.contour(gain, colors='black', linewidths=2)

        plt.title("NDVI Change: Blue=loss, Black=gain")
        plt.show()