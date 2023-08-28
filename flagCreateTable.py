from connectDB import conn, cur

sql = "create table flag ("
col1 = "no int, 국가코드 char(2), img mediumblob,"
col2 = "primary key(국가코드),"
col3 = "foreign key(국가코드) references worldPopulation(국가코드))"
op = "default charset=utf8"

sql = sql + col1 + col2 + col3 + op

cur.execute(sql)
conn.commit()
conn.close()
