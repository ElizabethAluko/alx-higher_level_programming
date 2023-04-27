#!/bin/bash
# Sends JSON POST request to s URL passed
curl -s -H "Content-Type: appliation/json" -d "$(cat "$2")" "$1"
