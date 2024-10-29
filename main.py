import tag
import csv
import os
import logging

logging.basicConfig(level=logging.DEBUG)


tagCount = {}
portPortocolCount = {}

protocolDict = {}

def readProtocolNumbersCSVFileContent(filePath):
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dstPort, protocol = row[:2]
            protocolDict[dstPort] = protocol.lower()
        logging.debug("Processed protocol numbers csv file")

def readFlowLogFileContent(filePath):
    with open(filePath, 'r') as file:
        for line in file:
            fields = line.split()
            if len(fields) >= 8:
                version = fields[0]
                if version != '2':
                    continue
                dstPort = fields[6]
                protocol = fields[7].lower()

                tag = tagsDict.getTag(dstPort, protocolDict[protocol])
                if tag not in tagCount:
                    tagCount[tag] = 0

                tagCount[tag] = tagCount[tag] + 1

                portProtocolKey = (dstPort, protocolDict[protocol])
                if portProtocolKey not in portPortocolCount:
                    portPortocolCount[portProtocolKey] = 0
                portPortocolCount[portProtocolKey] = portPortocolCount[portProtocolKey] + 1

        logging.debug("Processed flow log content file")

    logging.debug(tagCount)
    logging.debug(portPortocolCount)


def writeTagCountsOutputFile():

    fieldnames = ['Tag', 'Count']  # Extract field names from the first dictionary

    os.makedirs('output', exist_ok=True)

    data_list = [{'Tag': key, 'Count': value} for key, value in tagCount.items()]

    with open('output/tagCounts.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)

    logging.info('Tag counts file written to output dir')


def writePortProtoCountsOutputFile():

    fieldnames = ['Port', 'Protocol', 'Count']  # Extract field names from the first dictionary

    os.makedirs('output', exist_ok=True)
    data_list = [{'Port': key[0], 'Protocol': key[1], 'Count': value} for key, value in portPortocolCount.items()]

    with open('output/portProtocolCounts.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)

    logging.info('Port Protocol combination counts file written to output dir')

def get_current_log_level():
    """Gets the current logging level of the root logger."""
    return logging.getLogger().level


if __name__ == "__main__":
    log_level = get_current_log_level()
    print(f"Current log level: {log_level}")


    flowLogPath = input("Flow log file path: ")
    tagFilePath = input("Tag file path (in CSV): ")
    if flowLogPath == '':
        flowLogPath = 'flowLogs.txt'
    if tagFilePath == '':
        tagFilePath = 'tags.csv'
    logging.debug(f"Flow Log Path: {flowLogPath}")
    logging.debug(f"Tag File Path: {tagFilePath}")

    # read tags from tag file path
    tagsDict = tag.readTagCSVFileContent(tagFilePath)

    # read protocol-numbers.csv file content
    readProtocolNumbersCSVFileContent("protocol-numbers.csv")

    # read flow log content
    readFlowLogFileContent(flowLogPath)

    # write tag counts file
    writeTagCountsOutputFile()

    # write port protocol combination file
    writePortProtoCountsOutputFile()
