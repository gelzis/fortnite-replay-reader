import sys
import json
from ray import Reader

if len(sys.argv) < 2:
    raise Exception('Need to pass filename path!')

with Reader(sys.argv[1]) as replay:
    eliminations = []
    for elim in replay.eliminations:
        eliminations.append({
            'eliminated': elim.eliminated,
            'eliminator': elim.eliminator,
            'gun_type': elim.gun_type,
            'time': elim.time.strftime('%Y-%m-%d %H:%I:%S'),
            'knocked': elim.knocked,
            'weapon': elim.weapon,
        })
    print(json.dumps(eliminations))