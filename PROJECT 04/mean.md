
# WEB STACK IMPLEMENTATIOM (LEMP STACK) NGINX

### What is NGINX

#### NGINX is open-source web server software used for reverse proxy, load balancing, and caching. It provides HTTPS server capabilities and is mainly designed for maximum performance and stability. It also functions as a proxy server for email communications protocols, such as IMAP, POP3, and SMTP. 

# Benefits of NGINX

#### 1. Reduces the waiting time to load a website. You don’t have to worry about high latency on your websites, therefore providing a good user experience. 

#### 2. Speeds up performance by routing traffic to web servers in a way that increases the overall speed. This feature provides a good browsing experience to your users.

#### 3. Acts as an inexpensive and robust load balancer.

#### 4. Offers scalability and the ability to handle concurrent requests. 

#### 5. Allows on-the-fly upgrades without downtime.

#  USE CASES

####  - A web server. This is the most common because of its performance and scalability.

####  - A reverse proxy server. NGINX does this by directing the client’s request to the appropriate back-end server. 

####  - A load balancer. It automatically distributes your network traffic load without manual configuration.

####  - An API gateway. This is useful for request routing, authentication, and exception handling.

####  - A firewall for web applications. This protects your application by filtering incoming and outgoing network requests on your server.

####  - A cache. NGINX acts as a cache to help store your data for future requests.

####  - Protection against distributed-denial-of-service (DDoS) attacks.

####  - K8s. These automate deployments and scaling and manage containerized applications.

####  - A sidecar proxy. This routes traffic to and from the container it runs alongside.

# Step 1 –  Installing the Nginx Web Server

## Prerequisites

####  we need  to enable port 80 and 443 ( Http nad Https)for Nginx from AWS you should have a regular, non-root user with sudo privileges configured on your server for installation  

# To Installing the Nginx Web server . Run:

#### sudo apt update

![software update](<Images/update.png>)

#### sudo apt install nginx

![Ngnix installed](<Images/Nginx installed.png>)
 
#### Before testing Nginx, the firewall software needs to be adjusted to allow access to the service. Nginx registers itself as a service with UFW upon installation, making it straightforward to allow Nginx access. If you have the ufw firewall enabled, you will need to allow connections to Nginx. Nginx registers a few different UFW application profiles upon installation. To check which UFW profiles are available, run: sudo ufw app list

![Http Allowed](<Images/allow http on Ec2.png>)

##### ##### It is recommended that you enable the most restrictive profile that will still allow the traffic you need. Since you haven’t configured SSL for your server in this guide, you will only need to allow regular HTTP traffic on port 80. Enable this by typing: run:  sudo ufw allow 'Nginx HTTP'

#### To verify the change by running:

#### sudo ufw status

![LAMP DESIGN](<images/LAMP design.png>)

#### verify the the Ngnix is runing, Run: $ sudo systemctl status nginx

![LAMP DESIGN](<Images/ngnix status.png>)

### To re-enable the service to start up at boot, you can type:

####  sudo systemctl enable nginx

# Access the server on the browser

####  With the new firewall rule added, you can test if the server is up and running by accessing your server’s domain name or public IP address in your web browser.

### http://server_domain_or_IP

![Webpage](<Images/webpage.png>)


# Step 2 — Installing MySQL  #

#### After the web server is operational, you must install the database system in order to store and manage content for your website. A well-liked database management system used in PHP settings is MySQL. to install run: 

####  sudo apt install mysql-server

![Mysql installed](<Images/Mysql installed.png>)

##### Press Y to confirm installation when prompted, and then hit ENTER.

##### It is advised that you execute a security script that is pre-installed with MySQL after the installation is complete. This script will lock down access to your database system and remove several unsafe default settings. To initiate the interactive script, execute:

#### sudo mysql_secure_installation

![secure Mysql](<Images/secured mysql page.png>)

#####   This will ask if you want to configure the VALIDATE PASSWORD PLUGIN.

### To connect to the MySQL server as the administrative database user root, which is inferred by the use of sudo when running this command. Run:

####  sudo mysql

![Mysql login page](<Images/mysql confirmed.png>)

## To secure and remove insecure default setting and lock down the data base syastem, it is recommended the we run a secutity script that come pre install with MySQL.before the scrpit we set a root user, using musql_native_ password as default authentication method. Run:

####   ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'PassWord.1';

#### To exit the MySQL console, Run:

#####  mysql> exit.

## to start the intractive script run:

####  $ sudo mysql_secure_installation    ----This will ask if you want to configure the VALIDATE PASSWORD PLUGIN.

