import requests

API_HOST = "http://35.192.209.218:5000"

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
  0: False,
  1: False,
  2: True,
  4: False,
  7: True
}

fib_tests = {
  0: [0],
  2: [0, 1, 1],
  10: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
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
  resp = requests.post(API_HOST + "/keyval/" + k + "/" + keyval_tests[k])
  print("Setting Key: ", k, " to ", keyval_tests[k], "...")
  if resp.response_code == 200:
    passed_tests += 1
    print("\t\tSuccess!")
  else:
    print("\t\tFailure, got response code ", resp.response_code)
 
 for k in keyval_tests.keys():
   total_tests += 1
   resp = requests.get(API_HOST + "/keyval/" + k)
   val = resp.json()["value"]
   expected = keyval_tests[k]
   print("Getting Key: ", k, ", expecting ", expected, "...")
   if resp.response_code == 200:
     if val == expected:
       passed_tests += 1
       print("\t\tSuccess!")
     else:
       print("\t\tFailure, got value ", val, " instead of ", expected)
   else:
     print("\t\tFailure, got response code ", resp.response_code)

  for k in keyval_tests.keys():
    total_tests += 1
    resp = requests.get(API_HOST + "/keyval/" + k)
   val = resp.json()["value"]
   expected = keyval_tests[k]
   print("Deleting Key: ", k, "...")
   if resp.response_code == 200:
     passed_tests += 1
     print("\t\tSuccess!")
   else:
     print("\t\tFailure, got response code ", resp.response_code)
  
print("\nStarting md5 tests...")
for k in md5_tests.keys():
  total_tests += 1
  resp = requests.get(API_HOST + "/md5/" + k)
  val = resp.json()["output"]
  expected = md5_tests[k]
  print("Testing md5 for ", k, ", expecting ", expected)
  if resp.response_code == 200:
     if val == expected:
       passed_tests += 1
       print("\t\tSuccess!")
     else:
       print("\t\tFailure, got value ", val, " instead of ", expected)
   else:
     print("\t\tFailure, got response code ", resp.response_code)
     
print("\nStarting prime tests...")
for k in prime_tests.keys():
  total_tests += 1
  resp = requests.get(API_HOST + "/is-prime/" + k)
  val = resp.json()["output"]
  expected = prime_tests[k]
  print("Testing primality of ", k, ", expecting ", expected)
  if resp.response_code == 200:
     if val == expected:
       passed_tests += 1
       print("\t\tSuccess!")
     else:
       print("\t\tFailure, got value ", val, " instead of ", expected)
   else:
     print("\t\tFailure, got response code ", resp.response_code)
     
print("\nStarting factorial tests...")
for k in fac_tests.keys():
  total_tests += 1
  resp = requests.get(API_HOST + "/factorial/" + k)
  val = resp.json()["output"]
  expected = fac_tests[k]
  print("Testing factorial of ", k, ", expecting ", expected)
  if resp.response_code == 200:
     if val == expected:
       passed_tests += 1
       print("\t\tSuccess!")
     else:
       print("\t\tFailure, got value ", val, " instead of ", expected)
   else:
     print("\t\tFailure, got response code ", resp.response_code)
     
print("\nStarting fibonacci tests...")
for k in fib_tests.keys():
  total_tests += 1
  resp = requests.get(API_HOST + "/fibonacci/" + k)
  val = resp.json()["output"]
  expected = fib_tests[k]
  print("Testing primality of ", k, ", expecting ", expected)
  if resp.response_code == 200:
     if val == expected:
       passed_tests += 1
       print("\t\tSuccess!")
     else:
       print("\t\tFailure, got value ", val, " instead of ", expected)
   else:
     print("\t\tFailure, got response code ", resp.response_code)
  
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
      print("Message 'Hello There.' failed to post, received status code: ", resp1.status_code)
    else:
      passed_tests += 1
      
    if resp2.status_code != 200:
      print("Message 'I Like Strings.' failed to post, received status code: ", resp2.status_code)
    else:
      passed_tests += 1
    print("\t\tFailure!")

print("\n\nTOTAL TESTS PASSED: ", passed_tests, "/", total_tests, " = ", str(passed_tests/total_tests))
