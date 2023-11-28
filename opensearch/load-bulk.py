import sys
import json
import time
from opensearchpy import OpenSearch
from opensearchpy import helpers
import os
from subprocess import call
import warnings
from urllib3.exceptions import InsecureRequestWarning
from tqdm import tqdm
# Suppress only the single InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)
host = 'https://search-rottnest-test-7piwkl2szfukp72w4nd4cpmomq.us-west-2.es.amazonaws.com'
port = 9200
auth = ('opensearch', 'XXXX') # For testing only. Don't store credentials in code.
es = OpenSearch(
    hosts = [host],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = auth,
    verify_certs = False
)

files = os.listdir(sys.argv[1])
for f in tqdm(files):
    fo = open(os.path.join(sys.argv[1], f),'r',encoding="ISO-8859-1")
    line = fo.readline()
    start_time = time.time()
    actions = []
    count = 0
    tot = 0
    while line:
        data = {}
        line = line.strip().replace("\'", "")
        data['log_content'] = line
            
        action = {}
        action['_index'] = sys.argv[2]
        action['_type'] = "test"
        action['_source'] = data
        if(count == 10000):
            helpers.bulk(es, actions)
            actions = []
            count = 0
        actions.append(action)
        count += 1
        tot += 1
        line = fo.readline()
        #print(tot)
    helpers.bulk(es, actions)

    fo.close()
end_time = time.time()
time_cost = end_time - start_time
print("time cost: " + str(time_cost))
