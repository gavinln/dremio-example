'''
Create a file /etc/odbc.ini with these contents

[Data Sources]
Dremio ODBC Driver 64-bit=Dremio ODBC Driver(64-bit)

[Dremio ODBC Driver 64-bit]
Description=Dremio ODBC Driver(64-bit)
Driver=/opt/dremio-odbc/lib64/libdrillodbc_sb64.so
'''

import time

import pyodbc
import pandas

host = '172.30.213.61'
port = 31010
uid = 'gavinln'
pwd = 'dremio-pass1'

dsn = 'Dremio ODBC Driver 64-bit'
# driver = 'Dremio ODBC Driver 64-bit'
# driver = 'Dremio ODBC Driver(64-bit)'

cnxn_str = (
    'DSN={};ConnectionType=Direct;'
    'HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}'.format(
        dsn, host, port, uid, pwd))

cnxn = pyodbc.connect(cnxn_str, autocommit=True)

# sql = '''SELECT * FROM "@gavinln".Incidents'''
sql = '''SELECT count(*) FROM "@gavinln".ny_taxi_1'''

start = time.time()
df = pandas.read_sql(sql, cnxn)
elapsed = time.time() - start

print('Elapsed {}'.format(elapsed))

print(df)

cnxn.close()
