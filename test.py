import connection
print(connection.mydb)

mycursor = connection.mydb.cursor()

# TODO Turn into function that can be called
# TODO Seperate functions for public posts vs private messages
# TODO Modify to iterate through a provided csv of search words

def word_search_test(columns, table, search_column, search_term):
    print(
        #"SELECT post_date, author_name, post_title, post FROM forums_posts where post like '%male%' limit 3 "
        "SELECT" + columns + "FROM" + table + "WHERE " + search_column + "LIKE '%" + search_term + "%'"
        #TODO improve search function https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html
    )

word_search_test("post", "forums_posts","post", "male")