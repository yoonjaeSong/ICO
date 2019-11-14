import db_config as config
import pymysql

# 클래스
class DBConnection:
    conn = None

    # 생성자
    def __init__(self):
        pass    # 함수에서 아무것도 안할 때 사용

    def get_connection(self):
        # 예외처리
        try:
            # database에 접근
            DBConnection.conn = pymysql.connect(host=config.ICO_CONFIG['host'],
                                   user=config.ICO_CONFIG['user'],
                                   password=config.ICO_CONFIG['password'],
                                   db=config.ICO_CONFIG['db'],
                                   charset=config.ICO_CONFIG['charset'])
            # database를 사용하기 위한 cursor를 세팅
#            cursor = conn.cursor()

            return DBConnection.conn

        except Exception as e:
            print(e)

"""
    def close_db(self):
        if DBConnection.conn != None:
            DBConnection.conn.close()

    # 소멸자
    def __del__(self):
        self.close_db()
"""