#!/bin/bash
#Quick and dirty as they say.

if [ -z "$1" ]
then 
  echo "***DNS TRANSFER SCRIPT***"
  echo "Enter script name followed by hostname to check"
  echo "Example -->  $0 <hostname>"
else 
  for name in $(host -t ns $1); do
    result=$(host -l $1 $name | grep "has address" | sort -u >> $1.txt)
  done
fi
 echo "To view the results: cat $1.txt"
