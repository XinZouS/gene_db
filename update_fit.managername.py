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

# 1. get { ManagerName.Name : ID }
mycursor.execute("SELECT * FROM research_managernames")
mIdNames = mycursor.fetchall()
fullLen = len(mIdNames)
for i in range(fullLen):
	row = mIdNames[i]
	mId = row[0]
	mName = row[1]
	# print("mId = %s" % row[0]) # test only
	# print("mName = %s" % row[1])
	# 2. use { ManagerName.Name : ID } to update CategoryID_id in FitDefault
	sqlFormula = "UPDATE research_fitDefault SET ManagerNameID_id = %s WHERE ManagerName = %s"
	mycursor.execute(sqlFormula, (mId, mName))
	print("%s / %s" % (i, fullLen))


print("--> finished, close db cursor.")
mycursor.close()

print("--> commit to db...")
mydb.commit()
mydb.close()
print("--> close db.")


