# project 3

* The IP address : `52.59.31.195`
* ssh port	 : `2200`
* website url	 : `52.59.31.195:80`
* summary of software installed and configuration changes made:
  - updated all the packages in the server machine
  - changed ssh port from `22` to `2200`
  - configured the firewall to allow ports `80 , 123 , 2200`
  - created `grader` user and gave `grader` sudo access
  - generated ssh key to `grader` putting the public key into server's `.ssh/authorized_keys.save` file
  - configured ssh configuration to disallow `PasswordAuthentication`
  - configured the local time zone to UTC
  - installed and configured `apache` webserver
  - installed and configured `python mod_wsgi`
  - installed `Postgresql`
  - created new postgresql user called `catalog`
  - installed `git` and cloned the application from github repository
  - installed packges: `python-pip httplib2 requests --upgrade oauth2client sqlalchemy flask libpq-dev psycopg2` for deploying  flask application on ubuntu
  - configured virtual host
  - added `app.wsgi`
