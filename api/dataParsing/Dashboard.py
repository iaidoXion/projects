import pandas as pd

def Bar(parserData):
    print()


def Line(parserData):
    print()

def Line(parserData):
    print()

def Map(parserData):
    print()



def Banner(parserData) :
    ATC = len(parserData)
    AD = []
    for i in range(ATC):
        CI = parserData[i]['computer_id']
        AI = parserData[i]['asset_item']
        AIPer = AI.lower()
        if AIPer.startswith('macbook'):
            AI = 'Notebook'
        if AIPer.startswith('imac'):
            AI = 'Desktop'
        OP = parserData[i]['os_platform']
        CIA = parserData[0]['ci_installed_application']
        if CIA is not None:
            #print(CI)
            for j in CIA :
                applicationList = {'id':j['id'], 'applicationName':j['normalized_name']}
                #print(applicationList)
                #print(CIA[j]['normalized_name'])

        #CIAC = len(CIA)
        #for j in range(CIAC) :
    #    CIAID = CIA[j]['id']
    #        CIANNM = CIA[j]['normalized_name']
    #        print(CIAID)
    #        print(CIANNM)


        AD.append(
            [
                CI,
                AI,
                OP
            ]
        )
    ACNM = ["id", "item", "os"]
    ADf = pd.DataFrame(AD, columns=ACNM)
    IG = ADf.groupby(["item"])
    AIGB = IG.size().reset_index(name='counts')
    AIDL = AIGB.item
    AICDL = AIGB.counts

    ACL = []
    for A in range(len(AIDL)) :
        list = {AIDL[A] : AICDL[A]}
        ACL.append(list)

    OG = ADf.groupby(["os"])
    AOGB = OG.size().reset_index(name='counts')
    AODF = AOGB.os
    AODL = AODF.tolist()
    AOCDF = AOGB.counts
    AOCDL = AOCDF.tolist()
    OSCL =[]

    for OS in range(len(AODL)) :
        list = {AODL[OS] : AOCDL[OS]}
        OSCL.append(list)

    returnList = {'asset_total_count': ATC, 'os_item_count' : OSCL,'asset_item_count' : ACL }
    #print(returnList)
    return returnList




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
    returnList = {'item' : {'name':AIDL.tolist(), 'value':AICDL.tolist()},
        'os':{'name':AODL.tolist(), 'value': AOCDL.tolist()},
        'osi':{'name':AOIDL.tolist(), 'value': AOICDL.tolist()}
    }
    #{'item': {'name': ['Desktop', 'MacBookPro18,1', 'Notebook', 'Rack Mount Chassis'], 'value': [1, 1, 11, 8]}, 'os': {'name': ['Linux', 'Mac', 'Windows'], 'value': [8, 1, 12]}, 'osi': {'name': ['CentOS', 'Ubuntu', 'Windows', 'macOS'], 'value': [7, 1, 12, 1]}}
    return returnList





