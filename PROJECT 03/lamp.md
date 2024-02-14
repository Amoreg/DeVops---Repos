
# WEB STACK ( TECHNOLOGY STACK)

### What is web stack?

#### A web stack includes all of the hardware and software systems that are needed to develop and run a single website, web integration, or mobile application. Software developers can use a pre-configured technology stack as the platform for developing a new application, or they may design a technology stack by choosing and incorporating software that meets their unique requirements.

#### A web stack, also known as a web application stack, is a type of solution stack. It's a collection of software applications that perform a particular task. In this case, the task or purpose is to enable web development, that is, the development of websites and web applications.

#### The term stack is used because the system's components and technologies are built upon one another and work in tandem for web development projects. Moreover, the stack can be used repeatedly for multiple projects. Selecting the right web stack is important because the wrong choices can prove costly.

#  Roles of each component in a web stack? 

#### The web stack's components work together to ensure that the correct information is passed to a requesting client, which is usually an internet browser. 

### 1. OS: The OS in the web stack is the central interface between the hardware and software components of the web application. The most popular OSes for web development are Windows, Linux, Unix, and MacOS.

### WEBSERVER: 

#### The web server delivers web documents and information to the clients who request them. Client requests are passed to the web server via HTTP. The web server then directly processes the requests for static content or refers to a database and script module for dynamic content. Apache, Microsoft Internet Information Services (IIS), and Nginx are all types of web servers.

### THE DATABASE :

#### The database is required to store the data for the web project and make it available to the web server as required. The server requests data using server extensions that generate the output in a suitable format, such as HTML, and forward it to the server. SQL, MySQL, Oracle, and MongoDB are all popular databases for web projects.

### PROGRAMMING LANGUAGE:

#### The programming language, also known as the script interpreter, operates on the client side and within the requesting browser. It's required to realize dynamic websites and web applications. PHP is one of the most popular script interpreters; others include Java, Ruby, Perl and Python.

# TYPES  OF WEB STACK

## LAMP Stack Alternatives

#### Open-source alternatives are:

### MEAN (MongoDB, Express, Angular, Node.js)

### LEMP (Linux, NGINX, MySQL/MariaDB, PHP/Perl/Python)

### LAPP (Linux, Apache, PostgreSQL, PHP)

### LEAP (Linux, Eucalyptus, AppScale, Python)

### LLMP (Linux, Lighttpd, MySQL/MariaDB, PHP/Perl/Python)

### XAMPP (Cross-platform, Apache, MariaDB, PHP, Perl)

#### Non-open source alternatives include:

### WAMP (Windows, Apache, MySQL/MariaDB, PHP/Perl/Python)

### WIMP (Windows, Internet Information Services, MySQL/MariaDB, PHP/Perl/Python)

### MAMP (macOS, Apache, MySQL/MariaDB, PHP/Perl/Python)


### 1. LAMP STACK:

### LAMP stands for Linux, Apache, MySQL, and PHP. Together, they provide a proven set of software for delivering high-performance web applications. Each component contributes essential capabilities to the stack

### LAMP stack components

#### 1. Linux: The operating system. Linux is a free and open-source operating system (OS) that has been around since the mid-1990s. Today, it has an extensive worldwide user base that extends across industries. Linux is popular in part because it offers more flexibility and configuration options than some other operating systems.

#### 2. Apache: The web server. The Apache web server processes requests and serves up web assets via HTTP so that the application is accessible to anyone in the public domain over a simple web URL. Developed and maintained by an open community, Apache is a mature, feature-rich server that runs a large share of the websites currently on the internet. 

#### 3. MySQL: The database. MySQL is an open-source relational database management system for storing application data. With My SQL, you can store all your information in a format that is easily queried with the SQL language. SQL is a great choice if you are dealing with a business domain that is well structured, and you want to translate that structure into the backend. MySQL is suitable for running even large and complex sites. See "SQL vs. NoSQL Databases: What's the Difference?" for more information on SQL and NoSQL databases.

#### 4. PHP: The programming language. The PHP open-source scripting language works with Apache to help you create dynamic web pages. You cannot use HTML to perform dynamic processes such as pulling data out of a database. To provide this type of functionality, you simply drop PHP code into the parts of a page that you want to be dynamic. PHP is designed for efficiency. It makes programming easier—and a bit more fun—by allowing you to write new code, hit refresh, and immediately see the resulting changes without the need for compiling.

## NOTE: LAMP has a classic layered architecture, with Linux at the lowest level. The next layer is Apache and MySQL, followed by PHP. Although PHP is nominally at the top or presentation layer, the PHP component sits inside Apache.

### How LAMP stack elements work together:

#### A high-level look at the LAMP stack order of execution shows how the elements interoperate. The process starts when the Apache web server receives requests for web pages from a user’s browser. If the request is for a PHP file, Apache passes the request to PHP, which loads the file and executes the code contained in the file. PHP also communicates with MySQL to fetch any data referenced in the code. 

#### PHP then uses the code in the file and the data from the database to create the HTML that browsers require to display web pages. The LAMP stack is efficient at handling not only static web pages, but also dynamic pages where the content may change each time it is loaded depending on the date, time, user identity, and other factors. 

