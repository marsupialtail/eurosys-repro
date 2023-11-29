# LogCloud Reproduction

## Dataset

LogHub data: https://zenodo.org/records/8196385. Spark, Hdfs, Windows, Hadoop and Thunderbird are used. Unzip the logs into text files under their own directories. 

## OpenSearch

Set up an AWS OpenSearch cluster as described here: https://aws.amazon.com/opensearch-service/ with ultrawarm and cold storage enabled. 

Load the log datasets with opensearch/bulk-load.py

Now you can run the search using opensearch/run.sh. Note that this will migrate indices to clear the ultrawarm cache to keep the comparisons fair.

## LogGrep

For compression, follow the instructions here: https://github.com/THUBear-wjy/LogGrep-zstd. In particular, this script can be used to compress all the logs: https://github.com/THUBear-wjy/LogGrep-zstd/blob/master/compression/quickTest.py.

After the logs are compressed, upload the compressed logs to an S3 bucket.

For search, just run https://github.com/marsupialtail/logcloud-experiments/blob/master/loggrep/search-loggrep.sh with the included binary thulr_cmdline. Modify the S3 bucket path accordingly.

## LogCloud

LogCloud is packaged under the name "rottnest" on pypi. Install the right version of LogCloud accordingly:
~~~
pip3 install rottnest==1.0.1 # Wavelet tree implementation, no early stopping
pip3 install rottnest==1.0.2 # Wavelet tree implementation, early stopping
pip3 install rottnest==1.0.3 # custom FM-index implementation, no early stopping
pip3 install rottnest==1.0.4 # custom FM-index implementation, early stopping
~~~

To compress the logs, use: https://github.com/marsupialtail/logcloud-experiments/blob/master/logcloud/compress.sh. Change the log directories in the script. The upload the output indices to an S3 bucket.

To search the logs, run: https://github.com/marsupialtail/logcloud-experiments/blob/master/logcloud/search-logcloud.sh. Change the S3 bucket path accordingly.
