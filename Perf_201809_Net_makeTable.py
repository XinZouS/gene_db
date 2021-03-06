import mysql.connector
import db_config


mydb = mysql.connector.connect(
	host=db_config.local_host,
	user=db_config.user,
	passwd=db_config.passwd,
	database=db_config.database	
	)

mycursor = mydb.cursor()


sql = """
CREATE TABLE perf_net (
Name varchar(100),
SecId varchar(10),
Category varchar(50),
TR201809 Numeric(15,10),
TR201808 Numeric(15,10),
TR201807 Numeric(15,10),
TR201806 Numeric(15,10),
TR201805 Numeric(15,10),
TR201804 Numeric(15,10),
TR201803 Numeric(15,10),
TR201802 Numeric(15,10),
TR201801 Numeric(15,10),
TR201712 Numeric(15,10),
TR201711 Numeric(15,10),
TR201710 Numeric(15,10),
TR201709 Numeric(15,10),
TR201708 Numeric(15,10),
TR201707 Numeric(15,10),
TR201706 Numeric(15,10),
TR201705 Numeric(15,10),
TR201704 Numeric(15,10),
TR201703 Numeric(15,10),
TR201702 Numeric(15,10),
TR201701 Numeric(15,10),
TR201612 Numeric(15,10),
TR201611 Numeric(15,10),
TR201610 Numeric(15,10),
TR201609 Numeric(15,10),
TR201608 Numeric(15,10),
TR201607 Numeric(15,10),
TR201606 Numeric(15,10),
TR201605 Numeric(15,10),
TR201604 Numeric(15,10),
TR201603 Numeric(15,10),
TR201602 Numeric(15,10),
TR201601 Numeric(15,10),
TR201512 Numeric(15,10),
TR201511 Numeric(15,10),
TR201510 Numeric(15,10),
TR201509 Numeric(15,10),
TR201508 Numeric(15,10),
TR201507 Numeric(15,10),
TR201506 Numeric(15,10),
TR201505 Numeric(15,10),
TR201504 Numeric(15,10),
TR201503 Numeric(15,10),
TR201502 Numeric(15,10),
TR201501 Numeric(15,10),
TR201412 Numeric(15,10),
TR201411 Numeric(15,10),
TR201410 Numeric(15,10),
TR201409 Numeric(15,10),
TR201408 Numeric(15,10),
TR201407 Numeric(15,10),
TR201406 Numeric(15,10),
TR201405 Numeric(15,10),
TR201404 Numeric(15,10),
TR201403 Numeric(15,10),
TR201402 Numeric(15,10),
TR201401 Numeric(15,10),
TR201312 Numeric(15,10),
TR201311 Numeric(15,10),
TR201310 Numeric(15,10),
TR201309 Numeric(15,10),
TR201308 Numeric(15,10),
TR201307 Numeric(15,10),
TR201306 Numeric(15,10),
TR201305 Numeric(15,10),
TR201304 Numeric(15,10),
TR201303 Numeric(15,10),
TR201302 Numeric(15,10),
TR201301 Numeric(15,10),
TR201212 Numeric(15,10),
TR201211 Numeric(15,10),
TR201210 Numeric(15,10),
TR201209 Numeric(15,10),
TR201208 Numeric(15,10),
TR201207 Numeric(15,10),
TR201206 Numeric(15,10),
TR201205 Numeric(15,10),
TR201204 Numeric(15,10),
TR201203 Numeric(15,10),
TR201202 Numeric(15,10),
TR201201 Numeric(15,10),
TR201112 Numeric(15,10),
TR201111 Numeric(15,10),
TR201110 Numeric(15,10),
TR201109 Numeric(15,10),
TR201108 Numeric(15,10),
TR201107 Numeric(15,10),
TR201106 Numeric(15,10),
TR201105 Numeric(15,10),
TR201104 Numeric(15,10),
TR201103 Numeric(15,10),
TR201102 Numeric(15,10),
TR201101 Numeric(15,10),
TR201012 Numeric(15,10),
TR201011 Numeric(15,10),
TR201010 Numeric(15,10),
TR201009 Numeric(15,10),
TR201008 Numeric(15,10),
TR201007 Numeric(15,10),
TR201006 Numeric(15,10),
TR201005 Numeric(15,10),
TR201004 Numeric(15,10),
TR201003 Numeric(15,10),
TR201002 Numeric(15,10),
TR201001 Numeric(15,10),
TR200912 Numeric(15,10),
TR200911 Numeric(15,10),
TR200910 Numeric(15,10),
TR200909 Numeric(15,10),
TR200908 Numeric(15,10),
TR200907 Numeric(15,10),
TR200906 Numeric(15,10),
TR200905 Numeric(15,10),
TR200904 Numeric(15,10),
TR200903 Numeric(15,10),
TR200902 Numeric(15,10),
TR200901 Numeric(15,10),
TR200812 Numeric(15,10),
TR200811 Numeric(15,10),
TR200810 Numeric(15,10),
TR200809 Numeric(15,10),
TR200808 Numeric(15,10),
TR200807 Numeric(15,10),
TR200806 Numeric(15,10),
TR200805 Numeric(15,10),
TR200804 Numeric(15,10),
TR200803 Numeric(15,10),
TR200802 Numeric(15,10),
TR200801 Numeric(15,10),
TR200712 Numeric(15,10),
TR200711 Numeric(15,10),
TR200710 Numeric(15,10),
TR200709 Numeric(15,10),
TR200708 Numeric(15,10),
TR200707 Numeric(15,10),
TR200706 Numeric(15,10),
TR200705 Numeric(15,10),
TR200704 Numeric(15,10),
TR200703 Numeric(15,10),
TR200702 Numeric(15,10),
TR200701 Numeric(15,10),
TR200612 Numeric(15,10),
TR200611 Numeric(15,10),
TR200610 Numeric(15,10),
TR200609 Numeric(15,10),
TR200608 Numeric(15,10),
TR200607 Numeric(15,10),
TR200606 Numeric(15,10),
TR200605 Numeric(15,10),
TR200604 Numeric(15,10),
TR200603 Numeric(15,10),
TR200602 Numeric(15,10),
TR200601 Numeric(15,10),
TR200512 Numeric(15,10),
TR200511 Numeric(15,10),
TR200510 Numeric(15,10),
TR200509 Numeric(15,10),
TR200508 Numeric(15,10),
TR200507 Numeric(15,10),
TR200506 Numeric(15,10),
TR200505 Numeric(15,10),
TR200504 Numeric(15,10),
TR200503 Numeric(15,10),
TR200502 Numeric(15,10),
TR200501 Numeric(15,10),
TR200412 Numeric(15,10),
TR200411 Numeric(15,10),
TR200410 Numeric(15,10),
TR200409 Numeric(15,10),
TR200408 Numeric(15,10),
TR200407 Numeric(15,10),
TR200406 Numeric(15,10),
TR200405 Numeric(15,10),
TR200404 Numeric(15,10),
TR200403 Numeric(15,10),
TR200402 Numeric(15,10),
TR200401 Numeric(15,10),
TR200312 Numeric(15,10),
TR200311 Numeric(15,10),
TR200310 Numeric(15,10),
TR200309 Numeric(15,10),
TR200308 Numeric(15,10),
TR200307 Numeric(15,10),
TR200306 Numeric(15,10),
TR200305 Numeric(15,10),
TR200304 Numeric(15,10),
TR200303 Numeric(15,10),
TR200302 Numeric(15,10),
TR200301 Numeric(15,10),
TR200212 Numeric(15,10),
TR200211 Numeric(15,10),
TR200210 Numeric(15,10),
TR200209 Numeric(15,10),
TR200208 Numeric(15,10),
TR200207 Numeric(15,10),
TR200206 Numeric(15,10),
TR200205 Numeric(15,10),
TR200204 Numeric(15,10),
TR200203 Numeric(15,10),
TR200202 Numeric(15,10),
TR200201 Numeric(15,10),
TR200112 Numeric(15,10),
TR200111 Numeric(15,10),
TR200110 Numeric(15,10),
TR200109 Numeric(15,10),
TR200108 Numeric(15,10),
TR200107 Numeric(15,10),
TR200106 Numeric(15,10),
TR200105 Numeric(15,10),
TR200104 Numeric(15,10),
TR200103 Numeric(15,10),
TR200102 Numeric(15,10),
TR200101 Numeric(15,10),
TR200012 Numeric(15,10),
TR200011 Numeric(15,10),
TR200010 Numeric(15,10),
TR200009 Numeric(15,10),
TR200008 Numeric(15,10),
TR200007 Numeric(15,10),
TR200006 Numeric(15,10),
TR200005 Numeric(15,10),
TR200004 Numeric(15,10),
TR200003 Numeric(15,10),
TR200002 Numeric(15,10),
TR200001 Numeric(15,10),
TR199912 Numeric(15,10),
TR199911 Numeric(15,10),
TR199910 Numeric(15,10),
TR199909 Numeric(15,10),
TR199908 Numeric(15,10),
TR199907 Numeric(15,10),
TR199906 Numeric(15,10),
TR199905 Numeric(15,10),
TR199904 Numeric(15,10),
TR199903 Numeric(15,10),
TR199902 Numeric(15,10),
TR199901 Numeric(15,10),
TR199812 Numeric(15,10),
TR199811 Numeric(15,10),
TR199810 Numeric(15,10),
TR199809 Numeric(15,10),
TR199808 Numeric(15,10),
TR199807 Numeric(15,10),
TR199806 Numeric(15,10),
TR199805 Numeric(15,10),
TR199804 Numeric(15,10),
TR199803 Numeric(15,10),
TR199802 Numeric(15,10),
TR199801 Numeric(15,10),
TR199712 Numeric(15,10),
TR199711 Numeric(15,10),
TR199710 Numeric(15,10),
TR199709 Numeric(15,10),
TR199708 Numeric(15,10),
TR199707 Numeric(15,10),
TR199706 Numeric(15,10),
TR199705 Numeric(15,10),
TR199704 Numeric(15,10),
TR199703 Numeric(15,10),
TR199702 Numeric(15,10),
TR199701 Numeric(15,10),
TR199612 Numeric(15,10),
TR199611 Numeric(15,10),
TR199610 Numeric(15,10),
TR199609 Numeric(15,10),
TR199608 Numeric(15,10),
TR199607 Numeric(15,10),
TR199606 Numeric(15,10),
TR199605 Numeric(15,10),
TR199604 Numeric(15,10),
TR199603 Numeric(15,10),
TR199602 Numeric(15,10),
TR199601 Numeric(15,10),
TR199512 Numeric(15,10),
TR199511 Numeric(15,10),
TR199510 Numeric(15,10),
TR199509 Numeric(15,10),
TR199508 Numeric(15,10),
TR199507 Numeric(15,10),
TR199506 Numeric(15,10),
TR199505 Numeric(15,10),
TR199504 Numeric(15,10),
TR199503 Numeric(15,10),
TR199502 Numeric(15,10),
TR199501 Numeric(15,10),
TR199412 Numeric(15,10),
TR199411 Numeric(15,10),
TR199410 Numeric(15,10),
TR199409 Numeric(15,10),
TR199408 Numeric(15,10),
TR199407 Numeric(15,10),
TR199406 Numeric(15,10)
)"""
mycursor.execute(sql)


mydb.commit()
mydb.close()