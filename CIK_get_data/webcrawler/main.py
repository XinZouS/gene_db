import mysql.connector # pip install mysql-connector-python
import time
import db_config
import cikIds
import crawler


#=== DB config ======================

mydb = mysql.connector.connect(
	host=db_config.local_host,
	user=db_config.user,
	passwd=db_config.passwd,
	database=db_config.database	
	)

mycursor = mydb.cursor()


def insertCIKs(cikId, cikName):
	colum_names = "CIK, Name"
	sqlFormula = "INSERT INTO CIKs (" + colum_names + ") VALUES (%s, %s)"
	values = (cikId, cikName)
	mycursor.execute(sqlFormula, values)

def insertSeries(cik, series, nameStr):
	colum_names = "CIK, Series, Name"
	sqlFormula = "INSERT INTO CIK_series (" + colum_names + ") VALUES (%s, %s, %s)"
	values = (cik, series, nameStr)
	mycursor.execute(sqlFormula, values)

def insertClass(cik, series, subCatStr, nameStr, ticker):
	colum_names = "CIK, Series, Class, Name, TickerSymbol"
	sqlFormula = "INSERT INTO cik_class (" + colum_names + ") VALUES (%s, %s, %s, %s, %s)"
	values = (cik, series, subCatStr, nameStr, ticker)
	mycursor.execute(sqlFormula, values)


#=== crawler load html ======================

start_time = time.time()
print("--- start loading ... ")

i = 1
for cik in cikIds.ids:
	crawler.loadDataByCikId(cik, insertCIKs, insertSeries, insertClass)
	print('    CIK finished #', i)
	i += 1

print('------ Invalidate CIKs: %s ------' % len(crawler.invalidateCiks))
print(crawler.invalidateCiks)

print("--- finished inserting in: [ %s ] seconds" % (time.time() - start_time))
print("--- close db cursor.")
mycursor.close()

print("--- commit to db...")
mydb.commit()

print("--- close db.")
mydb.close()





