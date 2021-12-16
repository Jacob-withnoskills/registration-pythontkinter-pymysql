import cx_Oracle


try:
    connection = cx_Oracle.connect(
        user='SYSTEM',
        password='miyamura',
        dsn='localhost:1521/XEPDB1',
        encoding='UTF-8',
        database='regsys'
    )
    cur=connection.cursor()
    cur.execute("insert into regsys(FIRST_NAME,LAST_NAME,CONTACT_NO,EMAIL,SECURITY_QUESTIONS,ANSWER,PASSWORD) values(%s,%s,%s,%s,%s,%s,%s)",
                 (self.txtname.get(),
                 self.lname.get(),
                 self.txtcontact.get(),
                 self.ename.get(),
                 self.txtanswer.get(),
                 self.sanswer.get(),
                 self.password.get())
                 )
    connection.commit()
    connection.close()

except Exception as ex:
    print(ex)