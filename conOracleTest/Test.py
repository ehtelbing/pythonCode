import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def fun1():
    from conOracleTest.OracleDB import OracleDB
    oracle1 = OracleDB()

    rs = None
    ret_sum_amount = 0
    ret_sum_money = 0
    proName = 'pg_mm_share.getSMKCTable'
    parVals = ['%', '%', '%', '%', '%', '', '', 0, 10, '%', '%', ret_sum_amount, ret_sum_money, rs]
    parTypes = ['string', 'string', 'string', 'string', 'string', 'string', 'string', 'number', 'number', 'string', 'string', 'number', 'number', 'cursor']
    parDirTypes = ['in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'out', 'out', 'out']
    result = oracle1.executeProcedure(proName, parVals, parTypes, parDirTypes)

    f = open('F:\\out.log', 'w')
    f.writelines(str(result[0]))
    f.writelines(str(result[1]))
    for row in result[2]:
        f.writelines(row['source_plantcode']+','+row['source_plantname']+'\n')
    f.writelines(str(result[3]))
    f.close()


def main():
    print('执行main函数')
    fun1()


if __name__ == '__main__':
    main()







