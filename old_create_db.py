import pymysql
from flask_login import UserMixin


db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='4612378',
    charset='utf8',
    db='hubdata'
)

cur = db.cursor()
try:
    sql1 = """drop table if exists hubuser"""

    sql2 = """CREATE TABLE hubuser (
        id int not null auto_increment,
        account varchar(20) not null, 
        username varchar(20) not null,
        password varchar(20) not null,
        authority varchar(4) not null,
        primary key (id)
    )"""

    sql3 = """CREATE TABLE member (
        memberNo tinyint not null auto_increment,
        memberName varchar(4) not null,
        academy varchar(10) not null,
        direction varchar(10) not null,
        primary key (memberNo)
    )"""

    sql4 = """CREATE TABLE essay(
        essayNo int not null auto_increment,
        title varchar(20) not null,
        author varchar(20) not null,
        body text,
        updatetime DATATIME not null
        primary key (essayNo)
        foreign key(author) references hubuser(username)
        )"""

    sql5 = """CREATE TABLE project(
        projectNo int not null auto_increment,
        projectName varchar(20) not null,
        projectleader varchar(4) not null,
        viewSum int,
        projectDate DATE,
        primary key(projectNo)
        foreign key(projectleader) references hubuser(username)
        )"""

    # cur.execute(sql1)
    db.commit()
except Exception:
    db.rollback()

db.close()

class User(UserMixin, object):
    # 构造函数
    def __init__(self, username):
        self.username = username
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            charset='utf8',
            db='hubdata'
        )
        self.id = self.get_id(username)
        self.cur = self.connect.cursor()
        self.passwd = self.get_password(username)

    # 析构函数
    def __del__(self):
        self.cur.close()
        self.connect.close()

    # 获取密码
    def get_password(self, username):
        sql = "select password from hubuser where username ='" + username + "'"
        self.cur.execute(sql)
        password = self.cur.fetchone()
        if password:
            return password[0]
        else:
            return 0

    # 获取ID
    def get_id(self, username):
        sql = "select id from hubuser where username='" + username + "'"
        self.cur.execute(sql)
        id = self.cur.fetchone()
        if id:
            return id[0]
        else:
            return "无此用户的id"

    # 获取账号
    def get_account(self, username):
        sql = "select account from hubuser where username='" + username + "'"
        self.cur.execute(sql)
        id = self.cur.fetchone()
        if id:
            return id[0]
        else:
            return "无此用户的账号"

    # 验证注册用户名是否重复
    def varify_username(self, username):
        sql = "select username from hubuser where username='" + username + "'"
        self.cur.execute(sql)
        username = self.cur.fetchone()
        if username:
            return False
        else:
            return True

    # 验证账号是否重复
    def varify_account(self, username):
        sql = "select account from hubuser where username='" + username + "'"
        self.cur.execute(sql)
        account = self.cur.fetchone()
        if account:
            return False
        else:
            return True

    # 验证密码
    def varify_password(self, password):
        if self.passwd is None:
            return False
        elif self.passwd == password:
            return True
        else:
            return False

    # 添加用户
    def add_user(self, uname, paword):
        try:
            sql = "insert into userhub(username,password) values('" + \
                uname + "'," + paword + ")"
            self.cur.execute(sql)
            self.connect.commit()
            return True
        except Exception:
            self.connect.rollback()
            return False

    # 获取用户
    @staticmethod
    def get(self, userid):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            charset='utf8',
            db='hubdata'
        )
        sql = "select username from hubuser where account='" + userid + "'"
        self.cur.execute(sql)
        username = self.cur.fetchone()
        return User(username)

