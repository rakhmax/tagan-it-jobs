from flaskext.mysql import MySQL
from . import app

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST']     = 'localhost'
app.config['MYSQL_DATABASE_USER']     = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rootpass'
app.config['MYSQL_DATABASE_DB']       = 'pias'

mysql.init_app(app)

try:
    conn = mysql.connect()
except:
    print("MySQL not working")
    exit(1)

cursor = conn.cursor()

# create_users_table_query = '''CREATE TABLE users (
#         id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#         firstname VARCHAR(64) NOT NULL,
#         lastname VARCHAR(64) NOT NULL,
#         email VARCHAR(64) NOT NULL UNIQUE KEY,
#         password VARCHAR(64) NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
#     )'''

# cursor.execute(create_users_table_query)
