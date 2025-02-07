# with open(filename) as fp:
#     # do what you want

# import requests
# page = requests.get("URL")
# print(page)
# print("----------")
# print(page.content)

# # for files

# from xml.dom.minidom import parse
# filename = "file.xml"
# #read file in two ways

# doc = parse(filename)

# #or

# with open(filename) as fp: # fp = filepointer

#     doc = parse(fp)

# # check it works

# print(doc.toprettyxml(), end='') # output to console

# # for content from the cloud 

# import requests

# from xml.dom.minidom import parseString
# url = "http://someurl.com/"

# page = requests.get(url)
# doc = parseString(page.content)

# # check it works

# print(doc.toprettyxml(), end='') # output to console

# # get the employee elements as a list
from xml.dom.minidom import parse

filename = "employees.xml"
# read file in two ways
doc = parse(filename)

employeeNodeList = doc.getElementsByTagName("Employee")
print(len(employeeNodeList))
for employeeNode in employeeNodeList:
    #print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)

    
