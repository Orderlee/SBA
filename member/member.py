import sqlite3

class Student:
    id: str = ''
    paw: str = ''
    name: str = ''
    birth: str = ''
    regdate: str = ''
    
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.curser = conn.cursor()

class StudentDao:

    def create(self):
        # cursor(커서) : 데이터베이스 작업을 수행하고 있는 메모리 공간
        cursor = self.cursor
        try:
            #excute : sql 구문을 실행해주는 함수
            cursor.execute("drop table students")
        except sqlite3.OperationalError as err:
            print('테이블이 존재하지 않습니다.')

        self.cursor.execute(
            ''' create table students (id text primary key,pwd text, name text, birth text)'''
            
        )
        cursor.commit()

    def insert_one(self,payload):
        # payload = ('lee','이승기','1989/11/11')
        cursor = self.cursor
        sql ="insert into students(id, pwd, name, birth) values ('{student.id}','{student.pwd}','{student.name}','{studnet,birth}')"
        self.cursor.execute(sql)
        self.cursor.commint()

    def insert_many(self):
        data = [('jo','조용필','1985/12/31'),('ko','고아라','1970/07/17'),('sim','심형래','1950/03/22')]
        # ?: placeholder: 치환되어야할 어떤 대상
        # 데이터 유형에 상관없이 외따옴표 적지 마라
        sql="""
        INSERT INTO member(userid, password, phone) VALUES(?,?,?)
        """
        self.conn.executemany(sql,data)
        self.cursor.commit()

    def fetch_by_id(self,id):
        cursor = self.cursor
        findID = 'ko'
        sql = f"select * from students where id = '%{id}'" 
        cursor.execute(sql)
        result = cursor.fetchone() # fetch 해줘야함
        print(type(result)) # 튜플형태로 리턴
        if result != None:
            print('아이디  : ' + result[0], end='')
            print(', 이름 : ' + result[1], end='')
            print(', 생일 : ' + result[2], end='')

        else:
            print('문제가 있습니다.')
        print()
        return result

    def fetch_list(self):
        cursor = self.cursor
        sql = 'select * from students order by name desc'
        for id , name, birth in cursor.execute(sql): # 다중 데이터는 for 문으로 바로 출력가능
            print(id + '#' + name + '#' + birth)
        print('-'*20)

    def fetch_by_name(self, name):
        cursor = self.cursor
        sql = f"select * from students where name like '%{name}%'"
        cursor.execute(sql)
        return cursor.fetchall()

    def fetch_count(self):
        cursor = self.cursor
        sql = f'select count(*) from students'
        cursor = self.cursor.execute(sql)
        rows = cursor.fetchall()
        count = 0 
        for i in rows:
            count += 1
        return count.rowcount

    def fetch_all(self):
        ccursor = self.cursor
        cursor.execute('select * from students')
        return cursor.etchall()

    def login(self,id,pwd):
        cursor = self.cursor
        sql ="""
        select * from students where id like ? and pwd like ?
        """
        data = [id,pwd]
        cursor.execute(sql,data)
        return cursor.fetchone()


    def update(self):
        # 'id'가 'lee'인 친구의 이름을 '이문제소 바꾸세요'
        cursor = self.cursor
        sql = f"update students set name = '{name}' where id ='{id}'"
        cursor.execute(sql)
        print(cursor.rowcount) #성공여부
        self.conn.commit()

    def delete(self):
        # 'id'가 'sim'인 친구의 데이터를 삭제
        cursor = self.cursor
        sql = f"delete from students where id ='%{id}'"
        cursor.execute(sql)
        print(cursor.rowcount)
        self.conn.commit()

        # cursor.close()
        # conn.close() web 상대에서는 close하지 않음

class StudentService:
    pass

class StudentController:
    pass

