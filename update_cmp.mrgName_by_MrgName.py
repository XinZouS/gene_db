import mysql.connector
import db_config


mydb = mysql.connector.connect(
	host=db_config.local_host,
	user=db_config.user,
	passwd=db_config.passwd,
	database=db_config.database	
	)

mycursor = mydb.cursor()

# 1. get { Advisor_Name : ID }
mycursor.execute("SELECT * FROM blog_MgrNames")
mgrIdName = mycursor.fetchall()
allCount = len(mgrIdName)
curr = 0
for row in mgrIdName:
	mgrId = row[0]
	mgrName = row[1]
	# print("catId = %s" % row[0]) # test only
	# print("catName = %s" % row[1])
	# 2. use { MSCat_Name : ID } to update MSCatDbID_id in Company
	sqlFormula = "UPDATE blog_company SET MgrNameId_id = %s WHERE MgrName = %s"
	mycursor.execute(sqlFormula, (mgrId, mgrName))
	print("%s / %s" % (curr, allCount) )
	curr += 1


print("--> finished, close db cursor.")
mycursor.close()

print("--> commit to db...")
mydb.commit()
mydb.close()
print("--> close db.")


