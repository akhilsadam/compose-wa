# types
from nrclex import NRCLex as nl
import numpy as np
import jpcm

keys = ['fear', 'anger', 'anticip', 'trust', 'surprise', 'positive', 'negative', 'sadness', 'disgust', 'joy', 'anticipation']
cs = [jpcm.maps.kokimurasaki,jpcm.maps.karakurenai,None,jpcm.maps.chigusa_iro,jpcm.maps.shinshu,jpcm.maps.shikon,jpcm.maps.kokushoku,
      jpcm.maps.rurikon,jpcm.maps.omeshi_onando,jpcm.maps.tomorokoshi_iro,jpcm.maps.enji_iro]
n_keys = len(keys)

def nlparse(tx):
    item = nl(text=tx)
    res = item.affect_frequencies
    rkeys = res.keys()
    effect = np.zeros(n_keys)
    for j in range(n_keys):
        key = keys[j]
        if key in rkeys:
            effect[j] = res[key]
    return effect

   
