import requests
import sys

API_HOST = "http://35.192.209.218"

# Functions
def keyval_get(key):
    response = requests.get(API_HOST + "/keyval/" + key)
    if response.status_code == 409:
        print("Error: key ", key, " has no value!")
        return
    elif response.status_code == 200:
        print("Value of ", key, " is ", response.json()["value"])
        return
    else:
        print("Error: HTTP request responded with status code ", response.status_code)

def keyval_del(key):
    response = requests.delete(API_HOST + "/keyval/" + key)
    if response.status_code == 409:
        print("Error: key ", key, " has no value already!")
        return
    elif response.status_code == 200:
        print("Key ", key, " deleted!")
        return
    else:
        print("Error: HTTP request responded with status code ", response.status_code)

def keyval_set(key, val):
    return

def md5(str):
    response = requests.get(API_HOST + "/md5/" + str)
    print(str," Is equal to", response.json()["output"])
    return

def is_prime(num):
    response = requests.get(API_HOST + "/is-prime/" + num)
    if response.json()["output"] == True:
      print(num," Is a Prime")
      return
    else:
      print(num," Is NOT a Prime")
      return

def fibonacci(num):
    response = requests.get(API_HOST + "/fibonacci/" + num)
    print(num," Is equal to", response.json()["output"])
    return

def factorial(num):
    response = requests.get(API_HOST + "/factorial/" + num)
    print("The factorial of ",num, " is ", response.json()["output"])  
    return
    
def slack_alert(message):
  response = requests.get(API_HOST+"/slack-alert/"+message)
  if response.status_code == 400:
    print("Unable to connect to Slack, check Slack Key value and try again")
    return
  elif response.status_code == 200:
    print("Message posted succesfully to Slack channel!")
    return
  else:
    print("Error: HTTP request responded with status code ", response.status_code)
    return

def print_help():
    print("Format: ./client.py COMMAND <Args>")
    print("COMMAND options:")
    print("-- val: Gets or Sets values from database.")
    print("        Valid Args: GET <key>, SET <key> <value>, DEL <key>")
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

COMMAND = sys.argv[1:]

if COMMAND[0].lower() == "val":
    if len(COMMAND) == 3:
        if COMMAND[1].lower() == "get":
            keyval_get(COMMAND[2])
        elif COMMAND[1].lower() == "del":
            keyval_del(COMMAND[2])
    elif len(COMMAND) == 4 and COMMAND[1].lower() == "set":
        keyval_set(COMMAND[2], COMMAND[3])
    else:
        print("Error: Incorrect number of arguments or invalid command!")
      return # make sure inputs are valid then call method, which would call the API using the requests module (see link in slack) then report the result from the API to the user.

elif COMMAND[0].lower() == "md5":
    md5(COMMAND[1])

elif COMMAND[0].lower() == "slack":
   slack_alert(COMMAND[1])

elif COMMAND[0].lower() == "fac":
    factorial(COMMAND[1])

elif COMMAND[0].lower() == "fib":
    fibonacci(COMMAND[1])

elif COMMAND[0].lower() == "isprime":
    is_prime(COMMAND[1])
