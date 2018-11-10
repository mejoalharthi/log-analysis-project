# Log Analysis Project

 This project for build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information.
 The questions the reporting tool should answer:
 1. What are the most popular three articles of all time?
 2. Who are the most popular article authors of all time?
 3. On which days did more than 1% of requests lead to errors?

## Getting Started with Requires Software Installation

1. Install Vagrant: [Vagrant](https://www.vagrantup.com/downloads.html)
2. Install Virtual Machine: [VM](https://www.virtualbox.org/wiki/Downloads)
3. Download a FSND virtual machine: [FDNS-VM](https://github.com/udacity/fullstack-nanodegree-vm)
4. Download Git Bash: [GitBash](https://git-for-windows.github.io/) for windows, On Mac or Linux systems, you can use the
built-in
5. Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
6. Download or Clone this project
7. Unzip last two files and Make a folder for this project named "log-analysis-project" then copy all it into the vagrant directory.

Open Git bash or Terminal navigate to the project folders by following this instructions:
  ```
  cd vagrant
  vagrant up
  vagrant ssh
  cd /vagrant
  cd log-analysis-project
  ```

### Load the Data into Database

1. Load the data from the “newsdata.sql” by using the following command: Note that we are
using PostgreSQL for this project:
```
psql -d news -f newsdata.sql
```
2. Once you have the data loaded into your database, connect to your database using:
```
psql -d news
```
Now you can Run the project!

## Output

```
Queries Output:
 Question1:
"Candidate is jerk, alleges rival"- 338647 views
"Bears love berries, alleges bear"- 253801 views
"Bad things gone, say good people"- 170098 views

 Question2:
"Ursula La Multa"- 507594 views
"Rudolf von Treppenwitz"- 423457 views
"Anonymous Contributor"- 170098 views
"Markoff Chaney"- 84557 views

 Question3:
"July 17, 2016"- 2.3% errors
```
