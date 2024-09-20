import pymysql

try:
    # 데이터베이스 연결
    con = pymysql.connect(host='127.0.0.1', user='root', 
                          passwd= '110499', db='pythonExample', 
                          charset='utf8')

    print(con)
    
    # sql 실행 객체
    cursor = con.cursor()
    
    # sql문을 사용할 때 직접 값을 매핑하는 구조는 추천하지 않는다.
    # 이와 같이 사용하면 sql injection에 취약하다.
    #cursor.execute("Insert into usertbl value('Alice', 'David', 19700507, 'Seoul', '01012345678', '2024-09-20')")
    
    # tuple을 사용하여 값 매핑
    #cursor.execute("Insert into usertbl value(%s, %s, %s, %s, %s, %s)",('Queen', 'Yoshi', 19700507, 'Seoul', '01012345678', '2024-09-20'))
    
    #print("Insert Success")
    
    # After insert, you have to commit
    # If you don't commit, the data will not be saved.
    # If you want to rollback, you can use con.rollback()
    # When you use pymysql, It is not auto commit.
    #con.commit()
    
    
    # select
    # cursor.execute("select * from usertbl")
    
    # data = cursor.fetchall()
    
    # for row in data:
    #     print(row)
    
    # 프로시저 실행
    # 프로시저를 사용하면 데이터베이스의 정보를 숨길 수 있다.
    cursor.callproc('myproc', args = ('momo', 'momody', 1996, 'Koyto', '01012345678', '2024-09-20'))
    
    con.commit()

except Exception as e:
    print(f"Error: {e}")
    
finally:
    con.close()
    