-- Create replica user and password with replication client grant

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'hbtn7319';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
