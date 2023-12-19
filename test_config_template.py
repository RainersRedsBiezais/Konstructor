import os
import requests

print("Configuration file test")

# Testing if configuration file template exists on disk in the current working directory
print("----------")
print("Checking if config template file exists -->")
assert os.path.isfile("config.ini.template") == True
print("OK")
print("----------")
