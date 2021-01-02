import os
from time import sleep
import json
import urllib.request

def getlatesturl(varurl, filename):
    if not os.path.exists('.jsondat'):
            os.mkdir('.jsondat')
    url = varurl
    data = urllib.request.urlopen(url).read().decode()
    obj = json.loads(data)
    os.chdir('.jsondat')
    with open(f'{filename}', 'w') as json_file:
        json.dump(obj['assets_url'], json_file)
    os.chdir(os.path.pardir)
    
    



print('Getting latest GitHub links, please wait...')
getlatesturl('https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest','oc_url')
getlatesturl('https://api.github.com/repos/acidanthera/IntelMausi/releases/latest','mausi_url')
getlatesturl('https://api.github.com/repos/acidanthera/Lilu/releases/latest','lilu_url')
getlatesturl('https://api.github.com/repos/acidanthera/WhateverGreen/releases/latest','weg_url')
getlatesturl('https://api.github.com/repos/acidanthera/VirtualSMC/releases/latest','vsmc_url')
getlatesturl('https://api.github.com/repos/acidanthera/AppleALC/releases/latest','alc_url')
getlatesturl('https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest','itlwm_url')
print('Done!')
sleep(3)
exec(open("main.py").read())
