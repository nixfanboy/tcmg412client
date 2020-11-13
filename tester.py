import requests

API_HOST = "http://35.192.209.218"

keyval_tests = {
    "test1": 1,
    "test2": 2,
    "test3": 3,
    "test4": 4,
    "test5": 5
}

md5_tests = {
    "test1": "5a105e8b9d40e1329780d62ea2265d8a",
    "tcmg412": "83c6a8d9e65ce93a214cb33f101a214c",
    "tamu2021": "2324e5446c642a842415405e532681d7"
}

prime_tests = {
    0: True,
    1: False,
    2: True,
    4: False,
    7: True
}

fib_tests = {
    0: [0],
    2: [0, 1, 1, 2],
    10: [0, 1, 1, 2, 3, 5, 8]
}

fac_tests = {
    2: 2,
    5: 120,
    8: 40320
}

total_tests = 0
passed_tests = 0

print("Starting keyval tests...")
for k in keyval_tests.keys():
    total_tests += 1
    resp = requests.post(API_HOST + "/keyval/" + str(k) + "/" + str(keyval_tests[k]))
    print("Setting Key: ", str(k), " to ", str(keyval_tests[k]), "...")
    if resp.status_code == 200:
        passed_tests += 1
        print("\t\tSuccess!")
    else:
        print("\t\tFailure, got response code ", resp.status_code)

for k in keyval_tests.keys():
    total_tests += 1
    resp = requests.get(API_HOST + "/keyval/" + str(k))
    expected = keyval_tests[k]
    print("Getting Key: ", str(k), ", expecting ", str(expected), "...")
    if resp.status_code == 200:
        val = resp.json()["value"]
        if val == str(expected):
            passed_tests += 1
            print("\t\tSuccess!")
        else:
            print("\t\tFailure, got value ", str(val), " instead of ", str(expected))
    else:
        print("\t\tFailure, got response code ", str(resp.status_code))

for k in keyval_tests.keys():
    total_tests += 1
    resp = requests.delete(API_HOST + "/keyval/" + str(k))
    print("Deleting Key: ", str(k), "...")
    if resp.status_code == 200:
        passed_tests += 1
        print("\t\tSuccess!")
    else:
        print("\t\tFailure, got response code ", str(resp.status_code))

print("\nStarting md5 tests...")
for k in md5_tests.keys():
    total_tests += 1
    resp = requests.get(API_HOST + "/md5/" + str(k))
    expected = md5_tests[k]
    print("Testing md5 for ", str(k), ", expecting ", str(expected))
    if resp.status_code == 200:
        val = resp.json()["output"]
        if val == expected:
            passed_tests += 1
            print("\t\tSuccess!")
        else:
            print("\t\tFailure, got value ", str(val), " instead of ", str(expected))
    else:
        print("\t\tFailure, got response code ", str(resp.status_code))

print("\nStarting prime tests...")
for k in prime_tests.keys():
    total_tests += 1
    resp = requests.get(API_HOST + "/is-prime/" + str(k))
    expected = prime_tests[k]
    print("Testing primality of ", str(k), ", expecting ", str(expected))
    if resp.status_code == 200:
        val = resp.json()["output"]
        if val == expected:
            passed_tests += 1
            print("\t\tSuccess!")
        else:
            print("\t\tFailure, got value ", str(val), " instead of ", str(expected))
    else:
        print("\t\tFailure, got response code ", str(resp.status_code))

print("\nStarting factorial tests...")
for k in fac_tests.keys():
    total_tests += 1
    resp = requests.get(API_HOST + "/factorial/" + str(k))
    expected = fac_tests[k]
    print("Testing factorial of ", str(k), ", expecting ", str(expected))
    if resp.status_code == 200:
        val = resp.json()["output"]
        if val == expected:
            passed_tests += 1
            print("\t\tSuccess!")
        else:
            print("\t\tFailure, got value ", str(val), " instead of ", str(expected))
    else:
        print("\t\tFailure, got response code ", str(resp.status_code))

print("\nStarting fibonacci tests...")
for k in fib_tests.keys():
    total_tests += 1
    resp = requests.get(API_HOST + "/fibonacci/" + str(k))
    expected = fib_tests[k]
    print("Testing fibonacci up to ", str(k), ", expecting ", str(expected))
    if resp.status_code == 200:
        val = resp.json()["output"]
        if val == expected:
            passed_tests += 1
            print("\t\tSuccess!")
        else:
            print("\t\tFailure, got value ", str(val), " instead of ", str(expected))
    else:
        print("\t\tFailure, got response code ", str(resp.status_code))

    print("\nStarting slack tests...")
    total_tests += 1
    resp1 = requests.get(API_HOST + "/slack-alert/Hello%20There.")
    total_tests += 1
    resp2 = requests.get(API_HOST + "/slack-alert/I%20Like%20Strings.")

    if resp1.status_code == 200 and resp2.status_code == 200:
        print("Success! Both messages posted successfully!")
        passed_tests += 2
    else:
        if resp1.status_code != 200:
            print("Message 'Hello There.' failed to post, received status code: ", str(resp1.status_code))
        else:
            passed_tests += 1

        if resp2.status_code != 200:
            print("Message 'I Like Strings.' failed to post, received status code: ", str(resp2.status_code))
        else:
            passed_tests += 1
        print("\t\tFailure!")

print("\n\nTOTAL TESTS PASSED: ", str(passed_tests), "/", str(total_tests), " = ", str((passed_tests / total_tests)*100), "%")

return (total_tests - passed_tests)
