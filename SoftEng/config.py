MYSQL_URL="ec2-18-188-253-115.us-east-2.compute.amazonaws.com"
MYSQL_USER="hcorado"
MYSQL_PW="password123456"
MYSQL_DB="MyDBCoradoTech"
MYSQL_TABLE="myContacts"
MYSQL_CREATETABLE="""CREATE TABLE myContacts(
    id INT NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(30) NOT NULL,
    GAMERTAG VARCHAR(30) NOT NULL,
    PHONE VARCHAR(30) NOT NULL,
    DISCORD VARCHAR(30) NOT NULL,
    PRIMARY KEY(ID));
"""