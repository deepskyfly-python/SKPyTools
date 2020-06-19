from configparser import ConfigParser
 

def GetParamList(filePath):
    cfg = ConfigParser()
    cfg.read(filePath)

    sectionName = cfg.sections()[0]
    paramList = []
    for item in cfg.items(sectionName):
        if item[1] == '1':
            if(item[0] == 'BuildCookRun' or item[0] == 'MakeUTDLC'):
                paramList.append(item[0])
            else:
                paramList.append('-'+item[0])
        else:
            paramList.append('-'+item[0]+'='+item[1])
    
    return paramList

print(GetParamList('win64.ini'))

 

