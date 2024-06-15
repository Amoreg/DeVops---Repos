
## Implementing Wordpress Website With LVM Storage Management

### Introduction

######     WordPress is a content management system (CMS) that allows you to host and build websites. WordPress contains plugin architecture and a template system, so you can customize any website to fit your business, blog, portfolio, or online store. The focus of this tutorial is not on how to build websites with wordpress

####  What Is LVM Storage?

######      LVM stands for Logical Volume Manager, is a device mapper framework that provides logical volume management for the Linux kernel. Most modern Linux distributions are LVM-aware to the point of being able to have their root file systems on a logical volume.which is a technology used on Linux systems to manage storage devices and provide advanced features for managing disk space, such as logical volumes, snapshots, and volume resizing. LVM allows for more flexible and dynamic management of disk partitions compared to traditional partitioning schemes.LVM provides a flexible and efficient way to manage storage resources on Linux systems, offering advanced features that enhance data management and system flexibility. It is particularly useful in environments where storage requirements are dynamic and may change over time.

####    Key Components of LVM:

######     1.  Physical Volumes (PVs):These are physical storage devices (e.g., hard drives, SSDs) or partitions that are initialized for use with LVM. Each physical volume is assigned a unique identifier.

######     2.  Volume Groups (VGs):These are created by combining one or more physical volumes. A volume group represents a pool of storage that can be divided into logical volumes.

######     3.  Logical Volumes (LVs):These are virtual partitions created from free space within volume groups. They can be thought of as equivalent to partitions in traditional disk partitioning schemes (e.g., ext4 partitions). Logical volumes can be resized dynamically without requiring downtime.

####   Advantages of LVM:

######     Flexibility: LVM allows administrators to resize logical volumes dynamically, enabling easy allocation and reallocation of disk space without the need to repartition disks.

######     Volume Management: LVM simplifies storage management by abstracting physical storage devices into logical volumes, providing a unified view of storage across multiple disks.

######     Snapshots: LVM supports creating snapshots, which are read-only copies of a logical volume at a specific point in time. Snapshots are useful for backups and testing without affecting the original data.

######      Striping and Mirroring: LVM supports RAID-like functionality such as striping (to improve performance) and mirroring (to provide data redundancy) at the volume group level.

####     Common LVM Commands:

######      pvcreate: Initializes a physical volume for use with LVM. vgcreate: Creates a volume group by combining one or more physical volumes. lvcreate: Creates a logical volume within a volume group. lvresize: Resizes an existing logical volume. lvextend / lvreduce: Extends or reduces the size of a logical volume. lvdisplay: Displays information about logical volumes.

####   Use Cases for LVM:

######    1. Server Virtualization: LVM is commonly used in virtualization environments to manage disk resources for virtual machines.

#####     2.  Database Servers: LVM allows for easy resizing of partitions used by databases to accommodate changing storage requirements.

#####     3.  Backup Systems: LVM snapshots can be used for creating consistent backups of data without interrupting ongoing operations.

####   Implementing Wordpress Web Solution

######    Three-tier Architecture Generally, web, or mobile solutions are implemented based on what is called the Three-tier Architecture.

####    Three-tier Architecture is a client-server software architecture pattern that comprise of 3 separate layers.

###   1. Presentation Layer (PL): This is the user interface such as the client server or browser on your laptop.

###   2. Business Layer (BL): This is the backend program that implements business logic. Application or Webserver

###   3. Data Access or Management Layer (DAL): This is the layer for computer data storage and data access. Database Server or File System Server such as FTP server, or NFS Server.

####   Your 3-Tier Setup

####   *  A Laptop or PC to serve as a client

####   *  An EC2 Linux Server as a web server (This is where you will install WordPress)

####   *  An EC2 Linux server as a database (DB) serve

######   1.  Create an AWS instance using RedHat Distribution

#####    The EC2 instance will serve as a Web Server, create 3 volumes in the same AZ as the Web Srver EC2, each of 10GB.

#####   2. Attach the three volumes one by one to your Webserver EC2 instance

![LVM](<IMAGES/01.png>)

#####   3.  Open up the Linux terminal to begin configuration

#####  4.   Use lsblk command to inspect what block devices are attached to the server. Notice names of your newly created devices. All devices in Linux reside in /dev/ directory. Inspect it with ls /dev/ and make sure you see all 3 newly created block devices there – their names will likely be xvdf, xvdh, xvdp.

![LVM](<IMAGES/02.png>)

![LVM](<IMAGES/03.png>)

#####  5.  Use df -h command to see all mounts and free space on your server

![LVM](<IMAGES/04.png>)

######  6.  Use gdisk utility to create a single partition on each of the 3 disks

######      sudo gdisk /dev/xvdf

![LVM](<IMAGES/05.png>)

![LVM](<IMAGES/06.png>)

![LVM](<IMAGES/07.png>)

######     7.  Use lsblk utility to view the newly configured partition on each of the 3 disks.

![LVM](<IMAGES/08.png>)

######     8.  Install lvm2 package using sudo yum install lvm2. Run sudo lvmdiskscan command to check for available partitions.

![LVM](<IMAGES/09.png>)

![LVM](<IMAGES/10.png>)

######  9.  Use pvcreate utility to mark each of 3 disks as physical volumes (PVs) to be used by LVM.

![LVM](<IMAGES/11.png>)

