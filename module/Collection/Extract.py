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
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")

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
                #print(StatisticsSelectR)
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
        return StatisticsSelectL
    except :
        if DataLoadingType == 'DB':
            print('Statistics Daily Table connection(Select) Failure')
        elif DataLoadingType == 'FILE':
            print('Statistics Daily File(Read) Failure')
