#!/usr/bin/python3
""" Export to CSV """
import csv
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

    csv_data = []
    for each in todo_list:
        my_dict = []
        my_dict.append(user_id)
        my_dict.append(username)
        my_dict.append(each['completed'])
        my_dict.append(each['title'])
        csv_data.append(my_dict)

    # Compute the output
    with open('{}.csv'.format(user_id), mode='a') as csv_file:
        user_writer = csv.writer(csv_file,
                                 quotechar='"',
                                 quoting=csv.QUOTE_ALL)
        for each in csv_data:
            user_writer.writerow(each)
