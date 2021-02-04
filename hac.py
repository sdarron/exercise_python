#! /usr/bin/python3

import requests

list1 = ['https://passport.yandex.ru/profile', 
		'http://github.com', 
		'http://repl.it', 
		'http://losst.ru', 
		'http://translate.google.ru']

list = ['http://trudkirov.ru']

for alement in list:
	for i in range(100):
		response = requests.get(alement)
		print(response.status_code)
