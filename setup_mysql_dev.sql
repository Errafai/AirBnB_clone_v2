-- stup the MySQl database to work on the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create new user called hbnb_dev
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';

-- give it all privilege on hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db TO hbnb_dev@locahost; 

-- give only SELECT privilge to the hbnb_dev on perfomance_schema DATABASE
GRANT SELECT ON performance_schema TO hbnb_dev@locahost;
