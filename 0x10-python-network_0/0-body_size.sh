#!/bin/bash
### Displays the size of a response body
curl -s "$1" | wc -m
