import connection
import mysql.connector




search_words = ["male","female"]

# TODO Separate functions for public posts vs private messages
# TODO Modify to iterate through a provided csv of search words

def word_search(columns, table, search_column, search_term):
    # Creates a SELECT/FROM/WHERE/LIKE query against the database.
    mydb = mysql.connector.connect(
        host=connection.myhost,
        user=connection.myuser,
        database=connection.mydatabase,
        password=connection.mypassword
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT " + columns + " FROM " + table + " WHERE " + search_column + " LIKE '%" + search_term + "%'"
        # TODO improve search function https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html
    )
    myresult = mycursor.fetchall()
    # TODO Output to csv
    for x in myresult:
        print(x)
    mycursor.close()

for word in search_words:
    print("Results for " + word)
    word_search("author_name, post_title, post", "forums_posts", "post", word)
