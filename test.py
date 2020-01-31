import connection
import mysql.connector


search_words = ["alpha", "AoC", "beta", "boy", "consent", "cuck", "cuckold", "fag", "female", "feminazi", "feminine", "feminism", "feminist", "gay", "gender", "girl", "incel", "male", "mangina", "masculine", "rights", "misogyny", "pill", "rape", "sex", "sexuality", "victim"]

# TODO Separate functions for public posts vs private messages
# TODO Modify to iterate through a provided csv of search words

def word_search(columns, table, search_column, search_term, type):
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
    rownum=0
    for x in myresult:
        rownum=rownum+1
        with open('/Users/jonathanleek/Desktop/working/'+type+'_'+search_term+'_'+str(rownum)+'.html', 'w') as out:
            print(x, file=out)
    mycursor.close()

for word in search_words:
    print("Public Post Results for " + word)
    word_search("post", "forums_posts", "post", word,"public")
    print("Private Message Results for " + word)
    word_search("msg_post", "core_message_posts", "msg_post", word, "private")

