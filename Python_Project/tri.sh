#/usr/bin/bash

tee /dev/tty | grep -E '/etc/' | awk  '{print "File: "$6,"\tHost:node1 ","\tChecksum: "$8}' > checksum.txt ; sed -i '2s/node1/node2/g' checksum.txt
