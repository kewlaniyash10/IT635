import psycopg2

conn = psycopg2.connect("postgresql://admin:ilovesql@localhost/project")
cur = conn.cursor()

while True:
    print("Issue Management System \n")
    
    department = input("Enter Department ID: \n 1. Human Resources \n 2. Finance \n")
    
    issue_id = input("Enter Issue Number: \n")
    
    print("Fetching Results... \n")
    
    if department == 1:
        cur.execute ("""
        SELECT issue, department, first_name, last_name FROM HR WHERE issue = %s; 
        """ ,  (issue_id));
    else:
        cur.execute ("""
        SELECT issue, department, first_name, last_name FROM FINANCE WHERE issue = %s; 
        """ ,  (issue_id));
    
    result = cur.fetchall();
    print(result)
    
    print("End of Result \n")
    conn.commit()

conn.close()
