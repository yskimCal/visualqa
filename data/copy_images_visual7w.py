import json
from shutil import copyfile

root_visual7w = "C:\\Users\\Melnita\\Downloads\\visual7w_images\\images"
filered_images_root = "C:\\Users\\Melnita\\Downloads\\visual7w_images"

with open("result.json") as resultJSONfile:
    resultJSON = json.load(resultJSONfile)

filenames = [image["filename"] for image in resultJSON]

for filename in filenames:
    copyfile(root_visual7w + "\\" + filename, filered_images_root + "\\" + filename )

