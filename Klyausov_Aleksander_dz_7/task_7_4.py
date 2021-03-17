import os
from operator import itemgetter

folder = os.walk('some_data')
stat_dict = {}

for root, dirs, files in folder:
    for f in files:
        key = f"1{'0' * (len(str(os.stat(os.path.join(root, f)).st_size)))}"
        stat_dict[key] = stat_dict.get(key, 0) + 1

print('{')
stat_dict = dict(sorted(stat_dict.items(), key=itemgetter(0)))
for k, v in stat_dict.items():
    print(f'  {k}: {v},')
print('}')
