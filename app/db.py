from flaskext.mysql import MySQL
from . import app

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rootpass'
app.config['MYSQL_DATABASE_DB'] = 'pais_test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

try:
    conn = mysql.connect()
except:
    print("MySQL not working")
    exit(1)

cursor = conn.cursor()



