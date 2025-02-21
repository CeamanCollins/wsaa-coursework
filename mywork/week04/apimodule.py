import requests
URL = " http://andrewbeatty1.pythonanywhere.com/books"
# import json
def get_books():
    response = requests.get(URL)
    return response.json()

def read_book(id):
    geturl = URL + '/' + str(id)
    response = requests.get(geturl)
    return response.json()

def create_book(book):
    # headers ={"Content-type": "application/json"}
    # response = requests.post(URL, json=book, headers=headers)
    response = requests.post(URL, json=book)
    return response

def update_book(id, book):
    updateurl = URL + '/' + str(id)
    response = requests.put(updateurl, json=book)
    return response

def delete_book(id):
    deleteurl = URL + '/' + str(id)
    response = requests.delete(deleteurl)
    return response

if __name__ == "__main__":
    pass
    # print(get_books())
    # print(read_book(603))
    # print(create_book({'title' : 'Lathe of Heaven', 'author' : 'Ursula le Guinn', 'price' : 1799}))
    # print(create_book({'title' : 'Camera Lucidia', 'author' : 'Roland Barthes', 'price' : 1599}))
    # print(update_book())
    # print(update_book(602, {'price':1999}))
    # print(get_books())


# with open('response.json', 'w') as fp:
#      json.dump(response.json(), fp)

