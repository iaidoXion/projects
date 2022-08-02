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
BS = SETTING['FILE']
today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
day = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
twoago = (datetime.today() - timedelta(2)).strftime("%Y-%m-%d")
fiveDay = (datetime.today() - timedelta(5)).strftime("%Y-%m-%d")

def past_data() :
    AssetSelectL = []
    if DataLoadingType == 'DB':
        AssetSelectConn = psycopg2.connect('host={0} dbname={1} user={2} password={3}'.format(DBHost, DBName, DBUser, DBPwd))
        AssetSelectCur = AssetSelectConn.cursor()
        AssetSelectQ = """
            select 
                computer_id,
                disk_used_space,
                listen_port_count,
                established_port_count,
                ram_use_size,
                asset_collection_date
            from
                """+AssetTNM+"""
            where 
                to_char(asset_collection_date, 'YYYY-MM-DD') = '"""+yesterday+"""'
            order by computer_id desc
            
        """
        AssetSelectCur.execute(AssetSelectQ)
        AssetSelectRS = AssetSelectCur.fetchall()
        for AssetSelectR in AssetSelectRS:
            AssetSelectL.append(AssetSelectR)
        #print(AssetSelectL)
        return AssetSelectL
