#Importing required libraries
import streamlit as st
import mysql.connector 

#establishing MySQL connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Tweety@555",
    database = "electionresults2024"
)

#Creating a Cursor
mycursor = mydb.cursor()

#Streamlit app
# defining main function

def main():
    st.title("Election Results 2024")

    option = st.sidebar.selectbox("Select an Operation",("Create", "Read", "Update", "Delete"))
    if option =="Create":
        st.subheader("Create a Record")
        Constituency = st.text_input("Enter Constituency")
        ConstNo = st.number_input("Enter ConstNo")
        LeadingCandidate = st.text_input("Enter Leading Candidate")
        if st.button ("Create"):
            sql = "INSERT INTO results(Constituency, ConstNo, LeadingCandidate) VALUES (%s,%s,%s)"
            val =  (Constituency, ConstNo, LeadingCandidate)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record created!!!")
        
        
        elif option=="Read":
            st.subheader("Read Records")
            mycursor.execute("SELECT * FROM results")
            result = mycursor.fetchall()
            for row in result:
                st.write(row)

        elif option == "Update":
            st.subheader("Update a Record")
            Constituency = st.tetx_input("Enter Constituency")
            ConstNo = st.number_input("Enter ConstNo")
            LeadingCandidate = st.text_input("Enter Leading Candidate")
            if st.button("Update"):
                sql = "UPDATE results set Constituency=%s, LeadingCandidate=%s WHERE ConstNo=%s"
                val = (Constituency, LeadingCandidate, ConstNo)
                mycursor.execute(sql,val)
                mydb.commit()
                st.success("Record updated successfully!!")

        elif option == "Delete":
            st.subheader("Delete a Record")
            ConstNo = st.number_input("Enter ConstNo")
            if st.button("Delete"):
                sql = "DELETE FROM results WHERE ConstNo = %s"
                val = (ConstNo)
                mycursor.execute(sql,val)
                mydb.commit()
                st.success("Records Deleted Successfully")

    if __name__== "__main__":
        main()
