#!/bin/sh

bytes=$(objdump -d $1 | grep 400 | grep -v ">:" | cut -f 2 | tr " " "\n" | tr -s "\n" )
hex=$(echo $bytes | python -c "import sys,re; print ''.join(r'\x%s'%c for c in sys.stdin.read().split())")
echo "$hex"


