import mysql.connector
import db_config

# if get error, try: 
# pip install mysql-connector-python

mydb = mysql.connector.connect(
	host=db_config.local_host,
	user=db_config.user,
	passwd=db_config.passwd,
	database=db_config.database	
	)

mycursor = mydb.cursor()

# 1. get { Advisor_Name : ID }
mycursor.execute("SELECT * FROM research_Advisors")
advIdNames = mycursor.fetchall()
fullLen = len(advIdNames)
for i in range(fullLen):
	row = advIdNames[i]
	advId = row[0]
	advName = row[1]
	# print("advId = %s" % row[0]) # test only
	# print("advName = %s" % row[1])
	# 2. use { Advisor_Name : ID } to update AdvID_id in FitDefault
	sqlFormula = "UPDATE research_fitDefault SET AdvisorID_id = %s WHERE Advisor = %s"
	mycursor.execute(sqlFormula, (advId, advName))
	print("%s / %s" % (i, fullLen))


print("--> finished, close db cursor.")
mycursor.close()

print("--> commit to db...")
mydb.commit()
mydb.close()
print("--> close db.")


