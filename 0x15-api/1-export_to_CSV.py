#!/usr/bin/python3
""" Export to CSV """
import requests
from sys import argv
import csv


if __name__ == '__main__':
    # Get employee data
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': user_id}).json()
    username = user[0]['username']

    # Get todo_list data
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={'userId': user_id}).json()

    # Compute the output
    with open('{}.csv'.format(user_id), mode='a') as csv_file:
        fieldnames = ['user_id',
                      'username',
                      'task_completed_status',
                      'task_title']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames
                                quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for each in todo_list:
            writer.writerow({'user_id': user_id,
                             'username': username,
                             'task_completed_status': each['completed'],
                             'task_title': each['title']})
