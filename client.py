import requests
import sys
from slack import WebClient

API_HOST = "35.192.209.218:5000"

# Functions
def keyval_get(key):
    return

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
    response = SLACK_APP.chat_postMessage(channel='#testing-day', text=message)
    return jsonify(input=message, output=response["ok"])

if __name__ == "__main__":
    print("Attempting to read Slack App Key from slack.key file...")
    SLACK_KEY = None
    for l in open("slack.key"):
        SLACK_KEY = l.replace(" ", "")
    if SLACK_KEY == None or len(SLACK_KEY) < 55:
        print("ERROR: Could not read Slack App Key from slack.key file!")
    else:
        print("Connecting to Slack App with Key ", SLACK_KEY)
        SLACK_APP = WebClient(SLACK_KEY)

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
    t = requests.post(f'http://{API_HOST}/slack_alert/{message}')
    print(t.json())
    return
else:
    print_help()
