import os
from collections import defaultdict
from operator import itemgetter
import json

folder = os.walk('virt')
stat_dict = defaultdict(list)

for root, dirs, files in folder:

    for f in files:
        key = f"1{'0' * (len(str(os.stat(os.path.join(root, f)).st_size)))}"
        ext = f.rsplit('.', maxsplit=1)[-1]

        try:
            stat_dict[key][0] += 1
        except IndexError:
            stat_dict[key].append(1)
            stat_dict[key].append([])

        if ext not in stat_dict[key][1]:
            stat_dict[key][1].append(ext)

stat_dict = dict(sorted(stat_dict.items(), key=itemgetter(0)))

for k, v in stat_dict.items():
    stat_dict[k] = tuple(v)
print(stat_dict)

with open('virt_summary.json', 'w', encoding='utf-8') as f:
    json.dump(stat_dict, f)