#### After running the file code, PHP then passes the resulting data back to the Apache web server to send to the browser. It can also store this new data in MySQL. And of course, all of these operations are enabled by the Linux operating system running at the base of the stack.

## LAMP stack flexibility:

#### Although LAMP uses Linux as the OS, you can use the other components with an alternative OS to meet your specific needs. For example, there is a WAMP stack, which uses Microsoft Windows; MAMP with the Mac OS; and even WIMP, using Windows and the Internet Information Services webserver from Microsoft. 

#### Because LAMP is all open source and non-proprietary, you can avoid lock-in. You have the flexibility to select the right components for specific projects or business requirements.

#### LAMP offers flexibility in other ways as well. Apache is modular in design, and you will find there argit e existing, customizable modules available for many different extensions. These modules range from support for other languages to authentication capabilities. 

#### Another advantage of LAMP is its secure architecture and well-established encryption practices that have been proven in the enterprise.

# LEMP STACK SETUP

### Create a AWS account here: [Aws signup page ](https://aws.amazon.com)..

### Good knowledge of Linux

### Understand ssh kegs. click on this link to learn more on SSH

### Step 1: Configuring your server with Ubuntu Linux AWS EC2 

### Step 2: Installing Apache and Updating the Firewall

### Step 3: Installing and Configuring mysqel Server. ...

### Step 4: Installing MySQL Database Management System. ...

### Step 5: Installing PHP and Setting up Nginx to Use the PHP Processor. ...

### Step 6: Creating a PHP File to Test your LEMP stack.

# Step 1.  Creating an EC2 Instance

### Amazon EC2 basically provides a Virtual Computing environment, where they have pre-configured AMI (Amazon Machine Image) from which you can launch Virtual machines. 

### 1.   Log in to your AWS console.

![AWS console](<images/signin to console.png>)

### 2.   Search for EC2 in the search bar and click on it.

![Search for EC2](<images/search for EC2.png>)

### 3.	Once you are at the EC2 Dashboard, click on Launch to launch an instance.

#### 4.	In the Name and Tags step you can add tags to an instance, here tags help you to enable categorize AWS resources in different ways, for example, by owner, environment, or purpose.

![Identification](<images/Name tag.png>)

### 5.	Choose Ubuntu server 22.04,(HVM),SSD VOLUME architecture 

### 6.	For Select the t2.micro instance type, if you want you may select another instance type but they are chargeable so we choose the t2.micro instance type which is eligible for the free tier and limited resources.

![Instance type](<images/Select instance.png>)

### 7.Create the Key Pair.

![Key pair](<images/key pair.png>)

### 8.	Now select HTTP  and SSH Port under Network Setting.We add http rule here because we need to access our Webpage. As the communication for request and response between Webserver and Browser happens on port 80 which is http.

![Allow SSH & HTTP](<images/Allow ssh and http.png>)

### 9.9.	Now review all the things you have Configured and Click on Launch Instance.

![Start instatnce](<images/EC2 running.png>)

# ACCESSING EC2 FROM THE TERMINAL

## a.	Accessing via Browser using EC2 instance Connect.GUI

![GUI CONNECT TO SERVER](<images/connect.png>)

![Select & connect (GUI)](<images/Select instance and connect.png>)

## CONNECTED INTERFACE (GUI)

![GUI INTERFACE](<images/connected to the server.png>)

## b.	Accessing using COMMAND LINE OR BASH

## SSH into your Ubuntu EC2 instance-For Unix-like systems (Linux/macOS), use the following command:

### ssh -i /path/to/your/private/key.pem ubuntu@your-ec2-public-ip 

![Connected vis Terminal](<images/connected to EC2 via Terminal.png>)

#### (Replace /path/to/your/private/key.pem with the path to your private key file, and your-ec2-public-ip with your EC2 instance's public IP address.)

### For Windows using PuTTY, open PuTTY and enter your EC2 instance's public IP address under "Host Name (or IP address)" field, then navigate to "SSH" > "Auth" and browse to select your private key (.pem) file under "Private key file for authentication". Click "Open" to start the SSH session.For Windows Subsystem for Linux (WSL), you can use the same SSH command as for Unix-like systems.

# step 2.  Installing Apache2 on an AWS Ubuntu EC2 instance

## 1.  SSH into your EC2 instance: Use the terminal and SSH into your Ubuntu EC2 instance using the command provided earlier. Make sure you have the necessary permissions and the correct private key.

## 2.  Update package lists: Before installing Apache2, it's a good practice to update the package lists to ensure you're installing the latest available version. Run the following command:

### sudo apt update

![Connected vis Terminal](<images/sudo update.png>)

## 3.  Install Apache2: Once the package lists are updated, you can install Apache2 using the following command:

### sudo apt install apache2

## 4.  Start Apache2 service: After installation, start the Apache2 service using the following command:

###  sudo systemctl start apache2

## 5.   Enable Apache2 to start on boot: Ensure that Apache2 starts automatically when the system boots up by enabling it with the following command:

###  sudo systemctl enable apache2

