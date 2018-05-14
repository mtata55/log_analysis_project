# Log Analysis Project

**Description**<br />
Source code for running queries on a PostgreSQL database using the psycopg2 module for Udacity Full Stack Web Developer Project.<br /> 

**Contents:**<br />
README.md (This document)<br />
newsdata.py (Python code) <br />


**Prerequisites:**<br />
Python 3 <br />
PostgreSQL<br />
newsdata.sql (SQL file to create database. Not included as size > 100 MB)
Note: this project is run as per Udacity requirements using Vagrant + VirtualBox. If you do not have this setup this may not work. 

**Getting Started:**<br />
Connect to the vagrant Virtual Machine using vagrant up. Navigate to the /vagrant folder using cd /vagrant.<br />
Copy newsdata.py and newsdata.sql to the /vagrant folder. <br />
Run newsdata.sql to create the required news database and tables.<br />
Connect to the news database using psql -d news <br />

**Create 2 additional views by running the following commands:** <br />
CREATE VIEW errors as SELECT date_trunc('day', time) as day, count(status) as visits from log where status != '200 OK' group by day;<br />
CREATE VIEW total_visits as SELECT date_trunc('day', time) as day, count(status) as visits from log group by day;<br />

The errors view shows the day wise count of requests that returned a status other than '200 OK'<br />
The total_visits view shows the day wise total views<br />

These views are used to run the last query to compute the error percentage. <br />

Run newsdata.py in the terminal. Output will be printed to the terminal as the question followed by the result of the query to answer the question.


**Installation :**<br />
Clone the repository or unzip the folder contents on to the /vagrant folder your local drive / Virtual Machine.


**Acknowledgements**<br />
Udacity 

