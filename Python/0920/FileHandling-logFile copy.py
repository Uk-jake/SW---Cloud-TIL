data = []
dict = {}
sum = 0

try:
    with open("./Python/0920/log.txt", "r") as logFile:
        logs = logFile.readlines()
        tot = 0
        ipDict = {}
        
        for log in logs:
            data = log.split()
            
            try:
                tot += int(data[9])
            except:
                tot += 0
        
            try:
                ipDict[data[0]] = ipDict.get(data[0], 0) + int(data[9])
            except:
                ipDict[data[0]] = ipDict.get(data[0], 0) + 0
            
        
        
            
except FileNotFoundError:
    print("File not found")
    