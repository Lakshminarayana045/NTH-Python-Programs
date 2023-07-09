from pymysql import *

# create    or        Inserting Data
'''
a = connect(host = 'localhost',user = 'root',password = '8179',db = 'ps')
b = a.cursor()
b.execute(" insert into pra values(1,'lucky','Hyd'),(2,'venky','KDKR')")
a.commit()
'''

# update    or      Modifying Data
'''
a = connect(host = 'localhost',user = 'root',password = '8179',db = 'ps')
b = a.cursor()
b.execute("update pra set loc = 'Kandukur' where roll = 2")
a.commit()
'''

# Retrieve  or      Fetching Data
'''
a = connect(host = 'localhost',user = 'root',password = '8179',db = 'ps')
b = a.cursor()
b.execute(" select * from pra " )
a.commit()
print(b.fetchall())
'''

# Delete    or  Deleting Data
'''
a = connect(host = 'localhost',user = 'root',password = '8179',db = 'ps')
b = a.cursor()
b.execute("delete from pra where roll = 1")
a.commit()
'''
#Fetchone() : first row only
#fetchmany() : frist n number of rows
#fetchall() : all rows
