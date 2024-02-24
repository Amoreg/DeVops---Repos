
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

#### sudo apt install nginx
 
#### Before testing Nginx, the firewall software needs to be adjusted to allow access to the service. Nginx registers itself as a service with UFW upon installation, making it straightforward to allow Nginx access. If you have the ufw firewall enabled, you will need to allow connections to Nginx. Nginx registers a few different UFW application profiles upon installation. To check which UFW profiles are available, run: sudo ufw app list

##### ##### It is recommended that you enable the most restrictive profile that will still allow the traffic you need. Since you haven’t configured SSL for your server in this guide, you will only need to allow regular HTTP traffic on port 80. Enable this by typing: run:  sudo ufw allow 'Nginx HTTP'

#### To verify the change by running:

#### sudo ufw status

#### verify the the Ngnix is runing, Run: $ sudo systemctl status nginx

### To re-enable the service to start up at boot, you can type:

####  sudo systemctl enable nginx

# Access the server on the browser

####  With the new firewall rule added, you can test if the server is up and running by accessing your server’s domain name or public IP address in your web browser.

### http://server_domain_or_IP


# Step 2 — Installing MySQL  #

#### After the web server is operational, you must install the database system in order to store and manage content for your website. A well-liked database management system used in PHP settings is MySQL. to install run: 

####  sudo apt install mysql-server

##### Press Y to confirm installation when prompted, and then hit ENTER.

##### It is advised that you execute a security script that is pre-installed with MySQL after the installation is complete. This script will lock down access to your database system and remove several unsafe default settings. To initiate the interactive script, execute:

#### sudo mysql_secure_installation

#####   This will ask if you want to configure the VALIDATE PASSWORD PLUGIN.

### To connect to the MySQL server as the administrative database user root, which is inferred by the use of sudo when running this command. Run:

####  sudo mysql

## To secure and remove insecure default setting and lock down the data base syastem, it is recommended the we run a secutity script that come pre install with MySQL.before the scrpit we set a root user, using musql_native_ password as default authentication method. Run:

####   ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'PassWord.1';

#### To exit the MySQL console, Run:

#####  exit.














