import psycopg2

conn = psycopg2.connect("postgresql://admin:ilovesql@localhost/project")
cur = conn.cursor()

while True:
    print("Issue Management System \n")
    
    department = input("Enter Department Name: \n")
    
    issue_id = input("Enter Issue Number: \n")
    
    print("Fetching Results... \n")
    
    cur.execute ("""
    SELECT issue, department, first_name, last_name FROM %s WHERE issue = %s; 
    """ ,  (department, issue_id));
    
    result = cur.fetchall();
    print(result)
    print("End of Result \n")
    conn.commit()

conn.close()
