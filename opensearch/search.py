from opensearchpy import OpenSearch
import sys

host = 'https://search-eurosys-benchmark-eujkhfvuftae3xam7qpv4xzl2a.us-west-2.es.amazonaws.com'
port = 9200
auth = ('opensearch', 'XXXX') # For testing only. Don't store credentials in code.

# Create the client with SSL/TLS enabled, but hostname verification disabled.
client = OpenSearch(
    # hosts = [{'host': host, 'port': port}],
    hosts = [host],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = auth,
    verify_certs = False,
    timeout=60
)

index_name = sys.argv[1]
# Search for the document.
q = sys.argv[2]
mode = int(sys.argv[3])
if mode == 1:
    print("prefix")
    q = q + "*"
elif mode == 2:
    print("substring")
    q = "*" + q + "*"
query = {
  'size': 1000,
  'query': {
    'wildcard': {
      'log_content': q ,
    }
  }
}
import time
start = time.time()
response = client.search(
    body = query,
    index = index_name
)
took = time.time() - start
# print('\nSearch results:')
# print(response)
print("TIME TAKEN ", took)
