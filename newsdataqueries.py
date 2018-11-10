#!/usr/bin/env python3
import psycopg2
DBName = "news"
# FirstQuestion:What are the most popular three articles of all time?
firstQuery = """ SELECT articles.title, Count(log.path) AS Views
FROM articles, log
WHERE '/article/' || articles.slug = log.path
GROUP BY articles.title
ORDER BY Views desc
LIMIT 3; """

# Who are the most popular article authors of all time?
SecondQuery = """ SELECT authors.name ,Count(log.path) AS views
FROM authors,articles,log
WHERE articles.author = authors.id
AND '/article/'||articles.slug = log.path
GROUP BY authors.name
ORDER BY Views desc;"""

# On which days did more than 1% of requests lead to errors?
ThirdQuery = """ SELECT ErrorsRequest.Day ,
(ErrorsRequest.TotalErrors ::FLOAT/Total.TotalRequest::FLOAT)*100
 AS Errorpercentage
FROM (
SELECT Count(status) AS TotalErrors , time ::date AS Day
FROM log
WHERE status LIKE '%404%'
GROUP BY Day
ORDER BY Day) as ErrorsRequest
JOIN(
SELECT Count(status) AS TotalRequest, time ::date AS Day
FROM log
GROUP BY Day
ORDER BY Day) AS Total
ON ErrorsRequest.Day = Total.Day
WHERE (ErrorsRequest.TotalErrors::FLOAT/Total.TotalRequest::FLOAT)*100> 1.0
ORDER BY Errorpercentage DESC;"""


def ExecuteQueries(query):
    dbconn = psycopg2.connect("dbname="+DBName)
    cursor = dbconn.cursor()
    cursor.execute(query)
    fetchAllResult = cursor.fetchall()
    dbconn.close()
    return fetchAllResult


def PrintQuereis():
    print("Queries Output: \n Question1:")
    result = ExecuteQueries(firstQuery)
    #  Print Results
    for title, Views in result:
        print("\"" + str(title) + "\"- " + str(Views) + " views")
    print("\n Question2:")
    result = ExecuteQueries(SecondQuery)
    for name, Views in result:
        print("\"" + str(name) + "\"- " + str(Views) + " views")
    print("\n Question3:")
    result = ExecuteQueries(ThirdQuery)
    for Day, Errorpercentage in result:
        errors = str(round(Errorpercentage, 1)) + "% errors"
        print("\"" + str(Day.strftime('%B %d,%Y')) + "\"- " + errors)


PrintQuereis()
