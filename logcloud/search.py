import time
import statistics
from rottnest.internal import search_index_logcloud
import sys

def run_search(index_path, query, num_result=1000, runs=7, wavelet = False):
    times = []
    for i in range(runs):
        start = time.time()
        index_path = index_path if type(index_path) == list else [index_path]
        print(search_index_logcloud(index_path, query, num_result, wavelet_tree = wavelet))
        elapsed = time.time() - start
        times.append(elapsed)

    # Discard the first run and calculate stats
    times = times[2:]
    avg_time = statistics.mean(times)
    std_dev = statistics.stdev(times)
    return avg_time, std_dev

def run_and_report(name, index_path, query, wavelet = False):
    if type(index_path) == str:
        avg_time, std_dev = run_search(f's3://logcloud-experiments/rottnest/{index_path}', query, wavelet = wavelet)
    else:
        avg_time, std_dev = run_search([f's3://logcloud-experiments/rottnest/{path}' for path in index_path], query,  wavelet = wavelet)
    print(f"TIMING INFO {name} - Avg: {avg_time:.4f}, StdDev: {std_dev:.4f}")
    sys.stdout.flush()

# whether or not to use wavelet tree implementation
WAVELET = False

INDEX = "_index" if not WAVELET else "_wavelet_index"
INDEX1 = "_indices" if not WAVELET else "_wavelet_indices"

run_and_report(f"hdfs error", f"hdfs{INDEX}/hdfs", "error", wavelet=WAVELET)
run_and_report(f"hadoop ERROR", f"hadoop{INDEX}/hadoop", "ERROR", wavelet=WAVELET)
if not WAVELET:
    run_and_report(f"windows Failed", f"windows{INDEX}/windows", "Failed", wavelet=WAVELET)
run_and_report(f"thunderbird error", f"thunderbird{INDEX}/thunderbird", "error", wavelet=WAVELET)
run_and_report(f"big_hadoop debug", [f"big_hadoop{INDEX1}/hadoop_{i}" for i in range(5)] , "DEBUG", wavelet=WAVELET)

run_and_report(f"hdfs blk_5994635810173130289", f"hdfs{INDEX}/hdfs", "blk_5994635810173130289", wavelet=WAVELET)
run_and_report(f"hadoop blk_1076115144_2374320", f"hadoop{INDEX}/hadoop", "blk_1076115144_2374320", wavelet=WAVELET)
if not WAVELET:
    run_and_report(f"windows 1.1.7601.22667", f"windows{INDEX}/windows", "1.1.7601.22667", wavelet=WAVELET)
run_and_report(f"thunderbird 200512091831", f"thunderbird{INDEX}/thunderbird", "200512091831", wavelet=WAVELET)
run_and_report(f"big_hadoop debug", [f"big_hadoop{INDEX1}/hadoop_{i}" for i in range(5)] , "21530486088551044", wavelet=WAVELET)

run_and_report(f"hdfs 5994635810", f"hdfs{INDEX}/hdfs", "5994635810", wavelet=WAVELET)
run_and_report(f"hadoop 1076115144", f"hadoop{INDEX}/hadoop", "1076115144", wavelet=WAVELET)
if not WAVELET:
    run_and_report(f"windows 7601.22667", f"windows{INDEX}/windows", "7601.22667", wavelet=WAVELET)
run_and_report(f"thunderbird 512091831", f"thunderbird{INDEX}/thunderbird", "512091831", wavelet=WAVELET)
run_and_report(f"big_hadoop debug", [f"big_hadoop{INDEX1}/hadoop_{i}" for i in range(5)] , "88551044", wavelet=WAVELET)


#Ablation studies for scale
for n in range(1, 6):
    run_and_report(f"big_hadoop debug", [f"big_hadoop{INDEX1}/hadoop_{i}" for i in range(n)] , "DEBUG")
    run_and_report(f"big_hadoop debug", [f"big_hadoop{INDEX1}/hadoop_{i}" for i in range(n)] , "21530486088551044")
    run_and_report(f"big_hadoop debug", [f"big_hadoop{INDEX1}/hadoop_{i}" for i in range(n)] , "88551044")

