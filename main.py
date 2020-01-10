import connection
print(connection.mydb)

mycursor = connection.mydb.cursor()
search_words = ["male", "sex", "feminist"]

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

def public_post_search(search_terms):
    for i in search_terms:
        word_search("author_name, post_date, post", "forums_posts", "post", i)

public_post_search(search_words)