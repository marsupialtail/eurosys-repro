import os
from rottnest.internal import index_files_logcloud, search_index_logcloud


index_files_logcloud([f'thunderbird_parquets/{i}' for i in os.listdir('thunderbird_parquets')], 'log', 'thunderbird', 
        remote = 's3://logcloud-experiments/rottnest/', batch_files =4)
index_files_logcloud([f'hdfs_parquets/{i}' for i in os.listdir('hdfs_parquets')], 'log', 'hdfs', 
        remote = 's3://logcloud-experiments/hdfs/', batch_files =4)
index_files_logcloud([f'windows_parquets/{i}' for i in os.listdir('windows_parquets')], 'log', 'window',
        remote = 's3://logcloud-experiments/windows/', batch_files =4)
index_files_logcloud([f'hadoop_parquets/{i}' for i in os.listdir('hadoop_parquets')], 'log', 'hadoop', 
        remote = 's3://logcloud-experiments/rottnest/hadoop', batch_files=4)
index_files_logcloud([f'cluster_parquets/{i}' for i in os.listdir('big_hadoop_parquets')], 'log', 'hadoop', 
        remote = 's3://logcloud-experiments/rottnest/cluster', batch_files=4)

