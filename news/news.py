import psycopg2
from datetime import datetime

DB = psycopg2.connect("dbname = news")
c = DB.cursor()
sql_popular_articles = "./sqls/sel_popular_articles.sql"
sql_most_read = "./sqls/sel_most_read.sql"
sql_wors_percentage = "./sqls/sel_worst_percentage.sql"


def get_popular_articles():
    """ Function 2 recover 3 most popular articles
    PARAMS: None
    RETURN: Dict with query results
    """
    c.execute(open(sql_popular_articles, "r").read())
    results = ({'title': str(row[0]), 'cont': float(row[1])}
               for row in c.fetchall())
    return results


def get_most_read():
    """ Function 2 recover the authors more read
    PARAMS: None
    RETURN: Dict with query results
    """
    c.execute(open(sql_most_read, "r").read())
    results = ({'name': str(row[0]), 'cont': float(row[1])}
               for row in c.fetchall())
    return results


def get_worst_percentages():
    """ Function 2 recover worst percentage date (error > 1%)
    PARAMS: None
    RETURN: Dict with query results
    """
    c.execute(open(sql_wors_percentage, "r").read())
    results = ({'date': str(row[0]), 'perc': float(row[1])}
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
    for result in get_popular_articles():
        print '%s -- %d views' % (result['title'], float(result['cont']),)


def print_most_read():
    """ Function 2 print the authors more read
    PARAMS: None
    RETURN: None
    """
    for result in get_most_read():
        print '%s -- %d views' % (result['name'], float(result['cont']),)


def print_worst_percentage():
    """ Function 2 print worst percentage date (error > 1%)
    PARAMS: None
    RETURN: None
    """
    for result in get_worst_percentages():
        print '%s %2.2f%s' % (result['date'], result['perc'], '%',)


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
