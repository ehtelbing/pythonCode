import cx_Oracle
import configparser


#读取ini配置文件
config=configparser.ConfigParser();
config.read('../configs/db.ini')
username=config.get('database','username')
psd=config.get('database','password')
url=config.get('database','url')
sid=config.get('database','sid')
port=config.get('database','port')


def getConnOracle(): #获取数据库连接
    # conn=cx_Oracle.connect('pmnew','pmnew','10.101.2.47/ora12c')
    # conn=cx_Oracle.connect(username,psd,url+'/'+sid)
    dsn=cx_Oracle.makedsn(url,port,sid)
    conn=cx_Oracle.connect(username,psd,dsn)
    return conn



# 查看cx_Oracke 版本
print("cx_Oracle.version:", cx_Oracle.version)