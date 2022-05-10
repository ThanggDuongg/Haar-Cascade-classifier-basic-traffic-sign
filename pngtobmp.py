from PIL import Image
import glob
import os

listImg = glob.glob("F:/Projects/SELF_DRIVING_CAR/TrafficSignDetection/DATA-Traffic-Sign/traffic_Data/DATA/22/*.png")

i = 0
for img in listImg:
   img = Image.open(img)
   print(img)
   folder = 'turnleft/'
   file_out = "image" + str(i) +".bmp"
   # file_out = "test1.bmp"
   img.save(folder + file_out)
   i = i + 1