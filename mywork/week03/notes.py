
# # 
# import requests
# import json

# url = "https://url/"
# response = requests.get(url)
# data = response.json()

# Informational responses (100 – 199)
# Successful responses (200 – 299)
# Redirection messages (300 – 399)
# Client error responses (400 – 499)
# Server error responses (500 – 599)

# get all
# curl http://andrewbeatty1.pythonanywhere.com/books
# create, -d = data
# curl -H "Content-Type:application/json" -X POST -d '{"title":"xxx","author":"xxx","price":3000}' http://andrewbeatty1.pythonanywhere.com/books
# update
# curl -H "Content-Type:application/json" -X PUT -d '{"price":2000} http://andrewbeatty1.pythonanywhere.com/books/7
# delete
# curl -H "Content-Type:application/json" -X DELETE http://andrewbeatty1.pythonanywhere.com/books/7
# to file
# curl -o ricksanchez.json https://rickandmortyapi.com/api/character/1