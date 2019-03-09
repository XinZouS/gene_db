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
mycursor.execute("SELECT * FROM blog_MSCats")
catIdName = mycursor.fetchall()
for row in catIdName:
	catId = row[0]
	catName = row[1]
	# print("catId = %s" % row[0]) # test only
	# print("catName = %s" % row[1])
	# 2. use { MSCat_Name : ID } to update MSCatDbID_id in Company
	sqlFormula = "UPDATE blog_company SET MSCatDbID_id = %s WHERE MSCat = %s"
	mycursor.execute(sqlFormula, (catId, catName))



print("--> finished, close db cursor.")
mycursor.close()

print("--> commit to db...")
mydb.commit()
mydb.close()
print("--> close db.")


