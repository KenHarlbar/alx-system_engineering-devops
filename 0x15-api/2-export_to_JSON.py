#!/usr/bin/python3
""" Export to JSON """
import json
import requests
from sys import argv


if __name__ == '__main__':
    # Get employee data
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': user_id}).json()
    username = user[0]['username']

    # Get todo_list data
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={'userId': user_id}).json()

    json_data = []
    for each in todo_list:
        my_dict = {}
        my_dict['task'] = each['title']
        my_dict['completed'] = each['completed']
        my_dict['username'] = username
        json_data.append(my_dict)

    mydictionary = {user_id: json_data}

    # Compute the output
    with open('{}.json'.format(user_id), 'a') as f:
        json.dump(mydictionary, f)
