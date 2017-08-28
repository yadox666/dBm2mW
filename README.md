# dBm2mW

This is a sample and simple script in Python Programming Language 
to convert input values in dBm to its corresponding value in mW or
viceversa.

The input argument is parsed and cleaned to extract the digits,
the decimal comma or point, the negative sign  and the units to 
convert. If no input argumment is passed, usage is shown and a 
table with some values.

The functions ar very usefull to be included in Wi-Fi scripts where
you have to convert RF values in both units. Feel free to use or
include it in your own scripts.

*Yago Hansen*


## Samples:

```
python dBm2mW.py -12.3 dBm
-12.30 dBm = 0.0588843655 mW

python dBm2mW.py 1000mW
1000 mW = 30.00 dBm

python dBm2mW.py 9,23 dBm
9.23 dBm = 8 mW

python dBm2mW.py
Usage: Enter input value as 9.99dBm or 999mW
--------------------
2000 mW = 33.01 dBm
1900 mW = 32.79 dBm
1800 mW = 32.55 dBm
1700 mW = 32.30 dBm
1600 mW = 32.04 dBm
1500 mW = 31.76 dBm
1400 mW = 31.46 dBm
1300 mW = 31.14 dBm
1200 mW = 30.79 dBm
1100 mW = 30.41 dBm
1000 mW = 30.00 dBm
900 mW = 29.54 dBm
800 mW = 29.03 dBm
700 mW = 28.45 dBm
600 mW = 27.78 dBm
500 mW = 26.99 dBm
400 mW = 26.02 dBm
300 mW = 24.77 dBm
200 mW = 23.01 dBm
100 mW = 20.00 dBm
--------------------
10.00 dBm = 10 mW
11.00 dBm = 12 mW
12.00 dBm = 15 mW
13.00 dBm = 19 mW
14.00 dBm = 25 mW
15.00 dBm = 31 mW
16.00 dBm = 39 mW
17.00 dBm = 50 mW
18.00 dBm = 63 mW
19.00 dBm = 79 mW
20.00 dBm = 100 mW
21.00 dBm = 125 mW
22.00 dBm = 158 mW
23.00 dBm = 199 mW
24.00 dBm = 251 mW
25.00 dBm = 316 mW
26.00 dBm = 398 mW
27.00 dBm = 501 mW
28.00 dBm = 630 mW
29.00 dBm = 794 mW
30.00 dBm = 1000 mW
31.00 dBm = 1258 mW
32.00 dBm = 1584 mW
33.00 dBm = 1995 mW
```

