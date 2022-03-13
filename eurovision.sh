#! /bin/bash

output=""
echo $(echo "bon jour" | tr -d ' ')

for i in $(seq 1 $(wc -l countries.txt | awk '{print $1}'))
do
    url=$(cat url.txt | head -n $i | tail -n 1)
    output+=$(wget -qO- $url | grep -oP '(?<={"text":" • "},{"text":").*(?=vue)' | tr -d ' '),
done
echo $output >> eurovision.csv
