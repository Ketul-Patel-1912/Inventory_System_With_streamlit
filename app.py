

import base64
from email.policy import default
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
import os
import os.path
import sqlite3

# img1 = Image.open('icon16.png')

st.set_page_config(page_title='Die_Inventory_System',
                           layout='wide',
                           page_icon="bi bi-nintendo-switch")


mydb = sqlite3.connect('data.db')
mycursor =mydb.cursor()

def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS spec_history(die_number varchar(25) not null,compound varchar(25),tread_size varchar(50),spec_code varchar(50),oem varchar(50),total_width int not null,top_width int not null,length int not null,weight int not null,m_weight int not null,issue_date date,machining_date date,prototype_date date,production_date date,revoke_date date,remark varchar(80),image BLOB NOT NULL)")
                                          
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
                                       
def insert_values(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark,filepath):
        
        st.write(filepath)
        
        convert_pic = convert_To_Binary(filepath)

        mycursor.execute('INSERT INTO spec_history(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark,image) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_date,machining_date,prototype_date,production_date,revoke_date,remark,convert_pic))
        
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
        

def edit_die_data(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,convert_pic,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1,image1):
        
        mycursor.execute("""UPDATE spec_history SET die_number="{}",compound={},tread_size='{}',spec_code='{}',oem='{}',total_width={},top_width={},length={},weight={},m_weight={},issue_date='{}',machining_date='{}',prototype_date='{}',production_date='{}',revoke_date='{}',remark='{}',image={} WHERE  die_number={} and compound={} and tread_size='{}' and spec_code='{}' and oem='{}' and total_width={} and top_width={} and length={} and weight={} and m_weight={} and issue_date='{}' and machining_date='{}' and prototype_date='{}' and production_date='{}' and revoke_date='{}' and remark='{}' and image='{}'""".format(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,convert_pic,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1,image1))
            
        mydb.commit()
        fetch = mycursor.fetchall()
        return fetch

def update_image(new_die_number,image):
        
        mycursor.execute("UPDATE spec_history SET image='{}' WHERE die_number='{}'".format(image,new_die_number))

        mydb.commit()
        fetch = mycursor.fetchall()
        return fetch

def edit_die_data_radio_no(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1):
        
        mycursor.execute("""UPDATE spec_history SET die_number='{}',compound='{}',tread_size='{}',spec_code='{}',oem='{}',total_width={},top_width={},length={},weight={},m_weight={},issue_date='{}',machining_date='{}',prototype_date='{}',production_date='{}',revoke_date='{}',remark='{}' \
                     WHERE  die_number='{}' and compound='{}' and tread_size='{}' and spec_code='{}' and oem='{}' and total_width='{}' and top_width='{}' and length='{}' and weight='{}' and m_weight='{}' and issue_date='{}' and machining_date='{}' and prototype_date='{}' and production_date='{}' and revoke_date='{}' and remark='{}'""".format(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1))
    
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


def main():
        
        with st.sidebar:
                
                selection = option_menu(
                        menu_title=None,
                        options= ['TR Spec History','Die Inventory System'],
                        icons=['bi bi-device-ssd-fill',"bi bi-boxes"],
                        menu_icon="cast",
                        default_index=0)
                
        ### ------------------------------------------------------ Tread Specification History ----------------------------------------------------------------------------------        
                
        if selection == "TR Spec History":
     
                choice = option_menu(
                                menu_title=None,
                                options= ['About',"Add Record",'Show Records','Update Record','Delete Record'],
                                icons=['bi bi-file-person','bi bi-cloud-plus','bi bi-easel','bi bi-bootstrap-reboot','bi bi-trash'],
                                menu_icon="cast",
                                default_index=0,
                                orientation="horizontal")

        
                create_table()
                
                if choice == "Add Record":
                        # new_title1 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Add Tread Specification Details</p>'
                        # st.markdown(new_title1, unsafe_allow_html=True)
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
                                   
                        image_files = st.file_uploader("Choose Tread Specification Image",type=['.jpeg','.jpg','.png'],disabled=False)

                        if image_files is not None: 
                                cnt+=1
                                file_details = {"FileName":die_number,"FileType":image_files.type}
                                st.write(file_details) 
                                img=Image.open(image_files)
                                st.image(img,use_column_width='always')
                                parent_dir = "C:/"
                                directory = "Spec_Photo"
                                path = os.path.join(parent_dir, directory)
                                os.makedirs(path, exist_ok = True)
                                StoreFilePath = "{}/{}.JPG".format(path,die_number)
                                
                                with open(StoreFilePath, "wb") as file:
                                        file.write(image_files.getbuffer())
                                
                        else:
                                st.warning("Add Tread Spec Image",icon="⚠️")
                              
                        if cnt>=10:
                                
                                submit_button = st.button("Add Spec Data",disabled=False)                                    
                        else:
                                submit_button = st.button("Add Spec Data",disabled=True)
                                
                        if submit_button:
                                insert_values(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_data,machining_data,prototype_data,production_data,revoke_data,remark,StoreFilePath)
                                
                                st.balloons()
                                st.success("Tread Specification History Updated successfully :-  {}".format(die_number))
                                        
                        
                                

                elif choice == 'Show Records':
                        # new_title2 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">View Tread Specification Details</p>'
                        # st.markdown(new_title2, unsafe_allow_html=True)
                        
                        st.write("---")
                        result = view_all_data()
                        column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark','image']
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
                                       
                                        df = pd.DataFrame(result,columns=column)
                                        st.dataframe(df)
                                        
                                        if result is not None:
                                                parent_dir = "C:/"
                                                directory = "Spec_Photo"
                                                path = os.path.join(parent_dir, directory)
                                                StoreFilePath = "{}/{}.JPG".format(path,search_item)
                                                
                                                if StoreFilePath == 'C:/Spec_Photo/{}.JPG'.format(search_item):

                                                        file_exists = os.path.exists(StoreFilePath)
                                                        if file_exists:
                                                                img=Image.open(StoreFilePath)
                                                                st.image(img,use_column_width='always')
                                                        else:
                                                                st.warning("No match spec image in directory",icon="🙄")
                                                        
                                                elif search_item is None:
                                                        st.warning("Zero Record in Dataset, ADD Spec DATA",icon="🙄")
                                                        
                                                else:
                                                        st.warning("Zero Record in Dataset, ADD Spec DATA",icon="🙄")
                                       
                                        # print(read_image(search_item,StoreFilePath))               
                
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
                                        
                                        
                                        
                                
                        
                        with st.expander("Graph Plot"):
                                ## barhcart OEM wise
                                
                                
                                ## pie chart compound
                                col1,col2 = st.columns(2)
                                df_bar = df['compound'].value_counts().reset_index()
                                col1.dataframe(df_bar)
                                
                                pie_chart = px.pie(df_bar,names='index',values='compound')
                                col2.plotly_chart(pie_chart)
                                
                                
                                
                                
                                
                elif choice == 'Update Record':
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
                                        remark1 = select_result[0][15]   
                                        image1 = select_result[0][16]    ## binary data
                                        
                               
                                        
                                        #--make layout--#
                                        
                                        
                                col1,col2,col3=st.columns(3)
                                with col1:
                                        new_die_number = st.text_input("Die_number",die_number1,placeholder="IA001(101-01)-01")
                                        cmp=['7316','7716','7717','751','752','7316+7250','751+7250']
                                        new_compound = st.selectbox('Coumpound',cmp)
                                        new_tread_size  = st.text_input("Tread Size",tread_size1,placeholder='90/100-10 M6000')
                                        new_spec_code = st.text_input('Spec.Code',spec_code1,placeholder='SMC21522-027-A/B/C')                                                
                                        new_oem = st.text_input('OEM',oem1,placeholder='Honda-TT/TL')
                                        
                                with col2:
                                        new_total_width = st.number_input("Total Width",total_width1)                                                
                                        new_top_width = st.number_input("Top Width",top_width1)
                                        new_length = st.number_input("Length",length1)
                                        new_weight = st.number_input("Weight",weight1)
                                        new_m_weight = st.number_input("1 Meter Weight",m_weight1)
                                with col3:
                                        new_issue_date = st.text_input("Issue Date")
                                        new_machining_date = st.text_input("Die Machining Date")
                                        new_prototype_date = st.text_input("Prototype Date")
                                        new_production_date = st.text_input("Production Date")
                                        new_revoke_date = st.text_input("Revoke Date")
                        
                                new_remark = st.text_area("Remark",remark1)
                        
                                if select_die is not None:
                                        parent_dir = "C:/"
                                        directory = "Spec_Photo"
                                        path = os.path.join(parent_dir, directory)
                                        StoreFilePath = "{}/{}.JPG".format(path,select_die)
                                        
                                        f1,f2 = st.columns(2)
                                        f1.subheader("Currunt Tread Specification Image")
                                        img=Image.open(StoreFilePath)
                                        
                                        f1.image(img,use_column_width=True)
                                        
                                else:
                                        st.warning("Zero Record in Dataset, ADD Spec DATA",icon="🙄")
                                
                                if new_die_number and new_total_width and new_top_width and new_tread_size and new_length  and new_spec_code  and new_weight and new_m_weight:
                                        cnt=2
                                        radio_button = st.radio("Do you Want to change Tread Spec Image..?",options=["No",'Yes'],horizontal=True,disabled=False)
                                        # check = st.checkbox("")
                                
                                        if radio_button=="Yes":
                                                
                                                image_files_updated = st.file_uploader("Choose Tread Specification Image",type=['.jpeg','.jpg','.png'],disabled=False)
                                                update = st.button("Update Record",disabled=False)
                                                
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
                                                
                                                update = st.button("Update Record",disabled=False)
                     
                                else:
                                        radio_button = st.radio("Do you Want to change Tread Spec Image..?",options=["Yes","No"],horizontal=True,disabled=True)
                                        update = st.button("Update Record",disabled=True)
                                        
                                        st.info("OPPS..!! You havn't Fill the all required Details", icon="ℹ️")
                                
                        # if "load_state" not in st.session_state:
                        #                 st.session_state.load_state = False
                                
                        if update: #or st.session_state.load_state:
                                        
                                        # st.session_state.load_state = True    
                                         
                                        if radio_button=="No":
                                                
                                                parent_dir = "C:/"
                                                directory = "Spec_Photo"
                                                path = os.path.join(parent_dir, directory)
                                                
                                                old_path = "{}/{}.JPG".format(path,die_number1)
                                                new_path = "{}/{}.JPG".format(path,new_die_number)
                                                os.rename(old_path, new_path)
                                                
                                                
                                                edit_die_data_radio_no(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1)
                                
                                                st.balloons()
                                                st.success("Tread Specification History Updated successfully")
                                                
                                                
                                        elif radio_button=="Yes":
                                                
                                                with open(StoreFilePath2, "wb") as file:
                                                                file.write(image_files_updated.getbuffer())
                                                    
                                                # delete_image(die_number1)
                                                
                                                # st.write("delete query executed successfully")
                                                
                                                # image1=''
                                                
                                                convert_pic = list(convert_To_Binary(StoreFilePath2))
                                                convert_pic = list(convert_pic)
                                                
                                                edit_die_data(new_die_number,new_compound,new_tread_size,new_spec_code,new_oem,new_total_width,new_top_width,new_length,new_weight,new_m_weight,new_issue_date,new_machining_date,new_prototype_date,new_production_date,new_revoke_date,new_remark,convert_pic,die_number1,compound1,tread_size1,spec_code1,oem1,total_width1,top_width1,length1,weight1,m_weight1,issue_date1,machining_date1,prototype_date1,production_date1,revoke_date1,remark1,image1)
                                                
                                                st.write("update image query executed successfully")
                                                
                                                st.balloons()
                                                st.success("Tread Specification History Updated successfully")
          
                   
                elif choice == 'Delete Record':
                        # new_title4 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Delete Tread Specification Details</p>'
                        # st.markdown(new_title4, unsafe_allow_html=True)
                        st.write("---")
                        
                        result = view_all_data()
                        column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark','image']
                        df = pd.DataFrame(result,columns=column)
                        
                        with st.expander("Current Records"):
                                st.dataframe(df)
                                
                        list_of_die_number = [i[0] for i in view_unique_die_number()]
        
                        select_die = st.selectbox("SELECT DIE NUMBER FOR RECORD DELETE",list_of_die_number)
                        
                        # st.warning("Do you want to Delete record")
                        if st.button("Delete the record"):
                                delete_data(select_die)
                                st.balloons()
                                st.success("Data has been successfully Deleted")
                                
                        result = view_all_data()
                        column = ['die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark','image']
                        df = pd.DataFrame(result,columns=column)
                        
                        with st.expander("Current Records"):
                                st.dataframe(df)
                                
                        
                        
                else:
                        # new_title = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Die Inventory System with Streamlit</p>'
                        # st.markdown(new_title, unsafe_allow_html=True)
                        st.title("Tread Specification History")
                        st.write("---")
                        st.subheader('Add the recored')
                        st.write("First add record")
                                        
                                        
        #### -----------------------------------------------Die Inventory Systems --------------------------------------------------------------------
        
                
        if selection == "Die Inventory System":
                
                choice = option_menu(
                                menu_title=None,
                                options= ['About',"Add Die Record",'Show Records','Update Record','Delete Record'],
                                icons=['bi bi-file-person','bi bi-cloud-plus','bi bi-easel','bi bi-bootstrap-reboot','bi bi-trash'],
                                menu_icon="cast",
                                default_index=0,
                                orientation="horizontal")
                
                
                
                
                
    

if __name__ == '__main__':
        main()

