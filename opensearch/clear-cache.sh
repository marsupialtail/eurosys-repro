curl -XPOST -u 'opensearch:XXXX' 'https://search-eurosys-benchmark-eujkhfvuftae3xam7qpv4xzl2a.us-west-2.es.amazonaws.com/'$1'/_cache/clear'
bash move-to-cold.sh $1
sleep 2
bash move-to-ultrawarm.sh $1
