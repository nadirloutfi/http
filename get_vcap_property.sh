#!/bin/bash
suffix=${USERNAME:-$USER}
# make sure we use a lower case suffix, see https://stackoverflow.com/a/2264537
suffix=`echo "$suffix" | tr '[:upper:]' '[:lower:]'`

content=$(cf env ppro-firefly-$suffix| grep -o "\"$1\":.*" | cut -d'"' -f4 | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | sed 's/\\n/\n/g')
property_value=$(awk 'BEGIN {RS="\n\n"; ORS="\n\n"} NF { block = $0 } END { print block }' <<< "$content")

echo "$property_value"
