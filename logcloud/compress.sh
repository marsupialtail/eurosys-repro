pip3 install rottnest==1.0.3

rottnest-index --mode batch --dir Hdfs/ --index_interval 1024 --compaction_interval 20480 --index_name hdfs --prefix_bytes 14 --prefix_format "%y%m%d %H%M%S"
rottnest-index --mode batch --dir Spark/ --index_interval 1024 --compaction_interval 20480 --index_name spark --prefix_bytes 18 --prefix_format "%y/%m/%d %T"
rottnest-index --mode batch --dir Thunderbird/ --index_interval 1024 --compaction_interval 20480 --index_name thunderbird --prefix_bytes 24 --prefix_format "- %s %Y.%m.%d"
rottnest-index --mode batch --dir Hadoop/ --index_interval 1024 --compaction_interval 20480 --index_name hadoop --prefix_bytes 24 --prefix_format "%Y-%m-%d %T"
rottnest-index --mode batch --dir Windows/ --index_interval 1024 --compaction_interval 20480 --index_name windows --prefix_bytes 21 --prefix_format "%Y-%m-%d %H"




