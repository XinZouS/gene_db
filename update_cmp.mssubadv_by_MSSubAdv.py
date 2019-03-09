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
mycursor.execute("SELECT * FROM blog_MSSubAdvs")
idName = mycursor.fetchall()
for row in idName:
	id = row[0]
	name = row[1]
	# print("catId = %s" % row[0]) # test only
	# print("catName = %s" % row[1])
	
	# 2. use { MSCat_Name : ID } to update MSCatDbID_id in Company
	sqlFormula = "UPDATE blog_company SET MSSubAdvId_id = %s WHERE MSSubAdv = %s"
	mycursor.execute(sqlFormula, (id, name))



print("--> finished, close db cursor.")
mycursor.close()

print("--> commit to db...")
mydb.commit()
mydb.close()
print("--> close db.")


