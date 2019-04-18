## 用途
從高速公路旅次資料推估期末報告規劃的中投鐵路各小時旅次應以全天的百分之多少計算。

## 執行方法
### 安裝
電腦需裝python3, 以及requests這個package(pip3 install requests)
### 下載資料

```python3 download-data.py <日期>```<br>
日期格式為YYYYMMDD<br>
例如要下載2019/04/15的資料就執行:<br>
```python3 download-data.py 20190415``` <br>
會將當天的OD資料下載至```data/<YYYYMMDD>/```這個資料夾內
### 執行
``` python3 main.py <日期>``` <br>
即可看到各小時*南投地區->台中地區* & *台中地區->南投地區*的OD量

## 常見障礙
```ERROR ! data/20190412/06/TDCS_M08A_20190412_060000.csv may be corrupted``` <br>
若執行時出現類似以上錯誤訊息，代表該檔案有問題，可以重跑download-data.py或從高公局開放資料網站手動存取資料。<br>

## 其他說明
這個script中各地區所對應的交流道如下
- 南投地區: 草屯交流道, 中興交流道, 南投交流道
- 台中地區: 霧峰交流道, 中投交流道, 大里交流道, 快官交流道

中興系統&霧峰系統由於主要為其他地區來的城際旅次，故不計入。

所有OD都只計入小客車
## 結果
#### 20190412 FRI

```
SB TOTAL: 13360 , NB TOTAL: 13214

  HOUR NB-VOLUME NB-FACTOR SB-VOLUME SB-FACTOR
 06:00       589     0.044       357     0.027
 07:00      1458     0.109      1278     0.097
 08:00       890     0.067      1133     0.086
 09:00       654     0.049       821     0.062
 10:00       613     0.046       629     0.048
 11:00       594     0.044       624     0.047
 12:00       627     0.047       591     0.045
 13:00       674     0.050       610     0.046
 14:00       667     0.050       678     0.051
 15:00       738     0.055       683     0.052
 16:00      1035     0.077       712     0.054
 17:00      1447     0.108      1070     0.081
 18:00      1153     0.086      1009     0.076
 19:00       797     0.060       781     0.059
 20:00       558     0.042       687     0.052
 21:00       434     0.032       664     0.050
 22:00       285     0.021       570     0.043
 23:00       147     0.011       317     0.024
```
#### 20190413 SAT

```
SB TOTAL: 11873 , NB TOTAL: 11904

  HOUR NB-VOLUME NB-FACTOR SB-VOLUME SB-FACTOR
 06:00       364     0.031       290     0.024
 07:00       697     0.059       629     0.053
 08:00       756     0.064       751     0.063
 09:00       711     0.060       813     0.068
 10:00       769     0.065       650     0.055
 11:00       760     0.064       770     0.065
 12:00       782     0.066       669     0.056
 13:00       792     0.067       723     0.061
 14:00       731     0.062       806     0.068
 15:00       855     0.072       822     0.069
 16:00       868     0.073       802     0.067
 17:00       825     0.069       894     0.075
 18:00       711     0.060       662     0.056
 19:00       658     0.055       668     0.056
 20:00       581     0.049       619     0.052
 21:00       493     0.042       610     0.051
 22:00       308     0.026       463     0.039
 23:00       212     0.018       263     0.022
```
#### 20190414 SUN

```
SB TOTAL: 11414 , NB TOTAL: 11162

  HOUR NB-VOLUME NB-FACTOR SB-VOLUME SB-FACTOR
 06:00       229     0.020       196     0.018
 07:00       442     0.039       422     0.038
 08:00       634     0.056       553     0.050
 09:00       629     0.055       630     0.056
 10:00       695     0.061       747     0.067
 11:00       723     0.063       793     0.071
 12:00       640     0.056       609     0.055
 13:00       755     0.066       635     0.057
 14:00       762     0.067       691     0.062
 15:00       863     0.076       800     0.072
 16:00       782     0.069       780     0.070
 17:00       777     0.068       842     0.075
 18:00       818     0.072       713     0.064
 19:00       788     0.069       660     0.059
 20:00       802     0.070       754     0.068
 21:00       576     0.050       687     0.062
 22:00       330     0.029       419     0.038
 23:00       169     0.015       231     0.021
```

#### 20190415 MON
```
SB TOTAL: 12526 , NB TOTAL: 12133

  HOUR NB-VOLUME NB-FACTOR SB-VOLUME SB-FACTOR
 06:00       700     0.056       410     0.034
 07:00      1543     0.123      1367     0.113
 08:00       902     0.072      1146     0.094
 09:00       648     0.052       753     0.062
 10:00       611     0.049       654     0.054
 11:00       559     0.045       575     0.047
 12:00       594     0.047       529     0.044
 13:00       610     0.049       663     0.055
 14:00       630     0.050       631     0.052
 15:00       701     0.056       671     0.055
 16:00       839     0.067       689     0.057
 17:00      1348     0.108      1002     0.083
 18:00       992     0.079       886     0.073
 19:00       629     0.050       578     0.048
 20:00       490     0.039       530     0.044
 21:00       402     0.032       488     0.040
 22:00       213     0.017       386     0.032
 23:00       115     0.009       175     0.014
```

#### 20190416 TUE
```
SB TOTAL: 12238 , NB TOTAL: 11736

  HOUR NB-VOLUME NB-FACTOR SB-VOLUME SB-FACTOR
 06:00       599     0.049       318     0.027
 07:00      1490     0.122      1242     0.106
 08:00       928     0.076      1083     0.092
 09:00       663     0.054       757     0.065
 10:00       535     0.044       648     0.055
 11:00       567     0.046       557     0.047
 12:00       585     0.048       513     0.044
 13:00       635     0.052       527     0.045
 14:00       623     0.051       589     0.050
 15:00       610     0.050       629     0.054
 16:00       832     0.068       629     0.054
 17:00      1363     0.111      1049     0.089
 18:00      1032     0.084       869     0.074
 19:00       597     0.049       698     0.059
 20:00       451     0.037       566     0.048
 21:00       390     0.032       528     0.045
 22:00       217     0.018       360     0.031
 23:00       121     0.010       174     0.015
```

#### 20190417 WED
```
SB TOTAL: 12744 , NB TOTAL: 12182

  HOUR NB-VOLUME NB-FACTOR SB-VOLUME SB-FACTOR
 06:00       640     0.050       347     0.028
 07:00      1470     0.115      1301     0.107
 08:00       898     0.070      1058     0.087
 09:00       657     0.052       740     0.061
 10:00       599     0.047       674     0.055
 11:00       562     0.044       564     0.046
 12:00       643     0.050       527     0.043
 13:00       651     0.051       631     0.052
 14:00       635     0.050       617     0.051
 15:00       695     0.055       624     0.051
 16:00       860     0.067       672     0.055
 17:00      1389     0.109      1033     0.085
 18:00      1077     0.085       910     0.075
 19:00       667     0.052       724     0.059
 20:00       512     0.040       593     0.049
 21:00       397     0.031       518     0.043
 22:00       264     0.021       425     0.035
 23:00       128     0.010       224     0.018
```

## 相關連結
- [電子收費開放資料](http://tisvcloud.freeway.gov.tw/)