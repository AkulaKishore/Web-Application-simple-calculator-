# Calculator Web Application.
```
It is a sample web application to calculate addition, substraction, divison 
and multiplication hosted on the ubuntu instance created using Amazon web serivces. 
```


## Getting Started

```
link: ec2-18-216-131-164.us-east-2.compute.amazonaws.com/application/

Go the the above link and give two input numbers and press a submit for calculations.
ouput is displayed below the submit buttons. 

```
### Prerequisites

```
> Pyhton 3.6
> Django framework
```

### Installing on local server. 

```
1. Install latest version of python3
 
 Command: 

 $ sudo apt-get update
 $ sudo apt-get install python3.6
 
 
2. Install Django framework: 
 
 Command:
  
  $ sudo apt install python3-django
  $ django-admin --version
  
  Steps: 
  
 1. clone the repository from the GIT to local. 
 2. migrate the repository to the desired path. 
 3. run manage.py: Command: 
 ### python manage.py runserver
 
 4. run the following server:  http://127.0.0.1:8000/
 ```
 ### Deployment of App to the server. 
 
```
 1. Create a instance "Ubuntu 18.04" in the amazon web service. (you can choose alternate cloud vendor). AWS is offering 1 year free trail. 
 2. Once the instance is launched, download the key (.pem file) and convert to ppk file. this file can be used as to connect to instance using SSH auth. (Default username: ubuntu)
 
 3. Give permsion to the access http and give access to it from "anywhere", in the instance security groups.
 
 4. Install apache web server using following commands:
   
    $ sudo apt update
    $ sudo apt install apache2
    
 To verify apache is installed currently, public DNS in the webserver. A web page with apache details will be shown. 
 
 5. replace the index.html file in the /var/www/html with the application repository. 
 
 Here when we verify again using web browser, A directory is shown up instead of application. It is because, we did not say to the webserver that it is application. for that we need to implement mod_wsgi for providing WSGI
 
  WSGI: The Web Server Gateway Interface (WSGI) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.
 
 mod_wsgi: mod_wsgi is an Apache HTTP Server module by Graham Dumpleton that provides a WSGI compliant interface for hosting Python based web applications under Apache.
 
 installing mod_wsgi for python3: 
 
    sudo apt-get install libapache2-mod-wsgi-py3
    
  Once the installation is done. go to "/etc/apache2/sites-available/000-default.conf" and add the following code:
  
  <VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to

        DocumentRoot /var/www/html/webapp
        WSGIScriptAlias / /var/www/html/webapp/webapp/wsgi.py

        ErrorLog /var/www/html/logs/error.log
        CustomLog /var/www/html/logs/custom.log combined
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
  
  create logs folder in the /var/www/html/logs
  
 Add the following our application python path to the file " apache2.conf"
 
   WSGIPythonPath /var/www/html/webapp
   
   
   Now we integrated our python web application with Apache web server. Now run the public DNS, Our application will be shown. 
  ``` 
  
## Built With
```
* Django: The web framework used
* Amazon web services(AWS) : for launching instance
* Python: Programing language to develop web application
* HTML, CSS - templates
```
## Authors
```
   SAI KISHORE AKULA (M12951663) - University Of Cincinnati

```
## REFERENCE: 
```
* https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/
* https://www.youtube.com/watch?v=VNBpdT0N8hw
```
