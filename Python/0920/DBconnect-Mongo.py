from pymongo import MongoClient

try:
    # 데이터베이스 연결
    conn = MongoClient('127.0.0.1')

    # 데이터베이스 설정
    db = conn.mymongo

    # 컬렉션 설정
    collection = db.uesrs

    # document 생성 : {key:value}
    # doc1 = {'empno': '10001', 'name': '홍길동', 'phone': '010-1234-5678', 'age': 25}
    # doc2 = {'empno': '10002', 'name': '김철수', 'phone': '010-1234-5679', 'age': 30}
    # doc3 = {'empno': '10003', 'name': '이영희', 'phone': '010-1234-5680', 'age': 35}
    # doc4 = {'empno': '10004', 'name': '박민수', 'phone': '010-1234-5681', 'age': 40}
    
    # collection.insert_one(doc1)
    # collection.insert_many([doc2, doc3, doc4])
    
    # document 조회
    # python과 node에서는 mongodb연동을 할 떄 동일한 함수 사용
    
    result = collection.find()
    
    for data in result:
        print(data)
    
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")