import pymysql

try:
    # 데이터베이스 연결
    con = pymysql.connect(host='127.0.0.1', user='root', 
                          passwd= '110499', db='pythonExample', 
                          charset='utf8')

    print(con)
    
    cursor = con.cursor()
    
    # filename = './Python/0920/cat.jpeg'
    
    # f = open(filename, 'rb')
    # photo = f.read()
    # f.close()
    
    # cursor.execute("Insert into blobtable values(%s, %s, %s)", args=('cat', filename, photo))
    # con.commit()
    
    cursor.execute("Select * from blobtable")
    
    datas = cursor.fetchall()
    
    for data in datas:
        f = open(data[1], 'wb')
        f.write(data[2])
        f.close()
        
    
except Exception as e:
    print(f"Error: {e}")
    
finally:
    con.close()
    