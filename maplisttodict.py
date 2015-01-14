

def getFromDict(dataDict, mapList):    
    for i, k in enumerate(mapList):
        prev = dataDict 
        if isinstance(dataDict, dict):
            dataDict = dataDict.get(k)
        else:
            return (None, mapList[:i], None)
    if dataDict:
        if isinstance(dataDict, dict):
            return (None, mapList[:i+1], dataDict.keys())
        else:
            return (dataDict, mapList[:i+1], None)
    else:
        return (None, mapList[:i], prev.keys())


a={1:{2:{3:{4:0}}}}
b=[1,2,  3, 4, 5, 6]


data, valid, next = getFromDict(a,b)

print a, b
print 'data', data, 'valid', valid, 'next', next

