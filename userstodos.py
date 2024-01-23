#!/usr/local/bin/python3
#
#
#mchilty@gmail.com 20240121
#
#Collects and harmonizes oddball Latin homework completion status using 2 different approaches from:
#
#
#https://jsonplaceholder.typicode.com/users
#https://jsonplaceholder.typicode.com/todos
#https://jsonplaceholder.typicode.com/users/1
#
#
#Output example:
#{"userName": "Bret", "email": "Sincere@april.biz", "todoTitle":"delectus aut autem", "completed": false}
#
#configure the proxy as suits your needs
#
#

import json
import os
import requests


os.environ['REQUESTS_CA_BUNDLE'] = "/Users/mchilty/burpCAcert.pem"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
headers = {'User-Agent': 'mchilty-0.1'}

users_url = ("https://jsonplaceholder.typicode.com/users")
todos_url = ("https://jsonplaceholder.typicode.com/todos")
users_todos_url = ("https://jsonplaceholder.typicode.com/users/$id/todos")

users_response = requests.get(users_url, headers=headers, proxies=proxies)
todos_response = requests.get(todos_url, headers=headers, proxies=proxies)

users_response_data = users_response.json()
todos_response_data = todos_response.json()

print("Using the following API endpoints:")
print(users_url)
print(todos_url)
print(users_todos_url)
print()


#
#follows recommended approach provided in challenge
#uses data found in /todos and queries or fetches related data from the user's profile
#
todos_extract = {}
for todo in todos_response_data:
		userId = (todo['userId'])
		title = (todo['title'])
		completed = (todo['completed'])
		users_bio_url = (users_url + "/" + str(todo['userId']))
		users_bio_response = requests.get(users_bio_url, headers=headers, proxies=proxies) 
		users_bio_response_data = users_bio_response.json()
		
		username = (users_bio_response_data['username'])
		email = (users_bio_response_data['email'])
		
		todos_extract['userName'] = username
		todos_extract['email'] = email
		todos_extract['todoTitle'] = title
		todos_extract['completed'] = completed
		todos_extract_json_data = json.dumps(todos_extract)	
		print(todos_extract_json_data)
		
print()
print("################")
print()
	
#
#uses the data returned by /todos and /users without using subsequent GETs
#
another_todos_extract = {}
for user in users_response_data:
		username = (user['username'])
		email = (user['email'])

		for task in todos_response_data:
				title = (task['title'])
				completed = (task['completed'])
				
				if (task['userId']) == (user['id']):
					another_todos_extract['userName'] = username
					another_todos_extract['email'] = email
					another_todos_extract['todoTitle'] = title
					another_todos_extract['completed'] = completed
					another_todos_extract_json_data = json.dumps(another_todos_extract)	
					print(another_todos_extract_json_data)

print()
print("################")
print()		

#		
#uses the data returned by /users and queries or fetches todo data path from /users/$id/todos using subsequent GETs 
#
user_extract = {}
for user in users_response_data:
		userId = (user['id'])
		username = (user['username'])
		email = (user['email'])
		users_todos_url = (users_url + "/" + str(user['id']) + "/todos")
		users_todos_response = requests.get(users_todos_url, headers=headers, proxies=proxies)
		users_todo_response_data = users_todos_response.json()
		
		for task in users_todo_response_data:
			title = (task['title'])
			completed = (task['completed'])		
			user_extract['userName'] = username
			user_extract['email'] = email
			user_extract['todoTitle'] = title
			user_extract['completed'] = completed
			user_extract_json_data = json.dumps(user_extract)	
			print(user_extract_json_data)
			
print("Completum est.")
