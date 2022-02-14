import psycopg2

conn = psycopg2.connect("postgresql://it_admin:ilovesql@localhost/project")
cur = conn.cursor()

while True:
    print("Please enter issue ID: ")
    issue_id = int(input())
    department = input("Enter department name: ")
    print("Fetching Results... ")
    cur.execute ('''
    SELECT * FROM %s WHERE issue = %s RETURNING issue, department, first_name, last_name; 
    ''' , (issue_id, department));
    
    result = cur.fetchall();
    print(result)
    
    conn.commit()

conn.close()

