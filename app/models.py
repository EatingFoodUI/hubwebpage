# encoding=utf8

from flask_login import UserMixin
from . import db
from . import app
import datetime


# 用户
class User(UserMixin, db.Model):
    __tablename__ = 'hubuser'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(20), unique=True)
    # 问题:使用falsk migrate等导入数据库的定义与实际不符
    password = db.Column(db.String(20))
    # 用户权限的问题
    authority = db.Column(db.String(4))
    # 用户上一次登录时间(细化到分？)
    logintime = db.Column(db.Date)

    def __init__(self, username, password, account, authority):
        self.username = username
        self.password = password
        self.account = account
        self.authority = None

    def __repr__(self):
        return '<User %r>' % self.username


# 实验室成员
class Member(db.Model):
    __tablename__ = 'member'
    # 成员id
    memberNo = db.Column(db.Integer, primary_key=True)
    # 成员姓名
    memberName = db.Column(db.String(5), unique=True)
    # 成员学院
    academy = db.Column(db.String(10))
    # 成员方向
    direction = db.Column(db.String(10))
    # 学会的语言
    language = db.Column(db.String(40))
    # 学会的软件
    software = db.Column(db.String(40))
    # 个人经历
    experience = db.Column(db.String(150))

    def show_all_member_to_json(self):
        json_proEssay = {
            'id': self.memberNo,
            'name': self.memberName,
            'college': self.academy,
            'direction': self.direction
        }
        return json_proEssay

    def show_one_member_to_json(self):
        json_proEssay = {
            'name': self.memberName,
            'college': self.academy,
            'direction': self.direction,
            'skill': {
                'language': self.language,
                'software': self.software
            },
            'experience': self.experience
        }
        return json_proEssay

    def __repr__(self):
        return '<Member %r>' % self.memberName


# 项目文章是总共放在一起还是每个项目的文章分别放置一个独立的序号
# 项目文章
class ProjectEssay(db.Model):
    __tablename__ = 'ProjectEssay'
    # 项目文章id
    pro_essayNo = db.Column(db.Integer, primary_key=True)
    # 项目文章标题
    pro_title = db.Column(db.String(10))
    # 项目文章正文
    pro_content = db.Column(db.Text)
    # 项目文章上传时间
    pro_updateTime = db.Column(db.Date)
    # 项目文章作者
    pro_author = db.Column(db.String(4))
    # 文章分类：项目
    pro_type = db.Column(db.String(10))
    # 项目id（外键）
    projectNo = db.Column(db.Integer, db.ForeignKey('Project.projectNo'))
    # 文章简介
    pro_EssayTit = db.Column(db.String(20))

    Project = db.relationship('Project', backref=db.backref('ProjectEsssay'))

    # 项目页显示文章
    def proEssay_to_json(self):
        json_proEssay = {
            'title': self.pro_title,
            'content': self.pro_content,
            'id': self.pro_essayNo,
            'type': self.pro_type,
            'EssayTit': self.pro_EssayTit
        }
        return json_proEssay

    # 编辑项目文章
    def edit_proEssay_to_json(self):
        json_proEssay = {
            'type': self.pro_type,
            'id': self.pro_essayNo,
            'title': self.pro_title,
            'content': self.pro_content,
            'EssayTit': self.pro_EssayTit
        }
        return json_proEssay

    def __repr__(self):
        return '<Essay %r>' % self.title


# 所有文章
class Essay(db.Model):
    __tablename__ = 'Essay'
    # 文章id
    essayNo = db.Column(db.Integer, primary_key=True)
    # 文章标题
    title = db.Column(db.String(16), unique=True)
    # 文章正文
    content = db.Column(db.Text)
    # 文章上传时间
    updatetime = db.Column(db.Date)
    # 文章作者
    author = db.Column(db.String(8))

    # 显示文章转json使用
    def ShowEssay_to_json(self):
        Text = str(self.content)
        Text = Text[0:20]
        json_project = {
            'id': self.essayNo,
            'title': self.title,
            'content': Text
        }
        return json_project
    
    def __repr__(self):
        return '<Essay %r>' % self.title


# 实验室项目
# 有字符集问题
class Project(db.Model):
    __tablename__ = 'Project'
    # 项目id
    projectNo = db.Column(db.Integer, primary_key=True)
    # 项目名称
    projectName = db.Column(db.String(30), unique=True)
    # 项目负责人    
    projectMan = db.Column(db.String(10))
    # 阅览人数
    howmany = db.Column(db.Integer, default=0)
    # 项目时间 2018-7-26 
    # 修改datatime
    time = db.Column(db.Date, default=datetime.date.today())

    # 项目主页转json使用
    def ProjectPage_need_to_json(self):
        json_project = {
            'projectName': self.projectName,
            'projectMan': self.projectMan,
            'howmany': self.howmany,
            'time': str(self.time),
            'Projectid': self.projectNo
        }
        return json_project

    def __repr__(self):
        return '<Project %r>' % self.projectName

