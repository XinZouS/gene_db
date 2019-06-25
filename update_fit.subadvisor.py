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

# 1. get { SubAdvisor.Name : ID }
mycursor.execute("SELECT * FROM research_subadvisors")
sbIdNames = mycursor.fetchall()
fullLen = len(sbIdNames)
for i in range(fullLen):
	row = sbIdNames[i]
	sbId = row[0]
	sbName = row[1]
	# print("sbId = %s" % row[0]) # test only
	# print("sbName = %s" % row[1])
	# 2. use { SubAdvisor.Name : ID } to update SubAdvisorID_id in FitDefault
	sqlFormula = "UPDATE research_fitDefault SET SubAdvisorID_id = %s WHERE SubAdvisor = %s"
	mycursor.execute(sqlFormula, (sbId, sbName))
	print("%s / %s" % (i, fullLen))


print("--> finished, close db cursor.")
mycursor.close()

print("--> commit to db...")
mydb.commit()
mydb.close()
print("--> close db.")


