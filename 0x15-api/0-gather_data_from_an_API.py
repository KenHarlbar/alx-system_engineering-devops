#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
from sys import argv


if __name__ == '__main__':
    # Get employee data
    employee_id = argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users',
                            params={'id': employee_id}).json()
    employee_name = employee[0]['name']

    # Get todo_list data
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={'userId': employee_id}).json()

    # Compute the output
    total_number_of_tasks = len(todo_list)
    number_of_done_tasks = 0
    for each in todo_list:
        if each['completed']:
            number_of_done_tasks += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, number_of_done_tasks, total_number_of_tasks))
    for each in todo_list:
        if each['completed']:
            print('\t {}'.format(each['title']))
