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
                                    sr_no INT IDENTITY(1,1) PRIMARY KEY,
                                    die_number varchar(25) not null, 
                                    compound varchar(25),
                                    tread_size varchar(50),
                                    spec_code varchar(50),
                                    oem varchar(50),
                                    total_width int not null,
                                    top_width int not null,
                                    length int not null,
                                    weight int not null,
                                    m_weight int not null,
                                    issue_date date,
                                    machining_date date,
                                    prototype_date date,
                                    production_date date,
                                    revoke_date date,
                                    remark varchar(80) 
                                    )
                            END""")

        

# die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark
                                    
                                
def insert_values(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark):
    mycursor.execute('INSERT INTO spec_history(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark))
    
    mydb.commit()


def view_all_data():
    mycursor.execute('SELECT * FROM spec_history')
    data = mycursor.fetchall()
    return data

def view_unique_die_number():
    mycursor.execute('SELECT DISTINCT die_number FROM spec_history')
    data = mycursor.fetchall()
    return data

def get_die_number(number):
    mycursor.execute("SELECT * FROM spec_history WHERE die_number='{}'".format(number))
    data = mycursor.fetchall()
    return data
    

