import requests

class APIError(Exception):
    pass

URL = 'http://localhost:5000'

def create_todo(new_task={}):
    try:
        response = requests.post(f"{URL}/todos", json=new_task)
    except IOError:
        raise ValueError

    try:
        data = response.json() 
    except ValueError:
        raise APIError('aaaa ')    
    if response.ok:
        return data


response = requests.get(f"{URL}/todos")

print(response)
print(response.status_code)
print(response.ok)  # check if status code is <400


# data = response.json()
# print(type(data))
# print(data)
# print(data[0]['task'])

# payload = {'task': "Some new task"}
# response = requests.post(f"{URL}/todos", json=payload)
# print(response)
# print(response.json())

# response = requests.get(f"{URL}/todos")
# print(response.json())

new_task= {'task': "super grup rules"}
create_todo(new_task)
response = requests.get(f"{URL}/todos")

print(response)

response = requests.get(f"{URL}/todos")
print(response.json())