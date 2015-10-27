import ImageFinder
import glob

for i in glob.glob("/home/andre/PycharmProjects/ImageFinder/roms/*.smc"):
    print i.split('/')[-1]
    ImageFinder.getImage(i.split('/')[-1], "snes", ".smc")
