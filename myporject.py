import json
import os
from  cryptography.fernet import Fernet
import mysql.connector
import csv


try:

    csvpath=r"C:\Users\AbdealiDodiya\Desktop\DevOps\Python\Lecture 57\mycsvfile.csv"
    jsonfile=r"C:\Users\AbdealiDodiya\Desktop\DevOps\Python\Lecture 57\mylinux.json"

    with open(jsonfile) as jf:
        print("We are fetching MYSQL password and encrypting and decrypting...")
        my_dict = json.load(jf)
        username_mysql = (my_dict['username'])
        password_mysql = (my_dict['password'])
        message = password_mysql.encode("utf-8")
        key = Fernet.generate_key()
        f = Fernet(key)
        enc = f.encrypt(message)

        dec = f.decrypt(enc)    #Decryption
        passwd_mysql = dec.decode('utf-8')


        mydb = mysql.connector.connect (
            host = "192.168.1.8",
            user= "mysql_user",
            password = passwd_mysql,
            database = "alnafi"
        )

        print("CSV file reading and storing into mysql DB")
        with open(csvpath) as csv_file:
            csvfile = csv.reader(csv_file,delimiter=',')
            all_values=[]
            for row in csvfile:
                value = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                all_values.append(value)
        query= "insert into my_df_data (filesystem,size,used,avail,usage_with_per,mounted_on,datetime,ip_address,hostname) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor =mydb.cursor()
        mycursor.executemany(query,all_values)
        mydb.commit()
        mydb.close()
        print("Data has been imported into DB successfully")
except Exception as e:
    print("Something having issue : ",e)
