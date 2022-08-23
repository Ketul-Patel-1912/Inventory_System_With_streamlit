
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import os
# import pypyodbc as odbc
import sqlite3

# @st.cache
# def load_image(image_file):
#         img = Image(image_file)
#         return img

img1 = Image.open('icon16.png')

st.set_page_config(page_title='Die_Inventory_System',
                           layout='wide',
                           page_icon="img1")

## dB FXN
# from db_fxn import (table_create,insert_values,view_all_data,get_die_number,view_unique_die_number,view_unique_spec_size,view_unique_spec_code,view_unique_total_width,view_unique_compound,edit_die_data,delete_data,search_record)



mydb = sqlite3.connect('data.db')
mycursor =mydb.cursor()

def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS spec_history(die_number varchar(25) not null,compound varchar(25),tread_size varchar(50),spec_code varchar(50),oem varchar(50),total_width int not null,top_width int not null,length int not null,weight int not null,m_weight int not null,issue_date date,machining_date date,prototype_date date,production_date date,revoke_date date,remark varchar(80))")
                                             

# DRIVER_NAME = 'SQL SERVER'
# SERVER_NAME = 'LAPTOP-NQPCNVC9'
# DATABASE_NAME ="Tread_Spec_History"
# CONNECTION_STRING =f"""
#                     DRIVER={{{DRIVER_NAME}}};
#                     SERVER={SERVER_NAME};
#                     DATABASE={DATABASE_NAME};
#                     Trust_Connection=yes;
#                     """

# mydb = odbc.connect(CONNECTION_STRING)
# mycursor = mydb.cursor()
# mycursor.execute("USE Tread_Spec_History")

# def table_create():
#         mycursor.execute(""" IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'spec_history' AND type = 'U')
#                             BEGIN
#                                 CREATE TABLE spec_history (
#                                     die_number varchar(25) not null, 
#                                     compound varchar(25) not null,
#                                     tread_size varchar(50) not null,
#                                     spec_code varchar(50) not null,
#                                     oem varchar(50),
#                                     total_width int not null,
#                                     top_width int not null,
#                                     length int not null,
#                                     weight int not null,
#                                     m_weight int not null,
#                                     issue_date varchar(50),
#                                     machining_date varchar(50),
#                                     prototype_date varchar(50),
#                                     production_date varchar(50),
#                                     revoke_date varchar(50),
#                                     remark varchar(500) 
#                                     )
#                             END""")

        

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
    
