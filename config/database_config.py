import mysql.connector

class DatabaseConnector:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "123"
        self.database = "pbo_week11"
        self.connection = None

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def test_connection(self):
        try:
            self.connect_to_database()
            if self.connection.is_connected():
                print("Connection succesful.")
            else:
                print("Connection failed.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()