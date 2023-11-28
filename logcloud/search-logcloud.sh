#!/bin/bash

do_query() {
	start=$(($(date +%s%N)/1000000))
	OMP_NUM_THREADS=8 rottnest-search --index_path s3://cluster-dump/$1 --query $2 --limit 1000
	end=$(($(date +%s%N)/1000000))
	search_duration=$(( end - start ))

	# Write the runtime to a file
	echo "Execution time of $1 $2: Search $search_duration seconds" >> logcloud_runtime.txt
}

do_query spark ERROR
do_query hdfs error
do_query hadoop ERROR
do_query windows Error
do_query thunderbird error

do_query spark rdd_573
do_query hdfs blk_5994635810
do_query hadoop blk_1076115144
do_query windows consolehost_31bf3856ad364e35
do_query thunderbird 20051209183
# 
do_query spark rdd_573_3
do_query hdfs blk_5994635810173130289
do_query hadoop blk_1076115144_2374320
do_query windows consolehost_31bf3856ad364e35_0.0.0.0_none_f454588202a1731f
do_query thunderbird 200512091831

do_query spark 573_3
do_query hdfs 5994635810
do_query hadoop 1076115144
do_query windows 31bf3856ad364e35
do_query thunderbird 512091831

