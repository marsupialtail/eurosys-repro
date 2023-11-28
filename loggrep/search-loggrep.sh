#!/bin/bash

do_query() {
	start=$(($(date +%s%N)/1000000))
	aws s3 sync s3://cluster-dump/example_zip/$1 $1 --only-show-errors
	end=$(($(date +%s%N)/1000000))
	download_duration=$(( end - start ))
	start=$(($(date +%s%N)/1000000))
	./thulr_cmdline $1 $2
	end=$(($(date +%s%N)/1000000))
	search_duration=$(( end - start ))

	# Write the runtime to a file
	echo "Execution time of $1 $2: Download $download_duration seconds Search $search_duration seconds" >> runtime.txt
	rm -r $1
}

do_query Spark ERROR
do_query Hdfs error
do_query Hadoop ERROR
do_query Windows Error
do_query Thunderbird error

do_query Spark rdd_573
do_query Hdfs blk_5994635810
do_query Hadoop blk_1076115144
do_query Windows consolehost_31bf3856ad364e35
do_query Thunderbird 20051209183
# 
do_query Spark rdd_573_3
do_query Hdfs blk_5994635810173130289
do_query Hadoop blk_1076115144_2374320
do_query Windows consolehost_31bf3856ad364e35_0.0.0.0_none_f454588202a1731f
do_query Thunderbird 200512091831

do_query Spark 573_3
do_query Hdfs 5994635810
do_query Hadoop 1076115144
do_query Windows 31bf3856ad364e35
do_query Thunderbird 512091831

