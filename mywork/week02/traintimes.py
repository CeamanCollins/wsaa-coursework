import requests
import csv
from xml.dom.minidom import parseString

url='https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'

page = requests.get(url)
doc = parseString(page.content)

# check it works

# print(doc.toprettyxml(), end='')

# with open('trainxml.xml','w') as xmlfp:
#     doc.writexml(xmlfp)

# objTrainPositionNodes = doc.getElementsByTagName('objTrainPositions')
# for objTrainPositionNode in objTrainPositionNodes:
#     # traincodenode = objTrainPositionNode.getElementsByTagName('TrainCode').item(0)
#     # traincode = traincodenode.firstChild.nodeValue.strip()
#     # print(traincode)

#     trainlattitudenode = objTrainPositionNode.getElementsByTagName('TrainLatitude').item(0)
#     trainlattitude = trainlattitudenode.firstChild.nodeValue.strip()
#     print(trainlattitude)

retrieveTags = ['TrainStatus',
                'TrainLatitude',
                'TrainLongitude',
                'TrainCode',
                'TrainDate',
                'PublicMessage',
                'Direction'
                ]

with open('week02_train_d.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionNodes = doc.getElementsByTagName('objTrainPositions')
    for objTrainPositionNode in objTrainPositionNodes:
        traincodenode = objTrainPositionNode.getElementsByTagName('TrainCode').item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        # dataList.append(traincode)
        # if objTrainPositionNode.getElementsByTagName('TrainCode').item(0).firstChild.nodeValue.strip()[0] == 'D':
        if traincode[0] == 'D':
            for retrieveTag in retrieveTags:
                datanode = objTrainPositionNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
            train_writer.writerow(dataList)
            
