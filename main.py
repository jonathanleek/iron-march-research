import connection
print(connection.mydb)

mycursor = connection.mydb.cursor()

# TODO Turn into function that can be called
# TODO Seperate functions for public posts vs private messages
# TODO Modify to iterate through a provided csv of search words
mycursor.execute(
    "SELECT * FROM forums_posts where post like '%male%' " #TODO improve search function https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html
)

myresult = mycursor.fetchall()
# TODO Output to csv
for x in myresult:
    print(x)