from flask import Flask, url_for, request, redirect, abort
import bookdao

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

@app.route('/books', methods=['GET'])
def get_all():
    return "get all"

@app.route('/books/<int:id>', methods=['GET'])
def find_by_id(id):
    return f"find by id, book {id}"

#create
@app.route('/books', methods=['POST'])
def create():
    jsonstring = request.json

    return f"create {jsonstring}"

#update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"

#delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == "__main__":
    app.run(debug=True)

