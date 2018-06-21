#!/usr/bin/env python

"""helper.py: Important Helper functions."""
__author__ = "Ashish Belwase"


try:
    import httplib
except:
    import http.client as httplib
import csv
from datetime import datetime
import json


def validateLength(word, min, max):
	pass

def check_internet_connection():
	"""
	check if internet connection is ok
	"""
	conn = httplib.HTTPConnection("www.google.com", timeout=5)
	try:
		conn.request("HEAD", "/")
		conn.close()
		return True
	except:
		conn.close()
		return False

def count_unique_license(rows):
	"""
	count unique license plates in input rows
	"""
	unique_license = []
	for row in rows:
		pass	



def csvtoDict(path):
	with open(path) as f:
		#a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
		a = []
		for row in csv.DictReader(f, skipinitialspace=True):
			a.append(row)
		return a

		# rows = []
		# for row in csv.DictReader(f, skipinitialspace=True):
		# 	print (row)

		# return rows


def load_settings():
    settings = json.loads(open('./settings.json', 'r').read())['settings']
    return settings

def update_settings(settings):
	data = {'settings':settings}
	with open('./settings.json', 'w') as f:
		json.dump(data, f, ensure_ascii=False, indent=2)				