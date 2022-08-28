
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
import os
import os.path
import sqlite3
import random

# img1 = Image.open('icon16.png')

st.set_page_config(page_title='Die_Inventory_System',
                           layout='wide',
                           page_icon="bi bi-nintendo-switch")

hide_st_stype = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_stype,unsafe_allow_html=True)



mydb = sqlite3.connect('data.db')
mycursor =mydb.cursor()

def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS spec_history(die_number varchar(25) not null,compound varchar(25),tread_size varchar(50),spec_code varchar(50),oem varchar(50),total_width int not null,top_width int not null,length int not null,weight int not null,m_weight int not null,issue_date date,machining_date date,prototype_date date,production_date date,revoke_date date,status varchar(40),remark varchar(80),image BLOB NOT NULL)")
                                          
# die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark

# new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark

def convert_To_Binary(filepath):
        with open(filepath,'rb') as file:
                binarydata = file.read()
        return binarydata

def convert_Binary_To_File(binarydata2,filename):
        
        with open(filename,'wb') as file:
                pic_data = file.write(binarydata2)
                
        return pic_data
                                       
def insert_values(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,status,remark,filepath):
        
        st.write(filepath)
        
        convert_pic = convert_To_Binary(filepath)

        mycursor.execute('INSERT INTO spec_history(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,status,remark,image) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,status,remark,convert_pic))
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        

def read_image(number,StoreFilePath):

        mycursor.execute("SELECT image FROM spec_history WHERE die_number='{}'".format(number))
        data = mycursor.fetchone()[0]
        picname = '{}.jpeg'.format(number)
        convert_into_pic = convert_Binary_To_File(data,picname)
        
        with open(StoreFilePath,'wb') as f:
                f.write(convert_into_pic)
                
        mydb.commit()
        mycursor.close()
        mydb.close()
        
        return convert_into_pic
        
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

def delete_image(die_number):
        
        mycursor.execute("UPDATE spec_history SET image='' WHERE die_number='{}'".format(die_number))
        mydb.commit()
        print("query executed successfully")
        
def datatype_convert(x): 
        if x=="":
                pass
        else:
                return int(x)
                

def edit_die_data(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_status,new_remark,convert_pic,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,status1,remark1,image1):
        
        mycursor.execute("""UPDATE spec_history SET die_number="{}",compound={},tread_size='{}',spec_code='{}',oem='{}',total_width={},top_width={},length={},weight={},m_weight={},issue_date='{}',machining_date='{}',prototype_date='{}',production_date='{}',revoke_date='{}',status='{}',remark='{}',image={} WHERE  die_number={} and compound={} and tread_size='{}' and spec_code='{}' and oem='{}' and total_width={} and top_width={} and length={} and weight={} and m_weight={} and issue_date='{}' and machining_date='{}' and prototype_date='{}' and production_date='{}' and revoke_date='{}' and status='{}' and remark='{}' and image='{}'""".format(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_status,new_remark,convert_pic,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,status1,remark1,image1))
            
        mydb.commit()
        fetch = mycursor.fetchall()
        return fetch

def update_image(new_die_number,image):
        
        mycursor.execute("UPDATE spec_history SET image='{}' WHERE die_number='{}'".format(image,new_die_number))

        mydb.commit()
        fetch = mycursor.fetchall()
        return fetch

def edit_die_data_radio_no(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_status,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,status1,remark1):
        
        mycursor.execute("""UPDATE spec_history SET die_number='{}',compound='{}',tread_size='{}',spec_code='{}',oem='{}',total_width={},top_width={},length={},weight={},m_weight={},issue_date='{}',machining_date='{}',prototype_date='{}',production_date='{}',revoke_date='{}',status='{}',remark='{}' \
                     WHERE  die_number='{}' and compound='{}' and tread_size='{}' and spec_code='{}' and oem='{}' and total_width='{}' and top_width='{}' and length='{}' and weight='{}' and m_weight='{}' and issue_date='{}' and machining_date='{}' and prototype_date='{}' and production_date='{}' and revoke_date='{}' and status='{}' and remark='{}'""".format(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_status,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,status1,remark1))
    
        mydb.commit()
        fetch = mycursor.fetchall()
        return fetch
        
    
def delete_data(number):
    mycursor.execute("DELETE FROM spec_history WHERE die_number='{}'".format(number))
    mydb.commit() 

def search_record(search_item,code):
    mycursor.execute("SELECT * FROM spec_history WHERE {} LIKE '{}'".format(search_item,code))
    data = mycursor.fetchall()
    return data

def month_charmonth(x):
        if x==1:
                return "Jan"
        elif x==2:
                return "Feb"
        elif x==3:
                return "Mar"
        elif x==4:
                return "Apr"
        elif x==5:
                return "May"
        elif x==6:
                return "Jun"
        elif x==7:
                return "Jul"
        elif x==8:
                return "Aug"
        elif x==9:
                return "Sap"
        elif x==10:
                return "Oct"
        elif x==11:
                return "Nov"
        elif x==12:
                return "Dec"


emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼","👈"]




def main():
        
        create_table()
        
        with st.sidebar:

                choice = option_menu(
                                menu_title=None,
                                options= ['KPIs And Graphs',"Add Record",'Show Records','Update Record','Delete Record'],
                                icons=['bi bi-file-person','bi bi-cloud-plus','bi bi-easel','bi bi-bootstrap-reboot','bi bi-trash'],
                                menu_icon="cast",
                                default_index=0)
                                                
        if choice == "Add Record":
                st.title(":large_blue_circle: Add Tread Specification Record :large_blue_circle:")
                st.write("---")
                                       
                col1,col2,col3,col4,col5 = st.columns(5)
                with col1:
                        die_number = st.text_input("Die_number",placeholder="IA001(101-01)-01",max_chars=16,autocomplete="on")
                        total_width = st.number_input("Total Width",max_value=300)
                        issue_data = st.text_input("Issue Date",placeholder="DD/MM/YYYY")
                        status = st.selectbox('Status',['Active','Revoke'])
                                
                with col2:
                        cmp=['7316','7716','7717','751','752','7316+7250','751+7250']
                        compound = st.selectbox('Coumpound',cmp)
                        top_width = st.number_input("Top Width",max_value=200)
                        machining_data = st.text_input("Die Machining Date",placeholder="DD/MM/YYYY")
                        remark = st.text_area("Remark")
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
              
###--- Spec Load and store in directory-----#### 
                        
                validation = [die_number,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight]
                clm = ['Die Number','Tread Size','Spec Code','OEM','Total Width','Top Width','Length','Weight','m_weight']
                cnt=0
                for ind,i in enumerate(validation):
                        
                        if (i=="" or i==0):
                                st.info("Add {} First".format(clm[ind]),icon="ℹ️")
                                cnt+=1
                                break
                        else:
                                cnt+=1   
                ch1,ch2 = st.columns(2)           
                image_files = ch1.file_uploader("Choose Tread Specification Image",type=['.jpeg','.jpg','.png'],disabled=False)

                if image_files is not None: 
                        cnt+=1
                        file_details = {"FileName":die_number,"FileType":image_files.type}
                        ch1.write(file_details) 
                        img=Image.open(image_files)
                        ch2.image(img,use_column_width='always')
                        parent_dir = "C:/"
                        directory = "Spec_Photo"
                        path = os.path.join(parent_dir, directory)
                        os.makedirs(path, exist_ok = True)
                        StoreFilePath = "{}/{}.JPG".format(path,die_number)
                        
                        with open(StoreFilePath, "wb") as file:
                                file.write(image_files.getbuffer())
                        
                else:
                        
                        st.info("Add Tread Spec Image", icon="ℹ️")
                        
                if cnt>=10:
                        
                        # submit_button = st.button(f"Add Spec Data {st.session_state.emoji}", on_click=random_emoji,disabled=False)
                        
                        submit_button = ch1.button("Add Spec Data",disabled=False)                                    
                else:
                        # submit_button = st.button(f"Add Spec Data {st.session_state.emoji}", on_click=random_emoji,disabled=True)
                        submit_button = ch1.button("Add Spec Data 👈",disabled=True)
                        
                if submit_button:
                        insert_values(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_data,machining_data,prototype_data,production_data,revoke_data,status,remark,StoreFilePath)
                        
                        st.balloons()
                        st.success("Tread Specification History Updated successfully :-  {}".format(die_number))
                                        
                        
                                

        elif choice == 'Show Records':
                
                st.title(":red_circle: Display History Record :red_circle: ")
                st.write("---")
                
                        # new_title2 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">View Tread Specification Details</p>'
                        # st.markdown(new_title2, unsafe_allow_html=True)
                result = view_all_data()
                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','status','remark','image']
                df = pd.DataFrame(result,columns=column)
             
                st.dataframe(df.iloc[:,:-1])
                
                with st.expander("Search Records"):
                        
                        col1,col2 = st.columns(2)
                        file_Choose = ['Die Number','Tread Size','Specification Code','Compound','Total Width','status']
                        filter_selection = col1.selectbox("Choose Category for record Search",file_Choose)

                        st.write("---")
                        if filter_selection == "Die Number":
                                search_category = 'die_number'         
                                list_of_die_number = [i[0] for i in view_unique_die_number()]
                                search_item = col2.selectbox("Choose Right Die Number",list_of_die_number)
                                result = search_record(search_category,search_item)
                                
                                df = pd.DataFrame(result,columns=column)
                              
                                st.dataframe(df.iloc[:,:-1])
                                
                                ## Condition IF image already Stored in Local then get from it other wise takes from data base 
                                parent_dir = "C:/"
                                directory = "Spec_Photo"
                                
                                path = os.path.join(parent_dir, directory)
                                os.makedirs(path, exist_ok = True)
                                StoreFilePath_code = "{}/{}.JPG".format(path,search_item)
                                
                                if StoreFilePath_code == 'C:/Spec_Photo/{}.JPG'.format(search_item) and search_item:

                                        file_exists = os.path.exists(StoreFilePath_code)
                                        if file_exists:
                                                img=Image.open(StoreFilePath_code)
                                                st.image(img,use_column_width='always')
                                                st.info("Received image From Your Local Computer Directory")
                                        else:
                                                df_image = df.iloc[:,-1]
                                                binary_image = df_image[0]
                                                with open(StoreFilePath_code, "wb") as file:
                                                        file.write(binary_image)
                                                img=Image.open(StoreFilePath_code)
                                                st.image(img,use_column_width='always')
                                                st.info("Received image From DataSet")
                                else:
                                        st.error("No image in Dataset and Your Local Directory",icon="🙄")                                      
        
                        elif filter_selection == "Tread Size":
                                search_category = 'tread_size'         
                                unique_spec_size = [i[0] for i in view_unique_spec_size()]
                                search_item = col2.selectbox("Choose Right Specification Size",unique_spec_size)
                                
                                result = search_record(search_category,search_item)
                                
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)
                                
                        elif filter_selection == "Specification Code":
                                search_category = 'spec_code'         
                                unique_spec_code = [i[0] for i in view_unique_spec_code()]
                                search_item = col2.selectbox("Choose Right Specification Code",unique_spec_code)
                                
                                result = search_record(search_category,search_item)
                        
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)
                                
                        elif filter_selection == "Compound":
                                search_category = 'compound'         
                                unique_compound = [i[0] for i in view_unique_compound()]
                                search_item = col2.selectbox("Choose Right compound ",unique_compound)
                                
                                result = search_record(search_category,search_item)
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)
                                
                        elif filter_selection == "Total Width":
                                search_category = 'total_width'         
                                unique_total_width = [i[0] for i in view_unique_total_width()]
                                search_item = col2.selectbox("Choose Right Total Width",unique_total_width)
                                
                                result = search_record(search_category,search_item)
                                
                                df = pd.DataFrame(result,columns=column)
                                st.dataframe(df)        
                                
        elif choice == 'Update Record':
                
                st.title(":gem: Update History Record :gem:")
                st.write("---")
                        # new_title3 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Update Tread Specification Details</p>'
                        # st.markdown(new_title3, unsafe_allow_html=True)
                
                with st.expander("Find And Update Records"):
                                
                        list_of_die_number = [i[0] for i in view_unique_die_number()]
                        
                        select_die = st.selectbox("SELECT DIE NUMBER FOR RECORD UPDATE",list_of_die_number)
                        select_result = get_die_number(select_die)
                        st.write("---") 
                                
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
                                status1 = select_result[0][15]
                                remark1 = select_result[0][16]   
                                image1 = select_result[0][17]    ## binary data

                                col1,col2,col3=st.columns(3)
                                
                                with col1:
                                        new_die_number = st.text_input("Die_number",die_number1,placeholder="IA001(101-01)-01")
                                        cmp=['7316','7716','7717','751','752','7316+7250','751+7250']
                                        new_compound = st.selectbox('Coumpound',cmp)
                                        new_tread_size  = st.text_input("Tread Size",tread_size1,placeholder='90/100-10 M6000')
                                        new_spec_code = st.text_input('Spec.Code',spec_code1,placeholder='SMC21522-027-A/B/C')                                                
                                        new_oem = st.text_input('OEM',oem1,placeholder='Honda-TT/TL')
                                        new_status = st.selectbox('Status',['Active','Revoke'])
                                        
                                with col2:
                                        new_total_width = st.number_input("Total Width",total_width1)                                                
                                        new_top_width = st.number_input("Top Width",top_width1)
                                        new_length = st.number_input("Length",length1)
                                        new_weight = st.number_input("Weight",weight1)
                                        new_m_weight = st.number_input("1 Meter Weight",m_weight1)
                                        new_remark = st.text_area("Remark",remark1)
                                with col3:
                                        new_issue_date = st.text_input("Issue Date",issue_date1)
                                        new_machining_date = st.text_input("Die Machining Date",machining_date1)
                                        new_prototype_date = st.text_input("Prototype Date",prototype_date1)
                                        new_production_date = st.text_input("Production Date",production_date1)
                                        new_revoke_date = st.text_input("Revoke Date",revoke_date1)                    
                
                                if select_die is not None:
                                        parent_dir = "C:/"
                                        directory = "Spec_Photo"
                                        path = os.path.join(parent_dir, directory)
                                        StoreFilePath = "{}/{}.JPG".format(path,select_die)
                                        
                                        f1,f2 = st.columns(2)
                                        f1.subheader("Currunt Tread Specification Image")
                                        img=Image.open(StoreFilePath)
                                        
                                        f1.image(img,use_column_width=True)
                                
                                if new_die_number and new_total_width and new_top_width and new_tread_size and new_length  and new_spec_code  and new_weight and new_m_weight:
                                        cnt=2
                                        radio_button = st.radio("Do you Want to change Tread Spec Image..?",options=["No",'Yes'],horizontal=True,disabled=False)
                                        # check = st.checkbox("")
                                
                                        if radio_button=="Yes":
                                                
                                                image_files_updated = st.file_uploader("Choose Tread Specification Image",type=['.jpeg','.jpg','.png'],disabled=False)
                                                update = st.button("Update Record 👈",disabled=False)
                                                
                                                if image_files_updated is not None: 
                                
                                                        parent_dir = "C:/"
                                                        directory = "Spec_Photo"
                                                        path = os.path.join(parent_dir, directory)
                                                        os.makedirs(path, exist_ok = True)
                                                        StoreFilePath2 = "{}/{}.JPG".format(path,new_die_number)
                                                        f2.subheader("Updated Tread Specification Image")        
                                                        img2=Image.open(image_files_updated)
                                                        f2.image(img2,use_column_width=True)
                                                                                                
                                        else:
                                                
                                                image_files_updated = st.file_uploader("Choose Tread Specification Image",type=['.jpeg','.jpg','.png'],disabled=True)
                                                
                                                update = st.button("Update Record 👈 ",disabled=False)
                        
                                else:
                                        radio_button = st.radio("Do you Want to change Tread Spec Image..?",options=["Yes","No"],horizontal=True,disabled=True)
                                        update = st.button("Update Record 👈",disabled=True)                                       
                                        st.info("OPPS..!! You havn't Fill the all required Details", icon="ℹ️")
                         
                                if update: 
                                                                                               
                                        if radio_button=="No":
                                                
                                                parent_dir = "C:/"
                                                directory = "Spec_Photo"
                                                path = os.path.join(parent_dir, directory)
                                                
                                                old_path = "{}/{}.JPG".format(path,die_number1)
                                                new_path = "{}/{}.JPG".format(path,new_die_number)
                                                os.rename(old_path, new_path)
                                                
                                                
                                                edit_die_data_radio_no(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_status,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,status1,remark1)
                                
                                                st.balloons()
                                                st.success("Tread Specification History Updated successfully")
                                                
                                                
                                        elif radio_button=="Yes":
                                                
                                                with open(StoreFilePath2, "wb") as file:
                                                                file.write(image_files_updated.getbuffer())
                                                
                                                convert_pic = convert_To_Binary(StoreFilePath2)
                                                
                                                
                                                edit_die_data(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_status,new_remark,convert_pic,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,status1,remark1,image1)
                                                
                                                st.write("update image query executed successfully")
                                                
                                                st.balloons()
                                                st.success("Tread Specification History Updated successfully")
                                                
                        else:
                                st.error("Opps !!! Zero Recored Avalible in Dataset <--HINT-->Add Record First",icon="🙄") 
                                
                   
        elif choice == 'Delete Record':
                        # new_title4 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Delete Tread Specification Details</p>'
                        # st.markdown(new_title4, unsafe_allow_html=True)
                st.title(":bar_chart: Delete Tread History Record")
                st.write("---")
                
                
                result = view_all_data()
                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','status','remark','image']
                df = pd.DataFrame(result,columns=column)
                
                with st.expander("Current Records"):
                        st.dataframe(df)
                        
                list_of_die_number = [i[0] for i in view_unique_die_number()]

                select_die = st.selectbox("SELECT DIE NUMBER FOR RECORD DELETE",list_of_die_number)
                
                # st.warning("Do you want to Delete record")
                if st.button("Delete the record 👈 "):
                        delete_data(select_die)
                        st.balloons()
                        st.success("Data has been successfully Deleted")
                        
                result = view_all_data()
                df = pd.DataFrame(result,columns=column)
                
                with st.expander("Current Records"):
                        st.dataframe(df)
                                
                        
                        
        else:
                st.title(":bar_chart: Tread Specification History")
                st.write("---") 
                
                column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','status','remark','image']
                result = view_all_data()
                df = pd.DataFrame(result,columns=column)
        
                cl1,cl2,cl3,cl4,cl5 = st.columns(5)
                with cl1:
                        # st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)

                        st.info("Total Spec Availability")
                        st.info(df.shape[0])
                with cl2:
                        st.warning("Coumpound wise Spec")
                        df_bar = df['compound'].value_counts().reset_index().rename(columns={'index':'Rubber','compound':'count'})                                
                        st.write(df_bar)
                        
                with cl3:
                        st.info("OEM Spec")
                        df_bar = df['oem'].value_counts().reset_index().rename(columns={'index':'OEM','oem':'count'})                                
                        st.write(df_bar)
                        
                with cl4:
                        st.error("Number Of Active Spec")
                        active_spec = df[df['status']=='Active'].shape[0]                                
                        st.warning(active_spec)
                with cl5:
                        st.warning("Number Of Revoked")
                        active_spec = df[df['status']=='Revoke'].shape[0]                                
                        st.error(active_spec)
                        
                        
                with st.expander("Graph Plot"):
                        ## barhcart OEM wise
                        
                        f1,f2,f3 = st.columns(3)
                        oem_filter = f1.multiselect("Select OEM",options=df['oem'].unique(),
                        default=df['oem'].unique() )
                                                    
                        compound_filter = f2.multiselect("Select Rubber Name",options=df['compound'].unique(),
                        default=df['compound'].unique())
                        
                        status_filter = f3.multiselect("Select Spec Status",options=df['status'].unique(),
                        default=df['status'].unique())
                        
                        df_selection = df.query('oem==@oem_filter & compound==@compound_filter & status==@status_filter')
                        
                        ## bar chart --> total number of spec vs material,OEM,Active                            
                        df_bar = df_selection['compound'].value_counts().reset_index()                               
                        pie_chart = px.pie(df_bar,names='index',values='compound',width=500)
                        st.plotly_chart(pie_chart)
                        
                        ## bar chart --> total number of spec vs material,OEM,Active 
                        
                        grop_df = df_selection.groupby(['oem','status'])['die_number'].count().reset_index()
                        
                        cmd_grop_df = df_selection.groupby(['compound','status'])['die_number'].count().reset_index()
                        
                        
                        oem_count = px.histogram(grop_df, x="oem", y="die_number",
                        color='status', barmode='group',                       
                        text_auto=True,
                        template="plotly_white")
                        
                        
                        oem_count.update_layout(
                        plot_bgcolor="rgba(0,0,0,0)",
                        xaxis=(dict(title='Tire Vandors Type',showgrid=False)),
                        yaxis=(dict(title='NUmber of Tread Spec',showgrid=False,visible=True,showticklabels= False)),
                        showlegend=False
                        )
                        
                        
                        cmpnd_count = px.histogram(cmd_grop_df, x="compound", y="die_number",
                        color='status', barmode='group',                       
                        text_auto=True,
                        template="plotly_white",
                        )
                        
                        cmpnd_count.update_layout(
                        plot_bgcolor="rgba(0,0,0,0)",
                        xaxis=(dict(title='Type Of Rubber',showgrid=False)),
                        yaxis=(dict(title='NUmber of Tread Spec',showgrid=False,visible=True,showticklabels= False))
                        )
                        
                        
                        g1,g2 = st.columns(2)
                        g1.plotly_chart(oem_count,use_container_width=True)
                        g2.plotly_chart(cmpnd_count,use_container_width=True)
                        
                        
                        ### graph 3 
                        
                        # select year
                        
                        new = df.loc[:,('die_number','compound','oem','status','issue_date')]
                        
                        new['issue_date'] = pd.to_datetime(new['issue_date'])
                        new['year'], new['month'] = new['issue_date'].dt.year,new['issue_date'].dt.month
                        
                        
                        
                        Year = st.selectbox("Select Year",options=new['year'].unique())
                        
                        df_new = new.query('year==@Year')
                        
                        filter_data = df_new.groupby(['month','status'])['die_number'].count().reset_index()
                        
                        filter_data['month_char']=filter_data['month'].apply(month_charmonth)

                        year_spec = px.histogram(filter_data, x="month_char", y="die_number",
                        color='status', barmode='group',                       
                        text_auto=True,
                        width=600,height=400,
                        template="plotly_white",
                        color_discrete_map={'Active': 'green','Revoke': 'red'}
                        )
                        year_spec.update_layout(
                        plot_bgcolor="rgba(0,0,0,0)",
                        xaxis=(dict(title='Month Of the {}'.format(Year),showgrid=False)),
                        yaxis=(dict(title='NUmber of Tread Spec Issued',showgrid=False,visible=True,showticklabels= False))
                        )
                        
                        st.plotly_chart(year_spec)
                        

                        
                        
                        
                        
                        
                        
                        
              
                                        
                        
                        
                                
                                
                                
         
                                        
                                        
        # #### -----------------------------------------------Die Inventory Systems --------------------------------------------------------------------
        
                
        # elif selection == "Die Inventory System":
                
        #         choice1 = option_menu(
        #                         menu_title=None,
        #                         options= ['KPIs And Graphs',"Add Die Record",'Show Records','Update Record','Delete Record'],
        #                         icons=['bi bi-file-person','bi bi-cloud-plus','bi bi-easel','bi bi-bootstrap-reboot','bi bi-trash'],
        #                         menu_icon="cast",
        #                         default_index=0,
        #                         orientation="horizontal")
                
                # if choice1=="KPIs And Graphs":
                        
                #         st.write("hello...ketulya")
                #         number='IA049'
                #         StoreFilePath ="C:\Spec_Photo\IA049.JPG"
                #         IMG_NEW = read_image(number,StoreFilePath)
                        
                #         img2=Image.open(IMG_NEW)
                #         st.image(img2,use_column_width=True)
                        
                
                
                
                
                
    

if __name__ == '__main__':
        main()

