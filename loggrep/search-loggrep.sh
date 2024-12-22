#!/bin/bash

do_query() {
        start=$(($(date +%s%N)/1000000))
        ./s5cmd sync s3://logcloud-experiments/loggrep_zip/$1/* $1
        end=$(($(date +%s%N)/1000000))
        download_duration=$(( end - start ))
        start=$(($(date +%s%N)/1000000))
        # ./thulr_cmdline $1 $2
	parallel -j1 ./thulr_cmdline $1/split_{}/ $2 ::: {1..8}
        end=$(($(date +%s%N)/1000000))
        search_duration=$(( end - start ))

        # Write the runtime to a file
        echo "Execution time of $1 $2: Download $download_duration seconds Search $search_duration seconds" >> runtime.txt
        rm -r $1
}

for i in `seq 1 5`; do
        do_query Hdfs error
        do_query Hadoop ERROR
        do_query Windows Failed
        do_query Thunderbird error
  	do_query Cluster DEBUG

        do_query Hdfs blk_5994635810173130289
        do_query Hadoop blk_1076115144_2374320
        do_query Windows 1.1.7601.22667
        do_query Thunderbird 200512091831
	do_query Cluster 21530486088551044

        do_query Hdfs 5994635810
        do_query Hadoop 1076115144
        do_query Windows 7601.22667
        do_query Thunderbird 512091831
	do_query Cluster 88551044
done
