# illumio
Illumio Technical Assessment


Requirement details
1. Input file as well as the file containing tag mappings are plain text (ascii) files  
2. The flow log file size can be up to 10 MB
3. The lookup file can have up to 10000 mappings
4. The tags can map to more than one port, protocol combinations.  for e.g. sv_P1 and sv_P2 in the sample above.
5. The matches should be case insensitive


Assumptions
1. Use below reference for flow logs and only version 2 is supported.
    https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html  
2. Downloaded protocol numbers for flow logs to mapping
    https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

Execution
1. Run using following python command

    python3 main.py

2. The program waits for following user input
    a. Flow log content file path
    b. Tags csv file path

    If both are emtpy it uses the following files in same directory
    a. flowLogs.txt
    b.tags.csv

3. Output is written to output directory

    a. output/tagCounts.csv
    b. output/portProtocolCounts.csv
