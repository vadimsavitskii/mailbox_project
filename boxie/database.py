import sqlite3


def create_table():
    db = sqlite3.connect('/home/pi/BOXIE_study_project/db_server.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS device(
        password TEXT
    )""")
    db.commit()
    db.close()
    
    
def add_new_entry(password):
    db = sqlite3.connect('/home/pi/BOXIE_study_project/db_server.db')
    sql = db.cursor()
    sql.execute("""INSERT INTO device VALUES (?)""", (password,))
    db.commit()
    db.close()
    
    
def update_entry(old_password, new_password):
    db = sqlite3.connect('/home/pi/BOXIE_study_project/db_server.db')
    sql = db.cursor()
    sql.execute("""UPDATE device SET password = ? WHERE password = ?""", (new_password, old_password))
    db.commit()
    db.close()


def view_all_records():
    db = sqlite3.connect('/home/pi/BOXIE_study_project/db_server.db')
    sql = db.cursor()
    sql.execute("""SELECT * FROM device""")
    devices = sql.fetchall()
    db.close()
    return devices
    
box_password = view_all_records()[0][0]

if __name__ == '__main__':
    #create_table()
    #add_new_entry('1346')
    pass