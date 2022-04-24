#!/bin/bash
# bash script that takes url sends request and displays size of body response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
