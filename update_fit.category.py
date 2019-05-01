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

# 1. get { Category.Name : ID }
mycursor.execute("SELECT * FROM blog_fitcategorys")
catIdNames = mycursor.fetchall()
fullLen = len(catIdNames)
for i in range(fullLen):
	row = catIdNames[i]
	catId = row[0]
	catName = row[1]
	# print("catId = %s" % row[0]) # test only
	# print("catName = %s" % row[1])
	# 2. use { Category.Name : ID } to update CategoryID_id in FitDefault
	sqlFormula = "UPDATE blog_fitDefault SET CategoryID_id = %s WHERE Category = %s"
	mycursor.execute(sqlFormula, (catId, catName))
	print("%s / %s" % (i, fullLen))


print("--> finished, close db cursor.")
mycursor.close()

print("--> commit to db...")
mydb.commit()
mydb.close()
print("--> close db.")


