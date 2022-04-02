#!/usr/bin/python3

import time
j = [1089, 1086, 1089, 1080, 32, 1093, 1091, 1081]

while True:
    for i in j:
        print(chr(i), end='', flush=True)
        time.sleep(0.05)
    time.sleep(1)
    print()
