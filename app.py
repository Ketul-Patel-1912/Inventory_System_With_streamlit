from ctypes import resize
from secrets import choice
from tkinter import ANCHOR
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

## dB FXN
from db_fxn import table_create,insert_values,view_all_data,get_die_number,view_unique_die_number

def main():
        st.set_page_config(page_title='Die_Inventory_System',
                           layout='wide',
                           page_icon="🧊")

        menu = ["Create",'Read','Update','Delete','About']
        choice = st.sidebar.selectbox('Menu',menu)
        
        table_create()
        
        if choice == 'Create':
                new_title1 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Add Tread Specification Details</p>'
                st.markdown(new_title1, unsafe_allow_html=True)
                st.write('---')
                #--make layout--#
                col1,col2,col3,col4,col5 = st.columns(5)
                with col1:
                        die_number = st.text_input("Die_number",placeholder="IA001(101-01)")
                        total_width = st.number_input("Total Width",step=1,min_value=0,max_value=300)
                        issue_data = st.date_input("Issue Date")
                with col2:
                        cmp=['7316','7716','7717','751','752','7316+7250','751+7250']
                        compound = st.selectbox('Coumpound',cmp)
                        top_width = st.number_input("Top Width",step=1,min_value=0,max_value=200)
                        machining_data = st.date_input("Die Machining Date")
                with col3:
                        tread_size  = st.text_input("Tread Size",placeholder='90/100-10 M6000')
                        length = st.number_input("Length",step=50,min_value=500,max_value=3000)
                        prototype_data = st.date_input("Prototype Date")
                with col4:
                        spec_code = st.text_input('Spec.Code',placeholder='SMC21522-027-A/B/C')
                        weight = st.number_input("Weight",step=50,min_value=700,max_value=3000)
                        production_data = st.date_input("Production Date")
                with col5:
                        oem = st.text_input('OEM',placeholder='Honda-TT/TL')
                        m_weight = st.number_input("1 Meter Weight",step=50,min_value=700,max_value=3000)
                        revoke_data = st.date_input("Revoke Date")
                remark = st.text_area("Remark")
                
                if st.button("Add Details"):
                        insert_values(die_number,compound,tread_size,spec_code,oem,total_width,top_width,length,weight,m_weight,issue_data,machining_data,prototype_data,production_data,revoke_data,remark)
                        st.success("Die Data added successfully :-  {}".format(die_number))                       
        
        elif choice == 'Read':
                new_title2 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">View Tread Specification Details</p>'
                st.markdown(new_title2, unsafe_allow_html=True)
                
                result = view_all_data()
                column = ['sr_no','die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                df = pd.DataFrame(result,columns=column)
                
                with st.expander("View All Records"):
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
                column = ['sr_no','die_number','compound','tread_size','spec_code','oem','total_width','top_width','length','weight','m_weight','issue_date','machining_date','prototype_date','production_date','revoke_date','remark']
                df = pd.DataFrame(result,columns=column)
                
                with st.expander("Current Records"):
                        st.dataframe(df)
                list_of_die_number = [i[0] for i in view_unique_die_number()]
                # st.write(list_of_die_number)
                select_die = st.selectbox("SELECT DIE NUMBER FOR RECORD UPDATE",list_of_die_number)
                select_result = get_die_number(select_die)
                
                
                                        
                
                
                
        elif choice == 'Delete':
                new_title4 = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Delete Tread Specification Details</p>'
                st.markdown(new_title4, unsafe_allow_html=True)
        else:
                new_title = '<p style="font-family:sans-serif; color:#F63366; font-size: 40px; font-weight: bold;">Die Inventory System with Streamlit</p>'
                st.markdown(new_title, unsafe_allow_html=True)
                # st.title("Die Inventory System with Streamlit",title)
                st.subheader('About')
                
        
        


if __name__ == '__main__':
        main()

