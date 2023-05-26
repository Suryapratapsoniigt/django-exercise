import requests
import json

URL = "http://127.0.0.1:8000/getStudent/"

def getData(id = None):
    data={}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
        
    data = r.json()
    print(data, 'data')

getData()


def post_data():
    data ={
      'name' : 'sumit',
      'roll': 297,
      'city' : 'Sagar'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    res = r.json()
    print(res,'res')
    print(res['data'],'res')

# post_data()
# getData()


def updata_data():
    data ={
      'id' :8,
      'name' : 'Amit',
      'city': 'Indore',
      'roll' : '303'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    res = r.json()
    print(res,'res')
    print(res['data'],'res')

# updata_data()

def delete_data(id):
    json_data = json.dumps({'id': id})
    r = requests.delete(url=URL, data=json_data)
    res = r.json()
    print(res,'res')

delete_data(11)

