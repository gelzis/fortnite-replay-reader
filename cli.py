import sys
import json
from ray import Reader

if len(sys.argv) < 2:
    raise Exception('Need to pass filename path!')

with Reader(sys.argv[1]) as replay:

    jsonOutput = {
        'totalPlayers': replay.team_stats['total_players'],
        'eliminations': [],
    }

    eliminations = []
    for elim in replay.eliminations:
        jsonOutput['eliminations'].append({
            'eliminated': elim.eliminated,
            'eliminator': elim.eliminator,
            'gun_type': elim.gun_type,
            'time': elim.time.strftime('%H:%I:%S'),
            'knocked': elim.knocked,
            'weapon': elim.weapon,
        })

    print(json.dumps(jsonOutput))