from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from printer import printer
import argparse
from setting import logo

class MetaData:
    def __init__(self, PathImage):
        self.PathImage = PathImage
        
    def GetEixfData(self):
        try:
            MetaData = {}
            ImageFile = Image.open(self.PathImage)
            info = ImageFile._getexif()
            if info:
                for (tag, value) in info.items():
                    Tags = TAGS.get(tag, tag)
                    MetaData[Tags] = value
                return MetaData
            else:
                printer.error("No exif!")
        except FileNotFoundError:
            printer.error("No such file or directory!")
            exit(0)
class DataAnalysis:
    def __init__(self, image):
        self.data = image
    def GPSinfo(self):
        printer.title("GPS info")
        if "GPSInfo" in self.data:
            latitude = [float(x)/float(y) for x, y in self.data['GPSInfo'][2]]
            LatitudeRef = self.data['GPSInfo'][1]
            longitude = [float(x)/float(y) for x, y in self.data['GPSInfo'][4]]
            LongitudeRef = self.data['GPSInfo'][3]
            latitude = latitude[0]+latitude[1]/60+latitude[2]/3600
            longitude = longitude[0]+longitude[1]/60+longitude[2]/3600
            if LatitudeRef == 'S':
                latitude = -latitude
            if LongitudeRef == 'W':
                longitude = -longitude
            msg = ("Map Latitude/Longitude : {} {}".format(latitude, longitude))
            printer.info(msg)
        else:
            msg = ("Map Latitude/Longitude : unknown")
            printer.error(msg)
    def DateTimeOriginal(self):
        printer.title("Time info")
        if "DateTimeOriginal" in self.data:
            DateTimeNow = datetime.now()
            DateTimeOriginal = self.data['DateTimeOriginal']
            DateTimeOriginalD = DateTimeOriginal.split(":")
            PictureAgeYear = DateTimeNow.year-int(DateTimeOriginalD[0])
            msg = ("Date time original : {}".format(DateTimeOriginal))
            printer.info(msg)
            msg = (
                    "Picture age : {} years".format(
                        PictureAgeYear
                        )
                    )
            printer.info(msg)
        else:
            msg = ("Date time original : unknown")
            printer.error("Picture age : unknown")
    def DateTimeDigitized(self):
        if "DateTimeDigitized" in self.data:
            msg = (
                "Data time digitized : {}".format(
                    self.data['DateTimeDigitized']
                    )
                )
            printer.info(msg)
        else:
            printer.error("[-] Date time digitized : unknown")
    def ImageDescription(self):
        printer.title("Sys info")
        if "ImageDescription" in self.data:
            msg = (
                "Image description : {}".format(
                    self.data['ImageDescription']
                    )
                )
            printer.info(msg)
        else:
            msg = ("Image description : unknown")
            printer.error(msg)
    def Make(self):
        if "Make" in self.data:
            msg = (
               "Make : {}".format(
                   self.data['Make']
                   )
               )
            printer.info(msg)
        else:
            msg = ("Make : unknown")
            printer.error
    def Model(self):
        if "Model" in self.data:
            msg = (
                "Model : {}".format(
                    self.data['Model']
                    )
                )
            printer.info(msg)
        else:
            msg = ("Model : unknown")
            printer.error(msg)
    def Software(self):
        if "Software" in self.data:
            msg = (
                "Software : {}".format(
                    self.data['Software']
                    )
                )
            printer.info(msg)
        else:
            msg = ("Software : unknown")
            printer.error(msg)
def Analysis(image):
    Analysis = DataAnalysis(image)
    Analysis.GPSinfo()
    Analysis.DateTimeOriginal()
    Analysis.DateTimeDigitized()
    Analysis.ImageDescription()
    Analysis.Make()
    Analysis.Model()
    Analysis.Software()
def main():
    parser = argparse.ArgumentParser(prog="imginfo.py", add_help=True, usage=("python imginfo.py -i IMAGE"))
    parser.add_argument("-i", dest="image", required=True, help="Photo Path")
    args = parser.parse_args()
    logo()
    if args.image:
        image = MetaData(args.image)        
        image = image.GetEixfData()
        Analysis(image)
if __name__ == '__main__':
    main()