#####  --Note: Enabling this feature is something of a judgment call. If enabled, passwords which don’t match the specified criteria will be rejected by MySQL with an error. It is safe to leave validation disabled, but you should always use strong, unique passwords for database credentials.

####  Answer Y for yes, or anything else to continue without enabling.

##### Regardless of whether you chose to set up the VALIDATE PASSWORD PLUGIN, your server will next ask you to select and confirm a password for the MySQL root user. This is not to be confused with the system root. The database root user is an administrative user with full privileges over the database system. Even though the default authentication method for the MySQL root user dispenses the use of a password, even when one is set, you should define a strong password here as an additional safety measure. We’ll talk about this in a moment.If you enabled password validation, you’ll be shown the password strength for the root password you just entered and your server will ask if you want to continue with that password. If you are happy with your current password, enter Y for “yes” at the prompt:


#####  Notice that you didn’t need to provide a password to connect as the root user, even though you have defined one when running the mysql_secure_installation script. That is because the default authentication method for the administrative MySQL user is unix_socket instead of password. Even though this might look like a security concern at first, it makes the database server more secure because the only users allowed to log in as the root MySQL user are the system users with sudo privileges connecting from the console or through an application running with the same privileges. In practical terms, that means you won’t be able to use the administrative database root user to connect from your PHP application. Setting a password for the root MySQL account works as a safeguard, in case the default authentication method is changed from unix_socket to password.

##### For increased security, it’s best to have dedicated user accounts with less expansive privileges set up for every database, especially if you plan on having multiple databases hosted on your server.

## Your MySQL server is now installed and secured. Next, we’ll install PHP, the final component in the LEMP stack.

# Step 4 — Configuring Nginx to Use the PHP Processor

###  -On Ubuntu 20.04, Nginx is set up to serve documents from a directory at /var/www/html and has one server block enabled by default. While this is effective for one site, managing many sites might make it more challenging. /var/www/html will remain as the default directory to be served in the event that a client request does not match any other sites; instead, we will establish a directory structure within /var/www for the your_domain website.

### Create the root web directory for your_domain as follows: 

#### $ sudo mkdir /var/www/your_domain

![Config directory](<Images/directory for conig.png>)
f
###  Next, assign ownership of the directory with the $USER environment variable, which will reference your current system user:

###  $ sudo chown -R $USER:$USER /var/www/your_domain

### Then, open a new configuration file in Nginx’s sites-available directory using your preferred command-line editor. Here, I use nano:

#### sudo nano /etc/nginx/sites-available/your_domain

![Configuration file](<Images/config file.png>)


##### -- Here’s what each of these directives and location blocks do:

##### 1. listen — Defines what port Nginx will listen on. In this case, it will listen on port 80, the default port for HTTP.

##### 2. root — Defines the document root where the files served by this website are stored.

##### 3. ndex — Defines in which order Nginx will prioritize index files for this website. It is a common practice to list index.html files with a higher precedence than index.php files to allow for quickly setting up a maintenance landing page in PHP applications. You can adjust these settings to better suit your application needs.

##### 4. server_name — Defines which domain names and/or IP addresses this server block should respond for. Point this directive to your server’s domain name or public IP address.

##### 5. location / — The first location block includes a try_files directive, which checks for the existence of files or directories matching a URI request. If Nginx cannot find the appropriate resource, it will return a 404 error.

##### 6. location ~ \.php$ — This location block handles the actual PHP processing by pointing Nginx to the fastcgi-php.conf configuration file and the php7.4-fpm.sock file, which declares what socket is associated with php-fpm.

##### 6. location ~ /\.ht — The last location block deals with .htaccess files, which Nginx does not process. By adding the deny all directive, if any .htaccess files happen to find their way into the document root ,they will not be served to visitors

### Activate your configuration by linking to the config file from Nginx’s sites-enabled directory:

#### $ sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/

### Then, unlink the default configuration file from the /sites-enabled/ directory:

#### $ sudo unlink /etc/nginx/sites-enabled/default

###  This will tell Nginx to use the configuration next time it is reloaded. You can test your configuration for syntax errors by typing:

#### $ sudo nginx -t

![Directory for conf ](<Images/directory for config file.png>)

### Reload Nginx to apply the changes:

#### $ sudo systemctl reload nginx

##  Your new website is now active, but the web root /var/www/your_domain is still empty. Create an index.html file in that location so that we can test that your new server block works as expected:

#### $ nano /var/www/your_domain/index.html

![Web directory](<Images/web root directory.png>)

## Access the site on the brower with the serve public ip address:

##### http://server_domain_or_IP

![Mysql login page](<Images/output on browser.png>)


## The LEMP stack is now fully configured. 

























