import requests

s = requests.get('http://localhost:9091/transmission/rpc')
payload = {
    'method': 'torrent-add',
    'arguments': {
        'paused': 'false',
        'download-dir': '/Users/osamamahmood/Movies',
        'filename': 'magnet:?xt=urn:btih:CLRTVS4PCUYUJMVO2KJVTUR6HLHJREUG&tr=http://nyaa.tracker.wf:7777/announce&tr=udp://tracker.coppersurfer.tk:6969/announce&tr=udp://tracker.internetwarriors.net:1337/announce&tr=udp://tracker.leechersparadise.org:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://open.stealth.si:80/announce&tr=udp://p4p.arenabg.com:1337/announce&tr=udp://mgtracker.org:6969/announce&tr=udp://tracker.tiny-vps.com:6969/announce&tr=udp://peerfect.org:6969/announce&tr=http://share.camoe.cn:8080/announce&tr=http://t.nyaatracker.com:80/announce&tr=https://open.kickasstracker.com:443/announce'
    }
}
r = requests.post('http://localhost:9091/transmission/rpc',
                  headers=s.headers, json=payload)
print(r)
