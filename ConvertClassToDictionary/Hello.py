
class Hello:

    def __init__(self):
        self.name = 'Bharat'
        self.age = '12'


k = Hello()
print(k.__dict__)

print("This dictionary can be directly converted to Json object for serialization")

import  json
k_json = json.dumps(k.__dict__)
print(k_json)
print("This json can be directly used to send in api calls")

