import mysql.connector


mydb = mysql.connector.connect(
	host="127.0.0.1",
	user="root",
	passwd="BXY5201314",
	database="gene"
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


