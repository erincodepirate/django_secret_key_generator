#!/usr/bin/python3
from django.core.management.utils import get_random_secret_key

new_key = get_random_secret_key()

f = open("secret_key.py", "w")
f.write("SECRET_KEY = '" + str(new_key) + "'\n")
f.close()