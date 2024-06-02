
# IMPLEMEMTING LOAD BALANCERS WITH NGINX

## Introduction

####  *Assume you own a popular ice cream business with a single cashier. As more people wait up to buy ice cream, the cashier becomes busier, and the line becomes longer. Customers may become frustrated after waiting for an extended period of time, and the cashier may become overwhelmed.

####    Let's now add a load balancer to this situation. When the load balancer sees a long line, it acts as a helpful assistant by deciding to bring in extra cashiers to assist. Orders may be taken independently by each cashier, which speeds up the procedure significantly.

####    So, a load balancer is like a smart organizer that makes sure the workload is spread evenly among multiple servers, making the whole system more efficient and responsive, just like having multiple cashiers to serve customers quickly at an ice cream shop.

# WHAT IS LOAD BALANCER?

#####   Load balancing is a useful mechanism to distribute incoming traffic around several capable Virtual Private servers.By apportioning the processing mechanism to several machines, redundancy is provided to the application -- ensuring fault tolerance and heightened stability. The Round Robin algorithm for load balancing sends visitors to one of a set of IPs. At its most basic level Round Robin, which is fairly easy to implement, distributes server load without implementing considering more nuanced factors like server response time and the visitors’ geographic region.A load balancer is a network device or software application that efficiently distributes incoming network traffic across multiple servers. The primary purpose of a load balancer is to enhance the availability and reliability of applications by ensuring that no single server is overwhelmed with too much traffic, thus distributing the load across multiple servers.

![NIGX](<IMAGES/N1.png>)

####   * The image above show multiple client making request to a load balancer. The load balancer, make a request to a web server and gets a response then give the response back to the client. If the web server not available due to certain reasons which can either be that the server is down or cannot or cannot handle more requests, the load balancer will direct the client response to another server and give response back to the client.

## key features and benefits of load balancers

#####  1. Distribution of Traffic:

######  *Load balancers distribute incoming requests or network traffic across multiple servers to prevent overloading any single server. This ensures that each server shares the load and can handle a portion of the requests.

#####  2. Improved Scalability:

#####   Load balancing allows organizations to scale their applications horizontally by adding more servers to the server pool. This makes it easier to handle increased traffic and ensures that the application remains responsive.

#####  3.  Enhanced Availability and Redundancy:

#####   Load balancers can route traffic away from servers that are experiencing issues or are unavailable. This improves the overall availability of the application and provides a level of redundancy.

#####   4. Session Persistence:

#####    Some load balancers can maintain session persistence, ensuring that a user's requests are consistently directed to the same server. This is important for applications that require continuity, such as those with user login sessions.

#####   5.  SSL Termination:

#####   Load balancers can handle SSL/TLS termination, offloading the encryption and decryption process from the application servers. This helps improve performance and simplifies the management of SSL certificates.

####  Implementation of Load Balancers With Nginx

##### STEP 1:  Provisioning EC2 Instances We will provision 3 EC2 instance, two of these will be our webserver and one will be a load balancer

######      A. Launch 2 EC2 instances and name each "webserver_1" and "webserver_2"

######      B. Launch another EC2 instance and name it "load balancer"

#####  STEP 2: Open New Security Group For Both Webservers and load balancer

######      A. For the webservers and load balancer, go to the security groups

######      B. Edit inbound rules on open port 8000 for our both webserver_1 and webserver_2 and port 80 for our load balancer!

######      C. Allow traffic from anywhere on the open ports

![NIGX](<IMAGES/N2.png>)

#####  STEP 3: Install Apache Webserver i. Open 2 termianls and ssh into webserver 1 and webserver 2

######       A. Update and upgrade package lists

![NIGX](<IMAGES/N1A.png>)

######      B. Install Apache

![NIGX](<IMAGES/N1B.png>)


![NIGX](<IMAGES/N3.png>)

######       C. Confirm Apache has been successfully installed

ii. Add a new listen directive

#####   STEP 4: Configure Apache to Port 8000

######      By default, apache listen on port 80. Since our load balancer will also be listening on port 80, we need to make our webservers listen on port 8000

######    i. Edit port.conf file

![NIGX](<IMAGES/N1C.png>)

######    ii. Add a new listen directive

![NIGX](<IMAGES/N5.png>)

######     iii. Add a new virtualhost statement since a new listen directive has been added

![NIGX](<IMAGES/N1D.png>)

![NIGX](<IMAGES/N6.png>)

######      iv. Reload Apache

######          sudo systemctl reload apache2

#####      STEP 5: Configure Apache to Show Names Of Both Webservers

######        i. open a new index.html file

![NIGX](<IMAGES/N1E.png>)

######        ii. switch to nano editor and past the html file

![NIGX](<IMAGES/N7.png>)

######         iii. Change file ownership of index.html file

![NIGX](<IMAGES/N1F.png>)

######          iv. Overriding the default html file of Apache Webserver

![NIGX](<IMAGES/N1G.png>)

######           v. Restart the webserver to load the new configuration

![NIGX](<IMAGES/N1H.png>)

###  Note: This step should be done for both webserver1 and webserver 2

![NIGX](<IMAGES/N8.png>)

#####    STEP 6: Install and Configure Nginx As A Load Balancer For Both WebServers

#####    In the step, we will configure nginx as a load balancer for webserver 1 and 2

######     i. Update package lists and instal nginx

![NIGX](<IMAGES/N1I.png>)

######     ii. Verify that Nginx is successfully installed

![NIGX](<IMAGES/N1J.png>)

![NIGX](<IMAGES/N9.png>)

######     iii. Edit Nginx load balancer configuration file

![NIGX](<IMAGES/N1K.png>)

######       iv. Paste the configuration file below to configure nginx to act like a load balancer. A screenshot of an example config file is shown below: Make sure you edit the file and provide necessary information like your server IP address etc.

######            upstream backend_servers {

![NIGX](<IMAGES/N1L.png>)

#####   upstream backend_servers defines a group of backend servers. The server lines inside the upstream block list the addresses and ports of your backend servers. proxy_pass inside the location block sets up the load balancing, passing the requests to the backend servers. The proxy_set_header lines pass necessary headers to the backend servers to correctly handle the requests

######    v. Test if nginx configuration is correct

######     sudo nninx -t

![NIGX](<IMAGES/N10.png>)

######     vi. Restart nginx

![NIGX](<IMAGES/N1M.png>)

######     vii. Paste load balancer public Ip address on your web browser to see the content of web server 1 and 2

![NIGX](<IMAGES/N11.png>)










  















































