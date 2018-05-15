# Log Analysis Project

## Description
Source code for running queries on a PostgreSQL database using the psycopg2 module for the Udacity Full Stack Web Developer Project. 

The database is for a fictional news website and has 3 tables as follows:

* log - contains access data, time, ip addresses and request status for url paths on website
* articles - contains data on author, title, slug, time of publishing, content
* authors - contains data on author name, bio

The project requirements are to answer the following questions:

* What are the most popular three articles of all time? 
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors? 

## Contents:
* README.md (This document)
* newsdata.py (Python code) 
* Vagrantfile (To configure environment)
* views_script.sql (Script to create table views used for query. Optional)


## Prerequisites:
* Python 
* PostgreSQL
* newsdata.sql (SQL file to create database. Not included as size > 100 MB)

You can download the newsdata.sql file from [this link](https://goo.gl/emtXek).

Note: This project is run as per Udacity requirements using Vagrant + VirtualBox. If you do not have this setup this may not work.

You can learn more about and download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) from the links.

## Getting Started:
The instructions below assume that you have setup the environment using the Vagrantfile and have a virtual machine running.

Copy newsdata.py and newsdata.sql to the /vagrant folder of your local machine.

Connect to the vagrant Virtual Machine using vagrant up and vagrant ssh. Navigate to the /vagrant folder using cd /vagrant. You should see newsdata.py and newsdata.sql.
 
Run newsdata.sql using the following command to setup the table schema and insert the data into the tables.

    psql -d news -f newsdata.sql


Connect to the news database using the following command: 

    psql -d news 

### Create 2 additional views by running the following commands: 

```sql
CREATE VIEW errors AS
SELECT date_trunc('day', time) as day, count(status) as visits
FROM log
WHERE status != '200 OK'
GROUP BY day;

CREATE VIEW total_visits AS
SELECT date_trunc('day', time) as day, count(status) as visits
FROM log
GROUP BY day;
```

Alternatively you can run the optional script file views_script.sql using the following command:

    psql -d news -f views_script.sql

The errors view shows the day wise count of requests that returned a status other than '200 OK'

The total_visits view shows the day wise total views

These views are used to run the last query to compute the error percentage. 

Run newsdata.py in the terminal. Output will be printed to the terminal as the question followed by the result of the query to answer the question.


## Installation :
Clone the repository or unzip the folder contents on to the /vagrant folder your local drive / Virtual Machine.


## Acknowledgements
Udacity 

