import csv
import logging

class Tag():

    def __init__(self):
        self.tagDict = {}

    def add(self, dstPort, protocol, tag):
        key = self.getKey(dstPort, protocol)
        if key not in self.tagDict:
            self.tagDict[key] = ''
        self.tagDict[key] = tag

    def getKey(self, dstPort, protocol):
        return dstPort + '_' + protocol

    def getTag(self, dstPort, protocol):
        key = self.getKey(dstPort, protocol)
        if key not in self.tagDict:
            return 'Untagged'
        return self.tagDict[key]



def readTagCSVFileContent(filePath):

    tags = Tag()
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dstPort, protocol, tag = row
            if dstPort == None:
                dstPort = ''
            if protocol == None:
                protocol = ''
            if tag == None:
                tag = ''
            tags.add(dstPort, protocol.lower(), tag)

        logging.debug("Processed tags csv file")

    return tags
