#!/bin/zsh

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <day> <name>"
    exit 1
fi

year=$(date +'%Y')
day=$1
name=$2

dir="${year}/${day}_${name}"
mkdir "$dir"

cp -r ./template/* "$dir"
mv "$dir/aoc_template.py" "$dir/aoc${year}${day}.py"
