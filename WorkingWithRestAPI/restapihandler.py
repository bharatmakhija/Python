import pip._vendor.requests as requests
from pip._vendor.requests.auth import HTTPDigestAuth
from pip._vendor.distlib.compat import raw_input
import json

# A sample get call
r = requests.get('https://www.python.org')
print(r.status_code)

# generic post call
payload = dict(key1='username', key2='password')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)


#Performing get call where we need to parse data from 

url = "http://api_url"

# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
myResponse = requests.get(url,auth=HTTPDigestAuth(raw_input("username: "), raw_input("Password: ")), verify=True)
print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):
    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)
else:
    # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()

