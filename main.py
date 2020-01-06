import connection
print(connection.mydb)

mycursor = connection.mydb.cursor()

mycursor.execute(
    "SELECT * FROM forums_posts where post like '%male%' "
)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)