#!/bin/bash

bash clear-cache.sh spark
python3 phrase-search.py spark "Error sending result"

bash clear-cache.sh hdfs
python3 phrase-search.py hdfs "BlockInfo not found in volumeMap."

bash clear-cache.sh hadoop
python3 phrase-search.py hadoop "RECEIVED SIGNAL 15: SIGTERM"

bash clear-cache.sh windows
python3 phrase-search.py windows "Failed to process single phase execution"

bash clear-cache.sh thunderbird
python3 phrase-search.py thunderbird "Doorbell ACK timeout"

bash clear-cache.sh spark
python3 phrase-search.py spark "Error"

bash clear-cache.sh hdfs
python3 phrase-search.py hdfs "Error"

bash clear-cache.sh hadoop
python3 phrase-search.py hadoop "Error"

bash clear-cache.sh windows
python3 phrase-search.py windows "Error"

bash clear-cache.sh thunderbird
python3 phrase-search.py thunderbird "Error"

