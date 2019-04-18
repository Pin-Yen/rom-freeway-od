"""
These are the id of toll gantries
03F2066N (烏日-快官)
03F2066S (快官-烏日)
03F2078N (中投-烏日)
03F2079S (烏日-中投)
03F2100N (霧峰-中投)
03F2100S (中投-霧峰)
03F2125N (霧峰系統-霧峰)
03F2129S (霧峰-霧峰系統)
03F2152S (霧峰系統-草屯)
03F2153N (草屯-霧峰系統)
// 03F2194N (中興系統-草屯)
// 03F2194S (草屯-中興系統)
03F2231N (中興-中興系統)
03F2235S (中興系統-中興)
03F2260N (南投-中興)
03F2261S (中興-南投)

+ 快官 
|
+ 烏日
|
+ 中投
|
+ 霧峰
|
+ 霧峰系統
|
+ 草屯
|
+ 中興系統
|
+ 中興
|
+ 南投
"""

import sys

# entering at 快官 烏日 中投 霧峰 
sb_taichung_gantry = ['03F2066S', '03F2079S', '03F2100S', '03F2129S']

# exiting at 草屯 中興 南投
sb_nantou_gantry = ['03F2152S', '03F2235S', '03F2261S']

# entering at 南投 中興 草屯
nb_nantou_gantry = ['03F2260N', '03F2231N', '03F2153N']

# exiting at 霧峰 中投 烏日 快官
nb_taichung_gantry = ['03F2125N', '03F2100N', '03F2078N', '03F2066N']

# YYYYMMDD
DATE = '20190416'
if len(sys.argv) > 1:
    DATE = sys.argv[1]
print(DATE)

# {hour}{nb/sb}
traffic_volume = {}

filename_template = 'data/{date}/{hour:02}/TDCS_M08A_{date}_{hour:02}{min:02}00.csv'

for hour in range(6, 24):
    traffic_volume[hour] = {'nb': 0, 'sb': 0}
    for minute in range(0, 60, 5):
        filename = filename_template.format(date=DATE, hour=hour, min=minute)
        with open(filename) as file:
            for line in file:
                # print('line:' + line + 'END')
                try:
                    time, start, end, vtype, volume = line.split(',')
                except ValueError:
                    print('ERROR !', filename, 'may be corrupted')
                    break

                is_pcar = (vtype == '31')
                is_target_nb = (start in nb_nantou_gantry and end in nb_taichung_gantry)
                is_target_sb = (start in sb_taichung_gantry and end in sb_nantou_gantry)
                if is_pcar and is_target_nb:
                    traffic_volume[hour]['nb'] += int(volume)
                elif is_pcar and is_target_sb:
                    traffic_volume[hour]['sb'] += int(volume)

## print result
nb_sum = sum(traffic_volume[h]['nb'] for h in range(6, 24))
sb_sum = sum(traffic_volume[h]['sb'] for h in range(6, 24))
print('SB TOTAL:', nb_sum, ', NB TOTAL:', sb_sum)

print('\n{:>6} {:>9} {:>9} {:>9} {:>9}'\
    .format('HOUR', 'NB-VOLUME', 'NB-FACTOR', 'SB-VOLUME', 'SB-FACTOR'))

for hour in range(6, 24):
    print(' {:02}:00 {:9} {:9.3f} {:9} {:9.3f}'\
        .format(hour\
            , traffic_volume[hour]['nb']\
            , traffic_volume[hour]['nb'] / nb_sum\
            , traffic_volume[hour]['sb']\
            , traffic_volume[hour]['sb'] / sb_sum)) 

