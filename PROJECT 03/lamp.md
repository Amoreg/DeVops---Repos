
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

### Step 2: Installing and Configuring mysqel Server. ...

### Step 3: Installing MySQL Database Management System. ...

### Step 4: Installing PHP and Setting up Nginx to Use the PHP Processor. ...

### Step 5: Creating a PHP File to Test your LEMP stack.














