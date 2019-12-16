import requests

links = open('dl.txt', 'r')
s = requests.get('http://localhost:9091/transmission/rpc')
for x in links:
    payload = {
        'method': 'torrent-add',
        'arguments': {
            'paused': 'false',
            'download-dir': '/Users/osamamahmood/Movies',
            'filename': x
        }
    }
    r = requests.post('http://localhost:9091/transmission/rpc',
                      headers=s.headers, json=payload)
print("Done all links added.")
