#!/bin/bash

bash clear-cache.sh spark
python3 search.py spark rdd_573 1
bash clear-cache.sh hdfs
python3 search.py hdfs blk_5994635810 1
bash clear-cache.sh hadoop
python3 search.py hadoop blk_1076115144 1
bash clear-cache.sh windows
python3 search.py windows consolehost_31bf3856ad364e35 1
bash clear-cache.sh thunderbird
python3 search.py thunderbird 2005120918 1

bash clear-cache.sh spark
python3 search.py spark rdd_573_3 0
bash clear-cache.sh hdfs
python3 search.py hdfs blk_5994635810173130289 0
bash clear-cache.sh hadoop
python3 search.py hadoop blk_1076115144_2374320 0
bash clear-cache.sh windows
python3 search.py windows consolehost_31bf3856ad364e35_0.0.0.0_none_f454588202a1731f 0
bash clear-cache.sh thunderbird
python3 search.py thunderbird 200512091831 0


bash clear-cache.sh spark
python3 search.py spark 573_3 2
bash clear-cache.sh hdfs
python3 search.py hdfs 5994635810 2
bash clear-cache.sh hadoop
python3 search.py hadoop 1076115144 2
bash clear-cache.sh windows
python3 search.py windows 31bf3856ad364e35 2
bash clear-cache.sh thunderbird
python3 search.py thunderbird 512091831 2


