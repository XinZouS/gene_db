import mysql.connector
import os
import db_config


dbpw = os.environ.get('GENE_DB_PASSWORD')
dbna = os.environ.get('GENE_DB_NAME')
print(dbpw)
print(dbna)


mydb = mysql.connector.connect(
	host=db_config.local_host,
	user=db_config.user,
	passwd=db_config.passwd,
	database=db_config.database	
	)

mycursor = mydb.cursor()


sql = """
CREATE TABLE perf_gross (
Name varchar(100),
SecId varchar(10),
Category varchar(50),
GTR201809 Numeric(15,10),
GTR201808 Numeric(15,10),
GTR201807 Numeric(15,10),
GTR201806 Numeric(15,10),
GTR201805 Numeric(15,10),
GTR201804 Numeric(15,10),
GTR201803 Numeric(15,10),
GTR201802 Numeric(15,10),
GTR201801 Numeric(15,10),
GTR201712 Numeric(15,10),
GTR201711 Numeric(15,10),
GTR201710 Numeric(15,10),
GTR201709 Numeric(15,10),
GTR201708 Numeric(15,10),
GTR201707 Numeric(15,10),
GTR201706 Numeric(15,10),
GTR201705 Numeric(15,10),
GTR201704 Numeric(15,10),
GTR201703 Numeric(15,10),
GTR201702 Numeric(15,10),
GTR201701 Numeric(15,10),
GTR201612 Numeric(15,10),
GTR201611 Numeric(15,10),
GTR201610 Numeric(15,10),
GTR201609 Numeric(15,10),
GTR201608 Numeric(15,10),
GTR201607 Numeric(15,10),
GTR201606 Numeric(15,10),
GTR201605 Numeric(15,10),
GTR201604 Numeric(15,10),
GTR201603 Numeric(15,10),
GTR201602 Numeric(15,10),
GTR201601 Numeric(15,10),
GTR201512 Numeric(15,10),
GTR201511 Numeric(15,10),
GTR201510 Numeric(15,10),
GTR201509 Numeric(15,10),
GTR201508 Numeric(15,10),
GTR201507 Numeric(15,10),
GTR201506 Numeric(15,10),
GTR201505 Numeric(15,10),
GTR201504 Numeric(15,10),
GTR201503 Numeric(15,10),
GTR201502 Numeric(15,10),
GTR201501 Numeric(15,10),
GTR201412 Numeric(15,10),
GTR201411 Numeric(15,10),
GTR201410 Numeric(15,10),
GTR201409 Numeric(15,10),
GTR201408 Numeric(15,10),
GTR201407 Numeric(15,10),
GTR201406 Numeric(15,10),
GTR201405 Numeric(15,10),
GTR201404 Numeric(15,10),
GTR201403 Numeric(15,10),
GTR201402 Numeric(15,10),
GTR201401 Numeric(15,10),
GTR201312 Numeric(15,10),
GTR201311 Numeric(15,10),
GTR201310 Numeric(15,10),
GTR201309 Numeric(15,10),
GTR201308 Numeric(15,10),
GTR201307 Numeric(15,10),
GTR201306 Numeric(15,10),
GTR201305 Numeric(15,10),
GTR201304 Numeric(15,10),
GTR201303 Numeric(15,10),
GTR201302 Numeric(15,10),
GTR201301 Numeric(15,10),
GTR201212 Numeric(15,10),
GTR201211 Numeric(15,10),
GTR201210 Numeric(15,10),
GTR201209 Numeric(15,10),
GTR201208 Numeric(15,10),
GTR201207 Numeric(15,10),
GTR201206 Numeric(15,10),
GTR201205 Numeric(15,10),
GTR201204 Numeric(15,10),
GTR201203 Numeric(15,10),
GTR201202 Numeric(15,10),
GTR201201 Numeric(15,10),
GTR201112 Numeric(15,10),
GTR201111 Numeric(15,10),
GTR201110 Numeric(15,10),
GTR201109 Numeric(15,10),
GTR201108 Numeric(15,10),
GTR201107 Numeric(15,10),
GTR201106 Numeric(15,10),
GTR201105 Numeric(15,10),
GTR201104 Numeric(15,10),
GTR201103 Numeric(15,10),
GTR201102 Numeric(15,10),
GTR201101 Numeric(15,10),
GTR201012 Numeric(15,10),
GTR201011 Numeric(15,10),
GTR201010 Numeric(15,10),
GTR201009 Numeric(15,10),
GTR201008 Numeric(15,10),
GTR201007 Numeric(15,10),
GTR201006 Numeric(15,10),
GTR201005 Numeric(15,10),
GTR201004 Numeric(15,10),
GTR201003 Numeric(15,10),
GTR201002 Numeric(15,10),
GTR201001 Numeric(15,10),
GTR200912 Numeric(15,10),
GTR200911 Numeric(15,10),
GTR200910 Numeric(15,10),
GTR200909 Numeric(15,10),
GTR200908 Numeric(15,10),
GTR200907 Numeric(15,10),
GTR200906 Numeric(15,10),
GTR200905 Numeric(15,10),
GTR200904 Numeric(15,10),
GTR200903 Numeric(15,10),
GTR200902 Numeric(15,10),
GTR200901 Numeric(15,10),
GTR200812 Numeric(15,10),
GTR200811 Numeric(15,10),
GTR200810 Numeric(15,10),
GTR200809 Numeric(15,10),
GTR200808 Numeric(15,10),
GTR200807 Numeric(15,10),
GTR200806 Numeric(15,10),
GTR200805 Numeric(15,10),
GTR200804 Numeric(15,10),
GTR200803 Numeric(15,10),
GTR200802 Numeric(15,10),
GTR200801 Numeric(15,10),
GTR200712 Numeric(15,10),
GTR200711 Numeric(15,10),
GTR200710 Numeric(15,10),
GTR200709 Numeric(15,10),
GTR200708 Numeric(15,10),
GTR200707 Numeric(15,10),
GTR200706 Numeric(15,10),
GTR200705 Numeric(15,10),
GTR200704 Numeric(15,10),
GTR200703 Numeric(15,10),
GTR200702 Numeric(15,10),
GTR200701 Numeric(15,10),
GTR200612 Numeric(15,10),
GTR200611 Numeric(15,10),
GTR200610 Numeric(15,10),
GTR200609 Numeric(15,10),
GTR200608 Numeric(15,10),
GTR200607 Numeric(15,10),
GTR200606 Numeric(15,10),
GTR200605 Numeric(15,10),
GTR200604 Numeric(15,10),
GTR200603 Numeric(15,10),
GTR200602 Numeric(15,10),
GTR200601 Numeric(15,10),
GTR200512 Numeric(15,10),
GTR200511 Numeric(15,10),
GTR200510 Numeric(15,10),
GTR200509 Numeric(15,10),
GTR200508 Numeric(15,10),
GTR200507 Numeric(15,10),
GTR200506 Numeric(15,10),
GTR200505 Numeric(15,10),
GTR200504 Numeric(15,10),
GTR200503 Numeric(15,10),
GTR200502 Numeric(15,10),
GTR200501 Numeric(15,10),
GTR200412 Numeric(15,10),
GTR200411 Numeric(15,10),
GTR200410 Numeric(15,10),
GTR200409 Numeric(15,10),
GTR200408 Numeric(15,10),
GTR200407 Numeric(15,10),
GTR200406 Numeric(15,10),
GTR200405 Numeric(15,10),
GTR200404 Numeric(15,10),
GTR200403 Numeric(15,10),
GTR200402 Numeric(15,10),
GTR200401 Numeric(15,10),
GTR200312 Numeric(15,10),
GTR200311 Numeric(15,10),
GTR200310 Numeric(15,10),
GTR200309 Numeric(15,10),
GTR200308 Numeric(15,10),
GTR200307 Numeric(15,10),
GTR200306 Numeric(15,10),
GTR200305 Numeric(15,10),
GTR200304 Numeric(15,10),
GTR200303 Numeric(15,10),
GTR200302 Numeric(15,10),
GTR200301 Numeric(15,10),
GTR200212 Numeric(15,10),
GTR200211 Numeric(15,10),
GTR200210 Numeric(15,10),
GTR200209 Numeric(15,10),
GTR200208 Numeric(15,10),
GTR200207 Numeric(15,10),
GTR200206 Numeric(15,10),
GTR200205 Numeric(15,10),
GTR200204 Numeric(15,10),
GTR200203 Numeric(15,10),
GTR200202 Numeric(15,10),
GTR200201 Numeric(15,10),
GTR200112 Numeric(15,10),
GTR200111 Numeric(15,10),
GTR200110 Numeric(15,10),
GTR200109 Numeric(15,10),
GTR200108 Numeric(15,10),
GTR200107 Numeric(15,10),
GTR200106 Numeric(15,10),
GTR200105 Numeric(15,10),
GTR200104 Numeric(15,10),
GTR200103 Numeric(15,10),
GTR200102 Numeric(15,10),
GTR200101 Numeric(15,10),
GTR200012 Numeric(15,10),
GTR200011 Numeric(15,10),
GTR200010 Numeric(15,10),
GTR200009 Numeric(15,10),
GTR200008 Numeric(15,10),
GTR200007 Numeric(15,10),
GTR200006 Numeric(15,10),
GTR200005 Numeric(15,10),
GTR200004 Numeric(15,10),
GTR200003 Numeric(15,10),
GTR200002 Numeric(15,10),
GTR200001 Numeric(15,10),
GTR199912 Numeric(15,10),
GTR199911 Numeric(15,10),
GTR199910 Numeric(15,10),
GTR199909 Numeric(15,10),
GTR199908 Numeric(15,10),
GTR199907 Numeric(15,10),
GTR199906 Numeric(15,10),
GTR199905 Numeric(15,10),
GTR199904 Numeric(15,10),
GTR199903 Numeric(15,10),
GTR199902 Numeric(15,10),
GTR199901 Numeric(15,10),
GTR199812 Numeric(15,10),
GTR199811 Numeric(15,10),
GTR199810 Numeric(15,10),
GTR199809 Numeric(15,10),
GTR199808 Numeric(15,10),
GTR199807 Numeric(15,10),
GTR199806 Numeric(15,10),
GTR199805 Numeric(15,10),
GTR199804 Numeric(15,10),
GTR199803 Numeric(15,10),
GTR199802 Numeric(15,10),
GTR199801 Numeric(15,10),
GTR199712 Numeric(15,10),
GTR199711 Numeric(15,10),
GTR199710 Numeric(15,10),
GTR199709 Numeric(15,10),
GTR199708 Numeric(15,10),
GTR199707 Numeric(15,10),
GTR199706 Numeric(15,10),
GTR199705 Numeric(15,10),
GTR199704 Numeric(15,10),
GTR199703 Numeric(15,10),
GTR199702 Numeric(15,10),
GTR199701 Numeric(15,10),
GTR199612 Numeric(15,10),
GTR199611 Numeric(15,10),
GTR199610 Numeric(15,10),
GTR199609 Numeric(15,10),
GTR199608 Numeric(15,10),
GTR199607 Numeric(15,10),
GTR199606 Numeric(15,10),
GTR199605 Numeric(15,10),
GTR199604 Numeric(15,10),
GTR199603 Numeric(15,10),
GTR199602 Numeric(15,10),
GTR199601 Numeric(15,10),
GTR199512 Numeric(15,10),
GTR199511 Numeric(15,10),
GTR199510 Numeric(15,10),
GTR199509 Numeric(15,10),
GTR199508 Numeric(15,10),
GTR199507 Numeric(15,10),
GTR199506 Numeric(15,10),
GTR199505 Numeric(15,10),
GTR199504 Numeric(15,10),
GTR199503 Numeric(15,10),
GTR199502 Numeric(15,10),
GTR199501 Numeric(15,10),
GTR199412 Numeric(15,10),
GTR199411 Numeric(15,10),
GTR199410 Numeric(15,10),
GTR199409 Numeric(15,10),
GTR199408 Numeric(15,10),
GTR199407 Numeric(15,10),
GTR199406 Numeric(15,10)
)"""
mycursor.execute(sql)


mydb.commit()
mydb.close()