######  10.   Use vgcreate utility to add all 3 PVs to a volume group (VG). Name the VG webdata-vg

######    sudo vgcreate webdata-vg /dev/xvdh1 /dev/xvdg1 /dev/xvdf1

![LVM](<IMAGES/12.png>)

######   11.   Verify that VG has been created

![LVM](<IMAGES/13.png>)

######   12.   Use lvcreate utility to create 2 logical volumes. apps-lv (Use half of the PV size), and logs-lv Use the remaining space of the PV size. NOTE: apps-lv will be used to store data for the Website while, logs-lv will be used to store data for logs.

######     sudo lvcreate -n apps-lv -L 14G webdata-vg sudo lvcreate -n logs-lv -L 14G webdata-vg

![LVM](<IMAGES/14.png>)

######     Verify that your Logical Volume has been created successfully by running sudo lvs

![LVM](<IMAGES/15.png>)

######    14.   Verify the entire setup

![LVM](<IMAGES/16.png>)

![LVM](<IMAGES/17.png>)

######     15.  Use mkfs.ext4 to format the logical volumes with ext4 filesystem

![LVM](<IMAGES/AB.png>)

![LVM](<IMAGES/18.png>)

######   16.  Create /var/www/html directory to store website files

######       sudo mkdir -p /var/www/html

######   17.  Create /home/recovery/logs to store backup of log data

######        sudo mkdir -p /home/recovery/logs

######   18.   Mount /var/www/html on apps-lv logical volume

######         sudo mount /dev/webdata-vg/apps-lv /var/www/html/

######  19.   Use rsync utility to backup all the files in the log directory /var/log into /home/recovery/logs (This is required before mounting the file system)

######        sudo rsync -av /var/log/. /home/recovery/logs/

![LVM](<IMAGES/19.png>)

######   20.  Mount /var/log on logs-lv logical volume. (Note that all the existing data on /var/log will be deleted. That is why step 15 above is very important)

######     sudo mount /dev/webdata-vg/logs-lv /var/log

#####    21.  Restore log files back into /var/log directory

######      sudo rsync -av /home/recovery/logs/. /var/log

![LVM](<IMAGES/20.png>)

####   22.   UPDATE THE /ETC/FSTAB FILE

######     The UUID of the device will be used to update the /etc/fstab file;

![LVM](<IMAGES/AC.png>)

![LVM](<IMAGES/21.png>)

![LVM](<IMAGES/AD.png>)
 
![LVM](<IMAGES/AQ.png>)

#####    Update /etc/fstab in this format using your own UUID and remember to remove the leading and ending quotes.

![LVM](<IMAGES/22.png>)

#####    Test the configuration and reload the daemon

######      sudo mount -a

######      sudo systemctl daemon-reload

![LVM](<IMAGES/22.png>)

#####     Verify your setup by running df -h, output must look like this:

![LVM](<IMAGES/24.png>)

Prepare the Database Server
Launch a second RedHat EC2 instance that will have a role – ‘DB Server’ Repeat the same steps as for the Web Server, but instead of apps-lv create db-lv and mount it to var/www/db directory instead of /var/www/html/.

## Install WordPress On EC2 WebServer
Update the repository

sudo yum -y update

![LVM](<IMAGES/25.png>)

Install wget, Apache and it’s dependencies

sudo yum -y install wget httpd php php-mysqlnd php-fpm php-json

![LVM](<IMAGES/26.png>)

Start Apache

sudo systemctl enable httpd
sudo systemctl start httpd

![LVM](<IMAGES/27.png>)

To install PHP and it’s depemdencies

![LVM](<IMAGES/AK.png>)

![LVM](<IMAGES/28.png>)

Restart Apache

sudo systemctl restart httpd

Download Wordpress and Copy Wordpress to var/www/html

![LVM](<IMAGES/29.png>)

Configure SELinux Policies

![LVM](<IMAGES/AM.png>)

## Install MySQL On EC2 DB Server

#####      sudo yum update sudo yum install mysql-server -y

![LVM](<IMAGES/30.png>)

Verify that the service is up and running by using sudo systemctl status mysqld, if it is not running, restart the service and enable it so it will be running even after reboot:

![LVM](<IMAGES/31.png>)

##   Configure DB To Work With WordPress

![LVM](<IMAGES/32.png>)

![LVM](<IMAGES/33.png>)

Configure WordPress To Connect To Remote Database. Edit inbound rule and open port 3306 on database server and allow connection from only our database server.

![LVM](<IMAGES/34.png>)

Install MySQL client and test that you can connect from your Web Server to your DB server by using mysql-client

![LVM](<IMAGES/35.png>)

![LVM](<IMAGES/36.png>)

Verify if you can successfully execute SHOW DATABASES; command and see a list of existing databases.

Change permissions and configuration so Apache could use WordPress:

Enable TCP port 80 in Inbound Rules configuration for your Web Server EC2 (enable from everywhere 0.0.0.0/0 or from your workstation’s IP)

Verify Database Credentials
Check the wp-config.php file in your WordPress webserver to ensure that the database credentials are correct.

sudo nano /var/www/html/wordpress/wp-config.php

Verify the values below

![LVM](<IMAGES/AL.png>)

Try to access from your browser the link to your WordPress http:///wordpress/

![LVM](<IMAGES/37.png>)

![LVM](<IMAGES/380.png>)

![LVM](<IMAGES/390.png>)

![LVM](<IMAGES/40.png>)























