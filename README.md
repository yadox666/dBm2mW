# dBm2mW

This is a sample and simple script in Python Programming Language 
to convert input values in dBm to its corresponding value in mW or
viceversa.

The input argument is parsed and cleaned to extract the digits,
the decimal comma or point and the units to convert. If no input
argumment is passed, usage is shown and a table with some values.

The functions ar very usefull to be included in Wi-Fi scripts where
you have to convert RF values in both units. Feel free to use or
include it in your own scripts.

*Yago Hansen*

## Samples:

```
python dBm2mW.py 9.23dBm
python dBm2mW.py 1000mW
python dBm2mW.py 9,23 dBm
```

