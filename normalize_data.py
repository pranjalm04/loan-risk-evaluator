import os
import sqlite3
import pandas as pd
from datetime import datetime
def create_connection(db_file,delete_db=False):
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)
    conn=None

    try:
        conn=sqlite3.connect(db_file)
        conn.execute('PRAGMA foreign_keys = 1')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn,create_table_sql, drop_table_name=None):
    if drop_table_name:
        try:
            c=conn.cursor()
            c.execute("""DROP TABLE IF EXISTS %s""" %(drop_table_name))
        except sqlite3.Error as e:
            print(e)
    try:
        c=conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)



if __name__=='__main__':

    csv_file = "credit_features_subset.csv"
    data = pd.read_csv(csv_file)
    db_name = "Loan.db"

    credit_feature_sql=f"""CREATE TABLE CreditFeature (
        UID INTEGER,  -- Primary Key for CreditFeature
        ALL_AgeOfOldestAccount INTEGER NOT NULL,
        ALL_AgeOfYoungestAccount INTEGER NOT NULL,
        ALL_Count INTEGER NOT NULL,
        ALL_CountActive INTEGER NOT NULL,
        ALL_CountClosedLast12Months INTEGER NOT NULL,
        ALL_CountDefaultAccounts INTEGER NOT NULL,
        ALL_CountOpenedLast12Months INTEGER NOT NULL,
        ALL_CountSettled INTEGER NOT NULL,
        ALL_MeanAccountAge FLOAT NOT NULL,
        ALL_SumCurrentOutstandingBal INTEGER NOT NULL,
        ALL_SumCurrentOutstandingBalExcMtg INTEGER NOT NULL,
        ALL_TimeSinceMostRecentDefault INTEGER NOT NULL,
        ALL_WorstPaymentStatusActiveAccounts INTEGER NOT NULL,
        FOREIGN KEY (UID) REFERENCES LoanApplication (UID)
    );"""

    loan_application_sql=f"""CREATE TABLE LoanApplication (
        UID INTEGER PRIMARY KEY,  -- Primary Key for LoanApplication
        ApplicationDate TEXT NOT NULL,  -- Store the application date as text (you can later format it to datetime if needed)
        Amount INTEGER NOT NULL,  -- Loan amount
        Term INTEGER NOT NULL,  -- Loan term (in months, years, etc.)
        EmploymentType TEXT NOT NULL,  -- Employment type (categorical data)
        LoanPurpose TEXT NOT NULL,  -- Purpose of the loan (categorical data)
        Success INTEGER NOT NULL  -- Whether the application was successful (binary: 1 or 0)
    );
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    create_table(conn,credit_feature_sql)
    create_table(conn,loan_application_sql)



    loan_application_data=pd.read_csv('loan_applications.csv')
    loan_application_data.to_sql("LoanApplication", conn, if_exists="append", index=False)
    creditFeatureData = pd.read_csv('credit_features_subset.csv')
    creditFeatureData.to_sql("CreditFeature", conn, if_exists="append", index=False)
    data=pd.read_sql('select * from loanapplication ;',conn)
    print(data.head(5))
