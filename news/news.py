#!/usr/bin/python
import psycopg2

DB = psycopg2.connect("dbname = news")
c = DB.cursor()
sql_popular_articles = "./sqls/sel_popular_articles.sql"
sql_most_read = "./sqls/sel_most_read.sql"
sql_worst_percentage = "./sqls/sel_worst_percentage.sql"


def get_database_results(sql_file):
    """ Function 2 recover results from database
    PARAMS: SQL File with query
    RETURN: Dict with query results
    """
    c.execute(open(sql_file, "r").read())
    results = ({'field1': str(row[0]), 'field2': float(row[1])}
               for row in c.fetchall())
    return results


def print_line():
    """ Function 2 print "_" n times
    PARAMS: None
    RETURN: Screen Output with "_" * 80
    """
    print '_' * 80
    print ''


def print_popular_articles():
    """ Function 2 print the 3 articles more read
    PARAMS: None
    RETURN: None
    """
    for result in get_database_results(sql_popular_articles):
        print '%s -- %d views' % (result['field1'], float(result['field2']),)


def print_most_read():
    """ Function 2 print the authors more read
    PARAMS: None
    RETURN: None
    """
    for result in get_database_results(sql_most_read):
        print '%s -- %d views' % (result['field1'], float(result['field2']),)


def print_worst_percentage():
    """ Function 2 print worst percentage date (error > 1%)
    PARAMS: None
    RETURN: None
    """
    for result in get_database_results(sql_worst_percentage):
        print '%s %2.2f%s' % (result['field1'], result['field2'], '%',)


def main():
    """ Function which prints all the results
    PARAMS: None
    RETURN: None
    """
    print_line()
    print "First Question"
    print_line()
    print_popular_articles()
    print_line()
    print "Second Question"
    print_line()
    print_most_read()
    print_line()
    print "Third Question"
    print_line()
    print_worst_percentage()
    print_line()
    DB.close()


main()  # MAIN PROGRAM ...
