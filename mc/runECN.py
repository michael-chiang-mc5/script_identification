import urllib
import subprocess
import requests, json

interface_url = "http://104.131.145.75/"
metadata = interface_url + "ImagePicker/list_ECN_metadata/"
data = urllib.urlopen(metadata)
file = open("/home/ubuntu/script_identification/ECN/data/orig/test-list.txt","w")

for line in data: # each line is pk, image_url
    line = line.decode("utf-8").split('\t')
    pk=line[0]
    print line
    image_url = line[1]
    image_save_path = "/home/ubuntu/script_identification/ECN/data/orig/slab/" + str(pk) + ".jpg" # must be absolute path 
    urllib.urlretrieve(image_url, image_save_path)
    file.write("slab/" + str(pk) + ".jpg\t1\n") 
file.close() 



# run ECN
std = subprocess.check_output(['sh', 'mc-runECN.sh'])
with open("/home/ubuntu/script_identification/mc/output.txt") as f:
    for line in f:
        std = line.split('\t')
        if len(std)==0:
            std="0\t0\tnone"
        else:
            std = std.split('\t')
        languageID=std[0]
        score=std[1]
        language=std[2]


    # post to interface
    payload = {'boundingBox_pk':pk, 'method':'ECN', 'languageID':languageID, 'score':score, 'notes':''}
    post_url = interface_url + "ImagePicker/postECN/"
    r = requests.post(post_url, data={'json-str':json.dumps(payload)})

