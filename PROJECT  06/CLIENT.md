# Understanding Client Server Architecture With MySQL As RDBMS

![CLIENT-SERVER ](<IMAGES/CLIENT-SERVER.png>)

# What is Client Server Architecture?

#### Client Server Architecture is a computing model in which the server hosts, delivers, and manages most of the resources and services to be consumed by the client. This type of architecture has one or more client computers connected to a central server over a network or internet connection. This system shares computing resources. Client/server architecture is also known as a networking computing model or client/server network because all the requests and services are delivered over a network.Client-server architecture is an architecture of a computer network in which many clients (remote processors) request and receive service from a centralized server (host computer). Client computers provide an interface to allow a computer user to request services of the server and to display the results the server returns. Servers wait for requests to arrive from clients and then respond to them. Ideally, a server provides a standardized transparent interface to clients so that clients need not be aware of the specifics of the system (i.e., the hardware and software) that is providing the service. Clients are often situated at workstations or on personal computers, while servers are located elsewhere on the network, usually on more powerful machines. This computing model is especially effective when clients and the server each have distinct tasks that they routinely perform. In hospital data processing, for example, a client computer can be running an application program for entering patient information while the server computer is running another program that manages the database in which the information is permanently stored. Many clients can access the server’s information simultaneously, and, at the same time, a client computer can perform other tasks, such as sending e-mail. Because both client and server computers are considered intelligent devices, the client-server model is completely different from the old “mainframe” model, in which a centralized mainframe computer performed all the tasks for its associated “dumb” terminals

# The Purpose of Client/Server Architecture

#### We are in an era where information technology plays a critical role in business applications, considered as an area an organization would highly invest in order to widen the opportunities available to compete the global market. “A competitive global economy will ensure obsolescence and obscurity to those who cannot or are unwilling to compete”(Client/Server Architecture,2011), according to this statement it’s necessary for organizations sustain its market position by reengineering prevailing organizational structures and business practices to achieve their business goals. In short it’s a basic need to evolve with the change of technological aspects. Therefore organizations should undergo a mechanism to retrieve and process its corporate data to make business procedures more efficient to excel or to survive in the global market. The client/server model brings out a logical perspective of distributed corporative processing where a server handles and processes all client requests. This can be also viewed as a revolutionary milestone to the data processing industry. “Client/server computing is the most effective source for the tools that empower employees with authority and responsibility.”(Client/Server Architecture,2011) “Workstation power, workgroup empowerment, preservation of existing investments, remote network management, and market-driven business are the forces creating the need for client/server computing”. (Client/Server Architecture,2011) Client/server computing has a vast progression in the computer industry leaving any area or corner untouched. Often hybrid skills are required for the development of client/server applications including database design, transaction processing, communication skills, graphical user interface design and development etc. Advanced applications require expertise of distributed objects and component infrastructures. Most commonly found client/server strategy today is PC LAN implementation optimized for the usage of group/batch. This has basically given threshold to many new distributed enterprises as it eliminates host-centric computing.

# Characteristics of a Client-Server Architecture

#### * Client and server machines need different amount of hardware and software resources.

#### * Client and server machines may belong to different vendors.

#### * Horizontal scalability (increase of the client machines) and vertical scalability (migration to a more powerful server or to a multi-server solution)

#### * A client or server application interacts directly with a transport layer protocol to establish communication and to send or receive information.

#### * The transport protocol then uses lower layer protocols to send or receive individual messages. Thus, a computer needs a complete stack of protocols to run either a client or a server.

#### * A single server-class computer can offer multiple services at the same time; a separate server program is needed for each service.

# Three-tier Client Server Architecture

#### * A client that interacts with the user

#### * An application server that contains the business logic of the application

#### * A resource manager that stores data

#  Overview of how this architecture works with MySQL:

# Components:

## Client:

#### A client-server network is the medium through which clients access resources and services from a central computer, via either a local area network (LAN) or a wide-area network (WAN), such as the Internet.The client is the end-user device or application that initiates requests to the server. Clients can be various types, such as desktop applications, web browsers, mobile apps, or other devices that need access to data stored in the MySQL database.

## Server:

#### A server is a computer program or device that provides a service to another computer program and its user, also known as the client. In a data center, the physical computer that a server program runs on is also frequently referred to as a server. That machine might be a dedicated server or it might be used for other purposes.

# MySQL Database:

#### MySQL is an RDBMS that manages and organizes data in a structured manner. It stores data in tables, enforces relationships between tables, and provides a SQL (Structured Query Language) interface for interacting with the data.

## WORKFLOW:

## Client Request:

#### The client initiates a request by sending a query or a command to the server. This request could be a SQL query for data retrieval, insertion, updating, or deletion.

## Server Processing:

 #### A server process is one that is typically waiting for work. When work arrives, BTS restarts the process, which retrieves any state data that it has previously saved. Typically, the client invokes the server with a named input event, and sends it some input data in a data-container.The server receives the client's request and processes it. For example, if the request is a SELECT query, the server fetches the requested data from the MySQL database. If it's an INSERT or UPDATE, the server modifies the data accordingly.

## Database Interaction:

 #### The MySQL database manages data storage, retrieval, and manipulation. It executes the SQL queries received from the server and returns the results. The database ensures data integrity, enforces relationships, and performs various optimizations for efficient data handling.

## Response to Client:

 #### The server sends the results of the query or the status of the operation back to the client. This could be the requested data, a success message, or an error message, depending on the nature of the client's request.




