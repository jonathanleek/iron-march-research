import connection
print(connection.mydb)

mycursor = connection.mydb.cursor()

# TODO Separate functions for public posts vs private messages
# TODO Modify to iterate through a provided csv of search words

def word_search(columns, table, search_column, search_term):
    #Creates a SELECT/FROM/WHERE/LIKE query against the database.
    mycursor.execute(
        "SELECT " + columns + " FROM " + table + " WHERE " + search_column + " LIKE '%" + search_term + "%'"
        #TODO improve search function https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html
    )
    myresult = mycursor.fetchall()
    # TODO Output to csv
    for x in myresult:
        print(x)

word_search("post", "forums_posts","post", "male")