import psycopg2
from configparser import ConfigParser

def db_connection():
    parser = ConfigParser()
    parser.read('database.ini')
    db = parser['postgresql']  
    
    
    conn = psycopg2.connect(
        host=db['host'],
        database=db['database'],
        user=db['user'],
        password=db['password'],
        port=db.get('port', 5432)  
    )
    return conn

conn = db_connection()
cur = conn.cursor()
cur.execute("""SELECT station.stat_name, station.breite, station.laenge, messwerte_teststation_dd.txk FROM wetter_fue.messwerte_teststation_dd
                JOIN wetter_fue.station on messwerte_teststation_dd.stations_id = station.stations_id
                WHERE messwerte_teststation_dd.mess_datum = '1900-01-01';  """)
rows = cur.fetchall()

cur.close()
conn.close()

print (rows)