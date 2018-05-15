#!/usr/bin/env python

import psycopg2


def top_3_articles():
    """Connect to database 'news' and return top 3 articles of all time.

    Join log table to articles table by concatenating '/article/' with slug
    column in articles table using the '||' operator to match path column
    in log table.

    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("""SELECT title, count(title) as views FROM log
        JOIN articles on '/article/' || articles.slug = log.path
        WHERE status = '200 OK'
        GROUP BY title
        ORDER BY views DESC
        LIMIT 3;""")
    tuple_list = cursor.fetchall()
    print('The most popular 3 articles of all time are:')
    for item in tuple_list:
        print('{} - {} views'.format(item[0], item[1]))
    db.close()
    print('')


def most_popular_authors():
    """Connect to database 'news' and return all authors sorted by number
    of views.

    Join log table to articles table by concatenating '/article/' with slug
    column in articles table using the '||' operator to match path column in
    log table.

    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("""SELECT authors.name, count(authors.name) as views
        FROM log
        JOIN articles on '/article/' || articles.slug = log.path
        JOIN authors on authors.id = articles.author
        WHERE status = '200 OK'
        GROUP BY authors.name
        ORDER BY views DESC """)
    tuple_list = cursor.fetchall()
    print('The most popular article authors of all time are:')
    for item in tuple_list:
        print('{} - {} views'.format(item[0], item[1]))
    db.close()
    print('')


def error_rate():
    """Connect to database 'news' and return days on which error rate > 1%.

    Use 2 created views of log table - one with day wise errors and the other
    with day wise total views.
    Join views on day column and calculate percentage errors as a percentage
    of total views.
    Convert errors.visits to float to enable float division.

    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("""SELECT total_visits.day,
        errors.visits::float/total_visits.visits
        AS percent
        FROM total_visits
        JOIN errors on errors.day = total_visits.day
        WHERE errors.visits::float/total_visits.visits > 0.01;""")
    tuple_list = cursor.fetchall()
    print('Days on which more than 1 percent of requests led to errors:')
    for item in tuple_list:
        print('{0:%B %d, %Y} - {1:.2%} errors'.format(item[0], item[1]))
    db.close()


def main():
    """Generate reports"""
    top_3_articles()
    most_popular_authors()
    error_rate()


if __name__ == '__main__':
    """ """
    main()
