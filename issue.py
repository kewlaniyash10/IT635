import psycopg2

conn = psycopg2.connect("postgresql://admin:ilovesql@localhost/project")
cur = conn.cursor()

while True:
    print("Issue Management System ")
    department = input("Enter department name: ")
    issue_id = input("Enter issue number: ")
    print("Fetching Results... ")
    cur.execute ('''
    SELECT * FROM %s WHERE issue = %s RETURNING issue, department, first_name, last_name; 
    ''' , (department, issue_id));
    
    result = cur.fetchall();
    print(result)
    
    conn.commit()

conn.close()

