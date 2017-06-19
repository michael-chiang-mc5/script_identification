import urllib
import subprocess

interface_url = "http://104.131.145.75/"
metadata = interface_url + "ImagePicker/list_ECN_metadata/"
data = urllib.urlopen(metadata)

for line in data: # each line is pk, image_url
    line = line.decode("utf-8").split('\t')
    pk=line[0]
    #print line
    image_url = line[1]
    image_save_path = "/home/ubuntu/script_identification/ECN/data/orig/slab/temp.jpg" # must be absolute path 
    urllib.urlretrieve(image_url, image_save_path)

    # run ECN
    std = subprocess.check_output(['sh', 'mc-runECN.sh'])


    print std    

    break