## 6.  Check Apache2 status: To verify that Apache2 is running without any issues, you can check its status using the following command:

###   sudo systemctl status apache2

![Apache2 update](<images/sudo systemctl status apache2.png>)

## 7.  Access Apache2 default page: Once Apache2 is installed and running, you can access the default Apache2 landing page by entering your EC2 instance's public IP address in a web browser..

![Apache2 page ](<images/apache2 page.png>)

# How To Find your Server’s Public IP Address

### The curl utility to contact an outside party to tell you how it sees your server. This is done by asking a specific server what your IP address is:

###  curl http://icanhazip.com

#  Step 3.  Installing MYSQL

###   $ sudo apt install mysql-server

![Mysql installed ](<images/install mysql.png>)

###   $ sudo mysql --version

#  To Secure the installation from bug and dangerous lock down

###  $ sudo mysql_secure_installation

### Now read and complete the installtion steps.When it's done test if you are able to logged in to the mysql console

#### $ sudo mysql

![Mysql installed ](<images/Mysql page.png>)

##  Exit the MySQL console, type:

#### mysql> exit

#### Notice that you didn’t need to provide a password to connect as the root user, even though you have defined one when running the mysql_secure_installation script. That is because the default authentication method for the administrative MySQL user is unix_socket instead of password. Even though this might seem like a security concern, it makes the database server more secure because the only users allowed to log in as the root MySQL user are the system users with sudo privileges connecting from the console or through an application running with the same privileges. In practical terms, that means you won’t be able to use the administrative database root user to connect from your PHP application. Setting a password for the root MySQL account works as a safeguard, in case the default authentication method is changed from unix_socket to password.

#### To increased security, it’s best to have dedicated user accounts with less expansive privileges set up for every database, especially if you plan on having multiple databases hosted on your server.

##  MySQL server is now installed and secured.

# Installing PHP to Display Dynamic Content to the End User #

####  So far we have installed Apache web server to host our website and MySQL Database to store and mange the data. PHP will be the layer that displays dynamic content to the user.We need to install the PHP packages that so that the PHP component itself can communicate with the MySQL database

## Step 4.  Insalling PHP

####  To install PHP packages, run the following command:

###  sudo apt install php libapache2-mod-php php-mysql

![pHP installed ](<images/install php.png>)

### Run the “php -v” command after installation to verify that it was successfully installed

![Php check ](<images/php check.png>)

##  With the PHP successfully installed we have completed the LAMP stack sequence and have it fully operational!

# Step 5.   Creating a Virtual Host for your Website #

### When using the Apache web server, you can create virtual hosts (similar to server blocks in Nginx) to encapsulate configuration details and host more than one domain from a single server. In this guide, we’ll set up a domain called your_domain, but you should replace this with your own domain name.

##  First things first we are going to setup a domain and call it “amoreg.org”.

##  By default the Apache web server only allows one server block to be enabled. We are going to setup our own directory for our domain

### Run the following command to create a directory for “amoreg.org”

####  sudo mkdir /var/www/amoreg.org

###  Next, assign ownership of the directory with the $USER environment variable, which will reference your current system user:

####   sudo chown -R $USER:$USER /var/www/amoreg.org

####  Then, open a new configuration file in Apache’s sites-available directory using your preferred command-line editor. Here, we’ll use nano:Save and close the file when you’re done. If you’re using nano, do that by pressing CTRL+X, then Y and ENTER

![Domian directory ](<images/Domain directory.png>)

###  With this VirtualHost configuration, we’re telling Apache to serve your_domain using /var/www/your_domain as the web root directory. If you’d like to test Apache without a domain name, you can remove or comment out the options ServerName and ServerAlias by adding a pound sign (#) the beginning of each option’s lines.

###  Verify the file we created is in the directory by running the “ls” command to have all the files in the directory listed on the command line

### Use a2ensite command  to enable the new virtual host:

#### sudo a2ensite amoreg.org

### To disable the default website that comes installed with Apache. This is required if you’re not using a custom domain name, because in this case Apache’s default configuration would override your virtual host. To disable Apache’s default website, tuse the command below:

##### sudo apache2ctl configtest

![Disable apache2 defult page ](<images/Disable apache2 defult page.png>)

## Reload Apache so these changes take effect:

####  sudo systemctl reload apache2

![Relad apache2 ](<images/reload apapche2.png>)

##  The new website is now active, but the web root /var/www/yamoreg.org is still empty. Create an index.html file in that location to test that the virtual host works as expected:

####  $nano /var/www/amoreg.org/index.html

![Index page ](<images/Index.html.png>)

##  Save and close the file, then go to your browser and access your server’s domain name or IP address:

####  http://server_domain_or_IP

![Index page ](<images/landing page.png>)


# The PHP page provides information about the server and ensures that settings are setup properly. If you see this page, then CONGRATULATIONS that means the PHP installation was SUCCESSFUL!

#  For a secure connection, ensure that connections to your web server are secured, by serving them via HTTPS. In order to accomplish that, you can use Let’s Encrypt to secure your site with a free TLS/SSL certificate.

# Be sure to delete all your resources to avoid any cost. !!.



































