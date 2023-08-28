from connectDB import conn, cur, pd
url = 'https://raw.githubusercontent.com/kig2929kig/db/main/%EA%B5%AD%EA%B0%80%EB%B3%84%EC%9D%B8%EA%B5%AC%EC%88%9C%EC%9C%84.csv'

df = pd.read_csv(url, encoding='utf8')
#print(df['순번'])
column = zip(df['순번'], df['국가코드'], df['국가'], df['수도'], df['인구'])
for no, code, country, city, pop in column :
    no = int(no)
    code = str(code)
    code = code[:2].upper()
    print(no, code[:2], country, city, pop)
    sql = f'insert into worldPopulation values({no}, "{code}", "{country}", "{city}", {pop})'

    cur.execute(sql)
conn.commit()
conn.close()
