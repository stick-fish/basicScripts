#!/bin/bash

if [ -z "$1" ]
then 
  echo "***DNS TRANSFER SCRIPT***"
  echo "Enter script name followed by hostname to check"
  echo "Example -->  $0 <hostname>"
else 
  for name in $(host -t ns $1); do
    result=$(host -l $1 $name | grep "has address" | sed s/"has address"/"  "/ >> $1)
  done
  echo "| -- Output saved to $1 --|"
fi
