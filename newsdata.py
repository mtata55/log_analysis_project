#!usr/bin/python3

import psycopg2


def top_3_articles():
    db = psycopg2.connect("dbname=news")  # connect to database
    cursor = db.cursor()
    cursor.execute("""SELECT title, count(title) as views FROM log
        JOIN articles on '/article/' || articles.slug = log.path --use psql || operator for string concatenation thus creating join field
        WHERE status = '200 OK'  --ignore incorrect URL's
        GROUP BY title
        ORDER BY views DESC --sort highest to lowest
        LIMIT 3;""")  # top 3 results only
    tuple_list = cursor.fetchall()
    print('The most popular 3 articles of all time are:')
    for item in tuple_list:
        print('{} - {} views'.format(item[0], item[1]))
    db.close()
    print('')

top_3_articles()


def most_popular_authors():
    db = psycopg2.connect("dbname=news")  # connect to database
    cursor = db.cursor()
    cursor.execute("""SELECT authors.name, count(authors.name) as views FROM log
        JOIN articles on '/article/' || articles.slug = log.path
        JOIN authors on authors.id = articles.author  --use psql || operator for string concatenation thus creating join field
        WHERE status = '200 OK'  --ignore incorrect URL's
        GROUP BY authors.name
        ORDER BY views DESC """)  # sort highest to lowest;
    tuple_list = cursor.fetchall()
    print('The most popular article authors of all time are:')
    for item in tuple_list:
        print('{} - {} views'.format(item[0], item[1]))
    db.close()
    print('')


most_popular_authors()


def error_rate():
    db = psycopg2.connect("dbname=news")  # connect to database
    cursor = db.cursor()
    cursor.execute("""SELECT total_visits.day, errors.visits::float/total_visits.visits as percent from total_visits
        JOIN errors on errors.day = total_visits.day
        WHERE errors.visits::float/total_visits.visits > 0.01;""")
    tuple_list = cursor.fetchall()
    print('Days on which more than 1 percent of requests led to errors:')
    for item in tuple_list:
        # use strftime method to change date format for presentation
        print('{} - {} % errors'.format(item[0].strftime("%B %d, %Y"), float(round(item[1] * 100, 2))))
    db.close()

error_rate()
