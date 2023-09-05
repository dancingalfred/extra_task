import psycopg2

def db_connection():
    conn = psycopg2.connect(
    host="localhost",
    port="5432", # Usually port number 5432 for PostgreSQL
    database="checkpointdb",
    user="postgres",
    password="mittPW") # Change to your own pgAdmin postgres user
    return conn



def read_contacts():
    dbconn = db_connection()
    cur = dbconn.cursor()
    cur.execute("SELECT contacts.first_name,contacts.last_name,contacts.title,contacts.organization,items.contact,items.contact_id,items.contact_type_id,items.contact_category_id,contact_types.contact_type,contact_categories.contact_category FROM contacts JOIN items ON items.contact_id = contacts.id JOIN contact_types ON items.contact_type_id = contact_types.id JOIN contact_categories ON items.contact_category_id = contact_categories.id;")
    rows = cur.fetchall()
    cur.close()
    dbconn.close()
    return rows


def add_contact_to_contacts(first_name,last_name,title,organization):
    dbconn = db_connection()
    cur = dbconn.cursor()
    cur.execute("INSERT INTO contacts (first_name,last_name,title,organization) VALUES (%s, %s, %s, %s);",(first_name,last_name,title,organization))
    dbconn.commit()
    cur.close()
    dbconn.close()
    return "done"


def delete_contact_from_contacts(id):
    dbconn = db_connection()
    cur = dbconn.cursor()
    cur.execute("DELETE FROM contacts WHERE id = %s;", (id,))
    dbconn.commit()
    cur.close()
    dbconn.close()
    return "done"


while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")


    if cmd == "list":
        print(read_contacts())
    if cmd == "add":
        new_first_name = input("Type first name: ")
        new_last_name = input("Type new last name: ")
        new_title = input("Type new title: ")
        new_organization = input("Type new organization: ")
        add_contact_to_contacts(new_first_name,new_last_name,new_title,new_organization)
    if cmd == "delete":
        del_id = input("Type the id of the contact you want to delete: ")
        delete_contact_from_contacts(del_id)
    if cmd == "quit":
        exit()
