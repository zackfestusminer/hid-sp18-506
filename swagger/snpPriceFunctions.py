import pymysql
import config

connection = pymysql.connect(host=config.host,
                             user=config.user,
                             password=config.password,
                             db=config.db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

def snp_query_all():
    sql = "SELECT Date,Open,High,Low,Close,AdjClose,Volume FROM SNP_PRICE_DETAILS"
    cursor.execute(sql)
    resultSet = cursor.fetchall()
    return resultSet

def snp_query_by_date(snpDate):
    sql = "SELECT Date,Open,High,Low,Close,AdjClose,Volume FROM SNP_PRICE_DETAILS WHERE Date =%s"
    cursor.execute(sql, (snpDate))
    resultSet = cursor.fetchall()
    return resultSet

def snp_insert(snpInsert):
    sql = "INSERT INTO SNP_PRICE_DETAILS(Date,Open,High,Low,Close,AdjClose,Volume) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    resultSet = cursor.execute(sql, (snpInsert['snpDate'], snpInsert['open'], snpInsert['high'], snpInsert
                        ['low'], snpInsert['close'], snpInsert['adjClose'], snpInsert['volume'] ))
    connection.commit()
    return resultSet

def snp_delete(snpDate):
    sql = 'DELETE FROM SNP_PRICE_DETAILS WHERE Date = %s'
    resultSet = cursor.execute(sql, (snpDate))
    connection.commit()
    return resultSet

def snp_update(snpDate, snpUpdate):
    sql = "UPDATE SNP_PRICE_DETAILS SET Open = %s, High = %s, Low = %s, Close = %s, AdjClose=%s, Volume=%s WHERE Date = %s"
    resultSet = cursor.execute(sql, (snpUpdate['open'], snpUpdate['high'], snpUpdate
                        ['low'], snpUpdate['close'], snpUpdate['adjClose'], snpUpdate['volume'], snpDate))
    connection.commit()
    return resultSet

