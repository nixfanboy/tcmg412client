import requests
import sys

API_HOST = "http://35.192.209.218:5000"

# Functions
def keyval_get(key):
    response = requests.get(API_HOST + "/keyval/" + key)
    if response.status_code == 409:
        print("Error: key ", key, " has no value!")
        return
    elif response.status_code == 200:
        print("Value of ", key, " is ", response.json()["output"])
        return
    else:
        print("Error: HTTP request responded with status code ", response.status_code)

def keyval_set(key, val):
    return

def md5(str):
    return

def is_prime(num):
    return

def fibonacci(num):
    return

def factorial(num):
    return
    
def slack_alert(message):
    return

def print_help():
    print("Format: ./client.py COMMAND <Args>")
    print("COMMAND options:")
    print("-- val: Gets or Sets values from database.")
    print("        Valid Args: GET <key>, SET <key> <value>")
    print("-- md5: Hashes input string using md5.")
    print("        Valid Args: <string to hash>")
    print("-- isprime: Tests if an integer is prime.")
    print("        Valid Args: <integer to test primality>")
    print("-- fib: Calculates fibonacci's sequence up to <x> steps.")
    print("        Valid Args: <x>")
    print("-- fac: Calculates the factorial of a number")
    print("        Valid Args: <number to factorialize>")
    print("-- slack: Posts a custom slack alert")
    print("        Valid Args: <word1>...<wordX>")
    exit()

# Interpret Command
if len(sys.argv) < 3:
    print_help()

COMMAND = sysv.args[1:]

if COMMAND[0].lower() == "val":
    if len(COMMAND) == 2:
        keyval_get(COMMAND[1])
    elif len(COMMAND) == 3:
        keyval_set(COMMAND[1], COMMAND[2])
    else:
        print("Error: Incorrect number of arguments")
    return # make sure inputs are valid then call method, which would call the API using the requests module (see link in slack) then report the result from the API to the user.
elif COMMAND[0].lower() == "md5":
    return
elif COMMAND[0].lower() == "isprime":
    return
elif COMMAND[0].lower() == "fib":
    return
elif COMMAND[0].lower() == "fac":
    return
elif COMMAND[0].lower() == "slack":
    return
else:
    print_help()
