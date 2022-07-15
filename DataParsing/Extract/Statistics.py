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
StatisticsTNM = SETTING['DB']['StatisticsTNM']
BS = SETTING['FILE']
today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
day = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")
fiveDay = (datetime.today() - timedelta(5)).strftime("%Y-%m-%d")




def Yesterday():
    try:
        StatisticsSelectL = []
        if DataLoadingType == 'DB':
            StatisticsSelectConn = psycopg2.connect(
                'host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
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
                    to_char(statistics_collection_date, 'YYYY-MM-DD') = '""" + yesterday + """' 

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
            # print(DataLoadingType)
        return StatisticsSelectL
    except:
        if DataLoadingType == 'DB':
            print('Statistics Daily Table connection(Select) Failure')
        elif DataLoadingType == 'FILE':
            print('Statistics Daily File(Read) Failure')


def FiveDay(type):
    try:
        StatisticsSelectL = []
        if DataLoadingType == 'DB':
            StatisticsSelectConn = psycopg2.connect(
                'host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
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
                    classification = '"""+type+"""'
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
        # print(StatisticsSelectL)
        return StatisticsSelectL
    except:
        if DataLoadingType == 'DB':
            print('Statistics Daily Table connection(Five Day Select) Failure')
        elif DataLoadingType == 'FILE':
            print('Statistics Daily File(Five Day Read) Failure')

