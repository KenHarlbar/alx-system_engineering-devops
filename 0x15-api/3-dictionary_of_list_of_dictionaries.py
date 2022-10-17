#!/usr/bin/python3
""" Export to JSON """
import json
import requests


if __name__ == '__main__':
    # Get employee data
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    mydictionary = {}
    for user in users:
        user_id = user['id']
        username = user['username']

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

        mydictionary[user_id] = json_data

    # Compute the output
    with open('todo_all_employees.json', 'w') as f:
        json.dump(mydictionary, f)
