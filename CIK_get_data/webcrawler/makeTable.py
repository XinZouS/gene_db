import mysql.connector # pip install mysql-connector-python
import db_config


mydb = mysql.connector.connect(
	host=db_config.local_host,
	user=db_config.user,
	passwd=db_config.passwd,
	database=db_config.database	
	)

mycursor = mydb.cursor()


sql = """
CREATE TABLE CIKs (
CIK varchar(10) NOT NULL,
Name varchar(128) NOT NULL,
Date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (CIK)
);

CREATE TABLE CIK_series (
id int NOT NULL AUTO_INCREMENT,
CIK varchar(10) NOT NULL,
Series varchar(10) NOT NULL,
Name varchar(256) NOT NULL,
Date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);

CREATE TABLE CIK_class (
id int NOT NULL AUTO_INCREMENT,
CIK varchar(10) NOT NULL,
Series varchar(10) NOT NULL,
Class varchar(10) NOT NULL,
Name varchar(256) NOT NULL,
TickerSymbol varchar(7) NULL,
Date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);
"""
mycursor.execute(sql)


mydb.commit()
mydb.close()