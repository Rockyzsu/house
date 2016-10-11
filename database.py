# -*-coding=utf-8-*-
__author__ = 'Rocky'
import sqlite3

def create_table():
    conn = sqlite3.connect('shenzhen_house.db')
    try:
        create_tb_cmd='''
        CREATE TABLE IF NOT EXISTS HOUSE
        ('日期' TEXT,
        '一手房套数' TEXT,
        '一手房面积' TEXT,
        '二手房套数' TEXT,
        '二手房面积' TEXT);
        '''
        #主要就是上面的语句
        conn.execute(create_tb_cmd)
    except:
        print "Create table failed"
        return False


    conn.execute(create_tb_cmd)
    conn.commit()
    conn.close()

def insert(date,one_hand,one_area,second_hand,second_area):
    conn = sqlite3.connect('shenzhen_house.db')
    print "open database passed"

    cmd="INSERT INTO HOUSE ('日期','一手房套数','一手房面积','二手房套数','二手房面积') VALUES('%s','%s','%s','%s','%s');" %(date,one_hand,one_area,second_hand,second_area)
    #works 要么加\"
    #paul_su="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(5,'%s',32,'CALIFORNIA',2000.00);" %temp2
    #works 要么加 ’‘

    #allen="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'ALLEN',72,'CALIFORNIA',20500.00);"
    #teddy="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(3,'TEDDY',732,'CALIFORNIA',52000.00);"
    #mark="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(4,'MARK',327,'CALIFORNIA',3000.00);"
    #sun="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(?,?,?,?,?);"
    #conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(?,?,32,'CALIFORNIA',2000.00)",temp)

    conn.execute(cmd)

    conn.commit()
    conn.close()