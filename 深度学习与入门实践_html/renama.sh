#!/bin/bash

for file in *.md; do
    mv "$file" "${file%.md}.html"
done

