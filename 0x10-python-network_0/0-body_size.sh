#!/bin/bash
### Displays the size of a response body
# Synopsis: ./0-body_size <URL>
### Size is displayed in bytes
curl -s "$1" | wc -m