def main():


        menu = ["Add Tread Spec History",'Show Records','Update','Delete','About']
        choice = st.sidebar.selectbox('Menu',menu)
        
        create_table()
        
        if choice == 'Add Tread Spec History':
                new_title1 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Add Tread Specification Details</p>'
                st.markdown(new_title1, unsafe_allow_html=True)
                st.write('---')
                #--make layout--#
                
                col1,col2,col3,col4,col5 = st.columns(5)
                with col1:
                        die_number = st.text_input("Die_number",placeholder="IA001(101-01)-01",max_chars=16,autocomplete="on")
                        total_width = st.number_input("Total Width",max_value=300)
                        issue_data = st.text_input("Issue Date",placeholder="DD/MM/YYYY")
                                
                with col2:
                        cmp=['7316','7716','7717','751','752','7316+7250','751+7250']
                        compound = st.selectbox('Coumpound',cmp)
                        top_width = st.number_input("Top Width",max_value=200)
                        machining_data = st.text_input("Die Machining Date",placeholder="DD/MM/YYYY")
                with col3:
                        tread_size  = st.text_input("Tread Size",placeholder='90/100-10 M6000')
                        length = st.number_input("Length",max_value=3000)
                        prototype_data = st.text_input("Prototype Date",placeholder="DD/MM/YYYY")
                with col4:
                        spec_code = st.text_input('Spec.Code',placeholder='SMC21522-027-A/B/C')
                        weight = st.number_input("Weight",step=100,max_value=3000)
                        production_data = st.text_input("Production Date",placeholder="DD/MM/YYYY")
                with col5:
                        oem = st.text_input('OEM',placeholder='Honda-TT/TL')
                        m_weight = st.number_input("1 Meter Weight",step=100,max_value=3000)
                        revoke_data = st.text_input("Revoke Date",placeholder="DD/MM/YYYY")
                remark = st.text_area("Remark")
                
                
 ###--- Spec Load and store in directory-----#### 
                        
                validation = [die_number,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight]
                clm = ['Die Number','Tread Size','Spec Code','OEM','Total Width','Top Width','Length','Weight','m_weight']
                cnt=0
                for ind,i in enumerate(validation):
                        
                        if (i=="" or i==0):
                                st.warning("Add {} First".format(clm[ind]),icon="⚠️")
                                cnt+=1
                                break
                        else:
                                cnt+=1
                                
                image_files = st.file_uploader("Choose Tread Specification Image",type=['.jpeg','.jpg'],disabled=False)
                
                if image_files is not None:
                        cnt+=1
                        file_details = {"FileName":die_number,"FileType":image_files.type}
                        st.write(file_details) 
                        img=Image.open(image_files)
                        st.image(img,use_column_width='always')
                else:
                      st.warning("Add Tread Spec Image",icon="⚠️")  
                      
                if cnt>=10:
                        submit_button = st.button("Add Spec Data",disabled=False)   
                else:
                        submit_button = st.button("Add Spec Data",disabled=True)
                        
                if image_files is not None:
                                parent_dir = "C:/"
                                directory = "Spec_Photo"
                                path = os.path.join(parent_dir, directory)
                                try:
                                        os.makedirs(path, exist_ok = True)
                                        st.text("Directory '%s' created successfully" % directory)
                                except OSError as error:
                                        st.text("Directory '%s' can not be created" % directory)
                
                if submit_button:
                                                 
                        with open(os.path.join(path,"{}.jpg".format(die_number)),"wb")as f:
                                        f.write(image_files.getbuffer())
                          
                        insert_values(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_data,machining_data,prototype_data,production_data,revoke_data,remark)

                        st.success("Tread Specification History Updated successfully :-  {}".format(die_number))

        elif choice == 'Show Records':
                new_title2 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">View Tread Specification Details</p>'
                st.markdown(new_title2, unsafe_allow_html=True)
                
                result = view_all_data()
                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                df = pd.DataFrame(result,columns=column)
                st.dataframe(df)
                
                with st.expander("Search Records"):
                        
                        col1,col2 = st.columns(2)
                        file_Choose = ['Die Number','Tread Size','Specification Code','Compound','Total Width']
                        filter_selection = col1.selectbox("Choose Category for record Search",file_Choose)

                        st.write("---")
                        if filter_selection == "Die Number":
                                search_category = 'die_number'         
                                list_of_die_number = [i[0] for i in view_unique_die_number()]
                                search_item = col2.selectbox("Choose Right Die Number",list_of_die_number)
                                result = search_record(search_category,search_item)
                                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)
                                
                                path = "C://Spec_Photo/{}.JPG".format(search_item)
                                
                                if path is not "C://Spec_Photo/{}.JPG".format(search_item):
                                        img = Image.open(path,"r")
                                        st.image(img,use_column_width='always')
                                else:
                                        st.warning("Image Not Found",icon="⚠️")
             
                        elif filter_selection == "Tread Size":
                                search_category = 'tread_size'         
                                unique_spec_size = [i[0] for i in view_unique_spec_size()]
                                search_item = col2.selectbox("Choose Right Specification Size",unique_spec_size)
                                
                                result = search_record(search_category,search_item)
                                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)
                                
                        elif filter_selection == "Specification Code":
                                search_category = 'spec_code'         
                                unique_spec_code = [i[0] for i in view_unique_spec_code()]
                                search_item = col2.selectbox("Choose Right Specification Code",unique_spec_code)
                                
                                result = search_record(search_category,search_item)
                                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)
                                
                        elif filter_selection == "Compound":
                                search_category = 'compound'         
                                unique_compound = [i[0] for i in view_unique_compound()]
                                search_item = col2.selectbox("Choose Right compound ",unique_compound)
                                
                                result = search_record(search_category,search_item)
                                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)
                                
                        elif filter_selection == "Total Width":
                                search_category = 'total_width'         
                                unique_total_width = [i[0] for i in view_unique_total_width()]
                                search_item = col2.selectbox("Choose Right Total Width",unique_total_width)
                                
                                result = search_record(search_category,search_item)
                                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)
                                
                                
                                
                        
                
                with st.expander("Graph Plot"):
                        ## barhcart OEM wise
                        
                        
                        ## pie chart compound
                        col1,col2 = st.columns(2)
                        df_bar = df['compound'].value_counts().reset_index()
                        col1.dataframe(df_bar)
                        
                        pie_chart = px.pie(df_bar,names='index',values='compound')
                        col2.plotly_chart(pie_chart)
                        
                        
                        
                        
                        
        elif choice == 'Update':
                new_title3 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Update Tread Specification Details</p>'
                st.markdown(new_title3, unsafe_allow_html=True)
                
                result = view_all_data()
                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                df = pd.DataFrame(result,columns=column)
                
                with st.expander("Current Records"):
                        st.dataframe(df)
                list_of_die_number = [i[0] for i in view_unique_die_number()]
                # st.write(list_of_die_number)
                select_die = st.selectbox("SELECT DIE NUMBER FOR RECORD UPDATE",list_of_die_number)
                select_result = get_die_number(select_die)
                
                if select_result:
                        die_number1 = select_result[0][0]
                        compound1 =  select_result[0][1]
                        tread_size1 = select_result[0][2]
                        spec_code1 = select_result[0][3]
                        oem1 = select_result[0][4]
                        total_width1 = select_result[0][5]
                        top_width1 = select_result[0][6]
                        length1 = select_result[0][7]
                        weight1 = select_result[0][8]
                        m_weight1 = select_result[0][9]
                        issue_date1 = select_result[0][10]
                        machining_date1 = select_result[0][11]
                        prototype_date1 = select_result[0][12]
                        production_date1 = select_result[0][13]
                        revoke_date1 = select_result[0][14]
                        remark1 = select_result[0][15]   
                        
                        st.write('---')
                        
                        #--make layout--#
                        
                        col1,col2,col3,col4,col5 = st.columns(5)
                        with col1:
                                new_die_number = st.text_input("Die_number",die_number1,placeholder="IA001(101-01)-01")
                                new_total_width = st.number_input("Total Width",total_width1)
                                new_issue_date = st.text_input("Issue Date")
                        with col2:
                                cmp=['7316','7716','7717','751','752','7316+7250','751+7250']
                                new_compound = st.selectbox('Coumpound',cmp)
                                new_top_width = st.number_input("Top Width",top_width1)
                                new_machining_date = st.text_input("Die Machining Date")
                        with col3:
                                new_tread_size  = st.text_input("Tread Size",tread_size1,placeholder='90/100-10 M6000')
                                new_length = st.number_input("Length",length1)
                                new_prototype_date = st.text_input("Prototype Date")
                        with col4:
                                new_spec_code = st.text_input('Spec.Code',spec_code1,placeholder='SMC21522-027-A/B/C')
                                new_weight = st.number_input("Weight",weight1)
                                new_production_date = st.text_input("Production Date")
                        with col5:
                                new_oem = st.text_input('OEM',oem1,placeholder='Honda-TT/TL')
                                new_m_weight = st.number_input("1 Meter Weight",m_weight1)
                                new_revoke_date = st.text_input("Revoke Date")
                                
                        new_remark = st.text_area("Remark",remark1)
                        
                        if st.button("Update Details"):
                                
                                edit_die_data(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1)
                                
                                st.success("Tread Specification History Updated successfully")
                        
                        result = view_all_data()
                        column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                        df = pd.DataFrame(result,columns=column)
                        
                        with st.expander("Updated Records"):
                                st.dataframe(df)
                                          
                
        elif choice == 'Delete':
                new_title4 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Delete Tread Specification Details</p>'
                st.markdown(new_title4, unsafe_allow_html=True)
                
                result = view_all_data()
                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                df = pd.DataFrame(result,columns=column)
                
                with st.expander("Current Records"):
                        st.dataframe(df)
                        
                list_of_die_number = [i[0] for i in view_unique_die_number()]
   
                select_die = st.selectbox("SELECT DIE NUMBER FOR RECORD DELETE",list_of_die_number)
                
                # st.warning("Do you want to Delete record")
                if st.button("Delete the record"):
                        delete_data(select_die)
                        st.success("Data has been successfully Deleted")
                        
                result = view_all_data()
                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                df = pd.DataFrame(result,columns=column)
                
                with st.expander("Current Records"):
                        st.dataframe(df)
                        
                
                
        else:
                new_title = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Die Inventory System with Streamlit</p>'
                st.markdown(new_title, unsafe_allow_html=True)
                # st.title("Die Inventory System with Streamlit",title)
                st.subheader('About')
                
        
    

if __name__ == '__main__':
        main()

