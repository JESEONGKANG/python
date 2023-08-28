from connectDB import conn, cur

sql = "create table worldPopulation ("
column1 = "순번 int,"
column2 = "국가코드 char(2) primary key,"
column3 = "국가 varchar(50),"
column4 = "수도 varchar(50),"
column5 = "인구 float)"
option = "default charset=utf8"
sql = sql + column1 + column2 + column3 + \
      column4 + column5 + option
print(sql)

cur.execute(sql)
conn.commit()
conn.close()
