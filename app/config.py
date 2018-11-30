import os
import datetime

# 配置SQLALCHEMY
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACH_MODIFICATIONS = False
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1/hubpage'
# 迁移数据库使用
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog-dev.sql')

# 配置session
PERMANENT_SESSION_LIFETIME = datetime.timedelta(weeks=7)
