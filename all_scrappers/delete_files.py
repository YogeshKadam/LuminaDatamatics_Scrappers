

import os

filelist=os.listdir("D:\\YK Python\\amazon_bestsellers_updated\\amazon_bestsellers\\amazon_bestsellers\\full")

filenames_to_delete=[x for x in filelist if len(x)>15]

filepath="D:\\YK Python\\amazon_bestsellers_updated\\amazon_bestsellers\\amazon_bestsellers\\full\\"
[os.remove(filepath+file) for file in filenames_to_delete]