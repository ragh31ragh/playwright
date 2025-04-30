import csv
with open('C:\\Users\\bgh51043\\PycharmProjects\\PytestPython\\BackendAutomation\\utilities\\loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    #print(list(csvReader))
    names = []
    status = []
    for row in csvReader:
        #print(row)
        #print(row[0])
        names.append(row[0])
        status.append(row[1])
    print(names)
    print(status)

with open('C:\\Users\\bgh51043\\PycharmProjects\\PytestPython\\BackendAutomation\\utilities\\loanapp.csv','a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["bob","rejected"])