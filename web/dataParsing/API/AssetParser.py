import pandas as pd

def InfoParsing(parserData) :
    PDLC = len(parserData)
    AD=[]
    for i in range(PDLC) :
        OIDS = parserData[i]['operating_system'].split(' ')
        AD.append(
            [
                parserData[i]['computer_id'],
                parserData[i]['asset_item'],
                parserData[i]['os_platform'],
                OIDS[0]
            ]
        )
    ACNM = ["id", "item", "os", "osItem"]
    ADf = pd.DataFrame(AD, columns=ACNM)
    IG = ADf.groupby(["item"])
    OGroup = ADf.groupby(["os"])
    OIGroup = ADf.groupby(["osItem"])
    AIGB = IG.size().reset_index(name='counts')
    AOGB = OGroup.size().reset_index(name='counts')
    AOIGB = OIGroup.size().reset_index(name='counts')
    AIDL = AIGB.item
    AICDL = AIGB.counts
    AODL = AOGB.os
    AOCDL = AOGB.counts
    AOIDL = AOIGB.osItem
    AOICDL = AOIGB.counts
    returnList = {
        'item' : {'name':AIDL.tolist(), 'value':AICDL.tolist()},
        'os':{'name':AODL.tolist(), 'value': AOCDL.tolist()},
        'osi':{'name':AOIDL.tolist(), 'value': AOICDL.tolist()}
    }
    #{'item': {'name': ['Desktop', 'MacBookPro18,1', 'Notebook', 'Rack Mount Chassis'], 'value': [1, 1, 11, 8]}, 'os': {'name': ['Linux', 'Mac', 'Windows'], 'value': [8, 1, 12]}, 'osi': {'name': ['CentOS', 'Ubuntu', 'Windows', 'macOS'], 'value': [7, 1, 12, 1]}}
    return returnList