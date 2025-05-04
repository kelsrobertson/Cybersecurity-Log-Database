import cherrypy
import pymysql

# Database connection function
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Kelsey2003!',
        database='hacking_db',
        client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
    )

# CherryPy Application
class UserAuthApp(object):

    @cherrypy.expose
    def index(self):
        return '''
            <form method="POST" action="/login">
                Username: <input type="text" name="username" /><br />
                Password: <input type="password" name="password" /><br />
                <input type="submit" value="Login" />
            </form>
        '''

    @cherrypy.expose
    def login(self, username, password):
        # Get DB connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Create SQL query to match username and password
        query = f"SELECT * FROM Users WHERE username = '{username}' AND password = '{password}'"
        print(query)
        try:
            # Execute the query
            cursor.execute(query)
            user = cursor.fetchone()
            conn.commit()
            # If a matching user is found, return a success message
            if user:
                return f'Login successful! Welcome {user[0]}'
            else:
                return 'Invalid username or password.'
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()
            conn.close()

# Configure and start the CherryPy application
if __name__ == '__main__':
    cherrypy.quickstart(UserAuthApp(), '/', {
        '/': {
            'tools.sessions.on': True,
        }
    })