import glob
import ImageFinderBing

for i in glob.glob("/media/andre/14E733B34DA5E097/MaximusArcade/Emuladores/visualpimbal/Tables/*/*.vpt"):
    print("Baixando: " + i.split('/')[-1]+ "....   "),
    ImageFinderBing.getImage(i.split('/')[-1], "pinbal", ".vpt")

