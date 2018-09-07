#!/bin/bash
#Super rough version (X = ip octets)

for i in $(seq 0 254)
 do ping -c 1 X.X.X.$i | grep "bytes from" | cut -d ' ' -f 4 | sed s/:/''/ >> $0_results.txt &
done
