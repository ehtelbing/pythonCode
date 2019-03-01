import cx_Oracle as cx_oracle


class OracleDB:

    def __init__(self):
        print('对象初始化')
        self.db = None
        self.cursor = None

    def getConnection(self):
        return 'namm_ak/namm_ak@10.101.2.201/ora10g'

    def openConnection(self):
        conn = self.getConnection()
        try:
            self.db = cx_oracle.connect(conn)
            print('连接成功')
            return self.db
        except Exception as e:
            print(e)

    def closeConnection(self):
        if self.cursor is not None:
            self.cursor.close()
            print("cursor已关闭")
        if self.db is not None:
            self.db.close()
            print('连接已关闭')

    def executeQuery(self, sql_txt):
        if self.db is None:
            self.openConnection()
        try:
            if self.cursor is None:
                self.cursor = self.db.cursor()
            return self.cursor.execute(sql_txt).fetchall()
        except Exception as e:
            raise Exception(e)
        finally:
            self.closeConnection()

    def executeNonQuery(self,sql_txt):
        if self.db is None:
            self.openConnection()
        try:
            if self.cursor is None:
                self.cursor = self.db.cursor()
            return self.cursor.execute(sql_txt)
        except Exception as e:
            raise Exception(e)
        finally:
            self.closeConnection()

    def executeProcedure(self, pro_name, parVals, parTypes, parDirTypes):
        if self.db is None:
            self.openConnection()
        if len(parVals) == len(parTypes) and len(parTypes) == len(parDirTypes):
            try:
                if self.cursor is None:
                    self.cursor = self.db.cursor()
                for i in range(0, len(parVals)):
                    if parDirTypes[i] == 'in':
                        pass
                    elif parDirTypes[i] == 'out':
                        if parTypes[i] == 'string':
                            parVals[i] == self.cursor.var(cx_oracle.STRING)
                        elif parTypes[i] == 'number':
                            parVals[i] = self.cursor.var(cx_oracle.NUMBER)
                        elif parTypes[i] == 'cursor':
                            parVals[i] = self.cursor.var(cx_oracle.CURSOR)
                rs = self.cursor.callproc(pro_name, parVals)
                result = []
                cursor_count = 0
                for i in range(0, len(parVals)):
                    if parDirTypes[i] == 'out':
                        if parTypes[i] == 'cursor':
                            fieldnames = [d[0].upper() for d in rs[i].description]
                            rows = rs[i].fetchall()
                            cursor_count = len(rows)
                            cList = []
                            for row in rows:
                                dict = {}
                                for j in range(0, len(fieldnames)):
                                    dict[fieldnames[j].lower()] = row[j]
                                    cList.append(dict)
                            result.append(cList)
                        else:
                            result.append(rs[i])
                result.append(cursor_count)
                return result
            except Exception as e:
                raise Exception(e)
            finally:
                self.closeConnection()
        else:
            raise Exception('参数列表数量不一致')

####End Class OracleDB####








