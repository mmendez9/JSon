import os
import json

# Read in json file
wData = open("weather.json", "r")
wLines = wData.read()

# convert json to python
weatherD = json.loads(wLines)

wData.close()

print(weatherD)
print(weatherD.keys())  # Keys in the file
print("\n\n")
print(weatherD["main"]["temp"])
print(weatherD["main"]["humidity"])
print(weatherD["wind"]["speed"])
