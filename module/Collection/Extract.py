import psycopg2
import json
from datetime import datetime, timedelta
with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
DataLoadingType = SETTING['MODULE']['DataLoadingType']
DBHost = SETTING['DB']['DBHost']
DBName = SETTING['DB']['DBName']
DBUser = SETTING['DB']['DBUser']
DBPwd = SETTING['DB']['DBPwd']
AssetTNM = SETTING['DB']['AssetTNM']
StatisticsTNM = SETTING['DB']['StatisticsTNM']
BS = SETTING['FILE']
today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
day = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")
fiveDay = (datetime.today() - timedelta(5)).strftime("%Y-%m-%d")

def AssetYesterday() :
    AssetSelectL = []
    if DataLoadingType == 'DB':
        AssetSelectConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
        AssetSelectCur = AssetSelectConn.cursor()
        AssetSelectQ = """
            select 
                computer_id,
                disk_total_space,
                asset_collection_date
            from
                """+AssetTNM+"""
            where 
                to_char(asset_collection_date, 'YYYY-MM-DD HH24:MI:SS') > '"""+yesterday+""" 23:58:59'
            and 
                to_char(asset_collection_date, 'YYYY-MM-DD HH24:MI:SS') <= '"""+day+""" 23:58:59'
            order by computer_id desc
            
        """
        AssetSelectCur.execute(AssetSelectQ)
        AssetSelectRS = AssetSelectCur.fetchall()
        for AssetSelectR in AssetSelectRS:
            AssetSelectL.append(AssetSelectR)
        #print(AssetSelectL)
        return AssetSelectL

def StatisticsYesterday() :
    try:
        StatisticsSelectL = []
        if DataLoadingType == 'DB':
            StatisticsSelectConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            StatisticsSelectCur = StatisticsSelectConn.cursor()
            StatisticsSelectQ = """ 
                select 
                    classification,
                    item, 
                    item_count, 
                    statistics_collection_date
                from 
                    """+StatisticsTNM+""" 
                where 
                    to_char(statistics_collection_date, 'YYYY-MM-DD') = '"""+yesterday+"""' 
                
                """

            StatisticsSelectCur.execute(StatisticsSelectQ)
            StatisticsSelectRS=StatisticsSelectCur.fetchall()
            for StatisticsSelectR in StatisticsSelectRS :
                StatisticsSelectL.append(StatisticsSelectR)
        elif DataLoadingType == 'FILE':
            """AS = BS['asset']
            Storage = AS['Storage']
            FNM = AS['FileName'] + yesterday
            FT = AS['FileType']
            FileFullName = FNM + FT
            with open(Storage + FileFullName, encoding="UTF-8") as ADF:
                ADL = json.loads(ADF.read())
            AssetSelectL=ADL
            """
            #print(DataLoadingType)
        return StatisticsSelectL
    except :
        if DataLoadingType == 'DB':
            print('Statistics Daily Table connection(Select) Failure')
        elif DataLoadingType == 'FILE':
            print('Statistics Daily File(Read) Failure')

def StatisticsFiveDay() :
    try:
        StatisticsSelectL = []
        if DataLoadingType == 'DB':
            StatisticsSelectConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
            StatisticsSelectCur = StatisticsSelectConn.cursor()
            StatisticsSelectQ = """ 
                select 
                    classification,
                    item, 
                    item_count, 
                    statistics_collection_date
                from 
                    """ + StatisticsTNM + """ 
                where 
                    to_char(statistics_collection_date, 'YYYY-MM-DD') > '""" + fiveDay + """' 
                and
                    classification = 'asset'
                """

            StatisticsSelectCur.execute(StatisticsSelectQ)
            StatisticsSelectRS = StatisticsSelectCur.fetchall()
            for StatisticsSelectR in StatisticsSelectRS:
                StatisticsSelectL.append(StatisticsSelectR)
        elif DataLoadingType == 'FILE':
            """AS = BS['asset']
            Storage = AS['Storage']
            FNM = AS['FileName'] + yesterday
            FT = AS['FileType']
            FileFullName = FNM + FT
            with open(Storage + FileFullName, encoding="UTF-8") as ADF:
                ADL = json.loads(ADF.read())
            AssetSelectL=ADL
            """
            print(DataLoadingType)
        #print(StatisticsSelectL)
        return StatisticsSelectL
    except:
        if DataLoadingType == 'DB':
            print('Statistics Daily Table connection(Five Day Select) Failure')
        elif DataLoadingType == 'FILE':
            print('Statistics Daily File(Five Day Read) Failure')

