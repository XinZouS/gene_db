import mysql.connector


mydb = mysql.connector.connect(
	host="127.0.0.1",
	user="root",
	passwd="BXY5201314",
	database="gene"
	)

mycursor = mydb.cursor()

# 1. get { Advisor_Name : ID }
mycursor.execute("SELECT * FROM blog_Advisors")
advIdName = mycursor.fetchall()
for row in advIdName:
	advId = row[0]
	advName = row[1]
	# print("advId = %s" % row[0]) # test only
	# print("advName = %s" % row[1])
	# 2. use { Advisor_Name : ID } to update AdvID_id in Company
	sqlFormula = "UPDATE blog_company SET AdvisorID_id = %s WHERE Advisor = %s"
	mycursor.execute(sqlFormula, (advId, advName))



print("--> finished, close db cursor.")
mycursor.close()

print("--> commit to db...")
mydb.commit()
mydb.close()
print("--> close db.")


