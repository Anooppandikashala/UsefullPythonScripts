import mysql.connector
from mysql.connector import errorcode


def login(conn, user_name, password):
    cursor = conn.cursor()
    query = ("SELECT id FROM users "
             "WHERE username = %s AND PASSWORD = %s")
    cursor.execute(query, (user_name, password))
    records = cursor.fetchall()
    if len(records) > 0:
        return True
    else:
        return False


if __name__ == '__main__':

    try:
        conn = mysql.connector.connect(user='root', password='123456', database='login_test',
                                       unix_socket="/opt/lampp/var/mysql/mysql.sock")

        username = str(raw_input("Enter your Username :"))
        password = str(raw_input("Enter your Password :"))

        if login(conn, username, password):
            print("Login Success")
        else:
            print("Username or Password is incorrect")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        conn.close()
