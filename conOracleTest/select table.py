import cx_Oracle
import pandas
import sys

from conOracleTest.con_Oracle import getConnOracle


# cursor=cx_Oracle.Cursor(getConnOracle())
conndb=getConnOracle()
conn=cx_Oracle.Cursor(conndb)
print("=====")

# sql="select * from BASE_FILE"
# if True:
#     cursor.execute(sql)
#     for i in cursor:
#         print(i)
#     # dbconn.close()
# print("====")



# sql2="select * from BASE_PERSON"
# if True:
#     dbconn=cursor.execute(sql2)
#     result=cursor.fetchall()
#     print("len(result):",len(result))
#     # print(row)
# print("===============")


try:
    # V_V_DEPTCODE=sys.argv[0]
    # print("",V_V_DEPTCODE)
    in_var='99060206'
    out_cur=conn.var(cx_Oracle.CURSOR)
    arr=conn.callproc('PM_REPAIRDEPT_SEL',[in_var,out_cur])
    result=[]
    result=arr[1].fetchall()
    #多行数据单行输出
    # print(result)
    # for i in
    # 多行数据多行输出
    print(pandas.DataFrame(result))
except Exception as e:
    print('{}',format(e))
finally:
    conn.close()
    print("Exit")
pass


