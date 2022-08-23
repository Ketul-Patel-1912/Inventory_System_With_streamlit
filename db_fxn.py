import pypyodbc as odbc

# import sqlite3
# conn = sqlite3.connect('data.db')
# mycursor =conn.cursor()

# def create_table():
#     mycursor.execute("CREATE TABLE IF NOT EXISTS spec_history(die_number varchar(25) not null,compound varchar(25),tread_size varchar(50),spec_code varchar(50),oem varchar(50),total_width int not null,top_width int not null,length int not null,weight int not null,m_weight int not null,issue_date date,machining_date date,prototype_date date,production_date date,revoke_date date,remark varchar(80))")
                                             

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'LAPTOP-NQPCNVC9'
DATABASE_NAME ="Tread_Spec_History"
CONNECTION_STRING =f"""
                    DRIVER={{{DRIVER_NAME}}};
                    SERVER={SERVER_NAME};
                    DATABASE={DATABASE_NAME};
                    Trust_Connection=yes;
                    """

mydb = odbc.connect(CONNECTION_STRING)
mycursor = mydb.cursor()
mycursor.execute("USE Tread_Spec_History")

def table_create():
        mycursor.execute(""" IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'spec_history' AND type = 'U')
                            BEGIN
                                CREATE TABLE spec_history (
                                    die_number varchar(25) not null, 
                                    compound varchar(25) not null,
                                    tread_size varchar(50) not null,
                                    spec_code varchar(50) not null,
                                    oem varchar(50),
                                    total_width int not null,
                                    top_width int not null,
                                    length int not null,
                                    weight int not null,
                                    m_weight int not null,
                                    issue_date varchar(50),
                                    machining_date varchar(50),
                                    prototype_date varchar(50),
                                    production_date varchar(50),
                                    revoke_date varchar(50),
                                    remark varchar(500) 
                                    )
                            END""")

        

# die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark

# new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark
                                   
                                   
                                
def insert_values(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark):
    mycursor.execute('INSERT INTO spec_history(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark))
    
    mydb.commit()


def view_all_data():
    mycursor.execute('SELECT * FROM spec_history')
    data = mycursor.fetchall()
    return data

##------------------------------Find unique value for searching items-------------------------

def view_unique_die_number():
    mycursor.execute('SELECT DISTINCT die_number FROM spec_history')
    data = mycursor.fetchall()
    return data

def view_unique_spec_size():
    mycursor.execute('SELECT DISTINCT tread_size FROM spec_history')
    data = mycursor.fetchall()
    return data

def view_unique_spec_code():
    mycursor.execute('SELECT DISTINCT spec_code FROM spec_history')
    data = mycursor.fetchall()
    return data

def view_unique_compound():
    mycursor.execute('SELECT DISTINCT compound FROM spec_history')
    data = mycursor.fetchall()
    return data

def view_unique_total_width():
    mycursor.execute('SELECT DISTINCT total_width FROM spec_history')
    data = mycursor.fetchall()
    return data

    

##----------------------------------------------------------------------------------------------


def get_die_number(number):
    mycursor.execute("SELECT * FROM spec_history WHERE die_number='{}'".format(number))
    data = mycursor.fetchall()
    return data

def edit_die_data(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1):
    
    mycursor.execute("UPDATE spec_history SET die_number='{}',compound='{}',tread_size='{}',spec_code='{}',oem='{}',total_width={},top_width={},length={},weight={},m_weight={},issue_date='{}',machining_date='{}',prototype_date='{}',production_date='{}',revoke_date='{}',remark='{}' WHERE  die_number='{}' and compound='{}' and tread_size='{}' and spec_code='{}' and oem='{}' and total_width='{}' and top_width='{}' and length='{}' and weight='{}' and m_weight='{}' and issue_date='{}' and machining_date='{}' and prototype_date='{}' and production_date='{}' and revoke_date='{}' and remark='{}'".format(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1))
    
    mydb.commit()
    fetch = mycursor.fetchall()
    return fetch
    
    # mycursor.execute('UPDATE FROM spec_history SET die_number=?,compound=?,tread_size=?,spec_code=?,oem=?,total_width=?,top_width=?,length=?,weight=?,m_weight=?,issue_date=?,machining_date=?,prototype_date=?,production_date=?,revoke_date=?,remark=? WHERE die_number=? and compound=? and tread_size=? and spec_code=? and oem=? and total_width=? and top_width=? and length=? and weight=? and m_weight=? and issue_date=? and machining_date=? and prototype_date=? and production_date=? and revoke_date=? and remark=?",(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1))
    

def delete_data(number):
    mycursor.execute("DELETE FROM spec_history WHERE die_number='{}'".format(number))
    mydb.commit()
    
    

def search_record(search_item,code):
    mycursor.execute("SELECT * FROM spec_history WHERE {} LIKE '{}'".format(search_item,code))
    data = mycursor.fetchall()
    return data
    

    
    


    
