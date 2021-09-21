#!/usr/bin/env python3

import os
import requests


url = os.getenv("URL")

print(requests.get(url).text)

