# The Shell Scripting 

## Introduction to shell scripting

# What is shell scripting?

#### Shell scripting is a text file with a list of commands that instruct an operating system to perform certain tasks. A shell is an interface that interprets, processes, and executes these commands from the shell script. It can be particularly helpful to automate repetitive tasks, helping to save time and reduce human error.Shell scripting is a form of programming or scripting that involves writing a series of commands for a command-line interpreter, or shell, to execute. A shell is a user interface that allows users to interact with the operating system by entering commands. Shell scripts are essentially text files containing a sequence of such commands that can be executed together as a single program.

# A shell script comprises the following elements –

#### * Shell Keywords – if, else, break etc.
#### * Shell commands – cd, ls, echo, pwd, touch etc.
#### * Functions
#### * Control flow – if..then..else, case and shell loops etc.

# Why do we need shell scripts?

## There are many reasons to write shell scripts:

#### * To avoid repetitive work and automation

#### * System admins use shell scripting for routine backups.

#### * System monitoring

#### * Adding new functionality to the shell etc.

#### * Some Advantages of shell scripts

#### * The command and syntax are exactly the same as those directly entered in the command line, so programmers do not need to switch to entirely different syntax

#### * Writing shell scripts are much quicker

#### * Quick start......

#### * Interactive debugging etc.

#### * Some Disadvantages of shell scripts

#### * Prone to costly errors, a single mistake can change the command which might be harmful.

#### * Slow execution speed

#### * Design flaws within the language syntax or implementation

#### * Not well suited for large and complex task

#### * Provide minimal data structure unlike other scripting languages. etc.

# Key Aspects of Shell Scripting

#### Interactivity: Shells provide an interactive environment where users can enter commands and receive immediate feedback. Shell scripts allow users to automate sequences of these commands.

#### Scripting Language: Shell scripts are typically written in scripting languages specific to the shell environment. For example, Bash (Bourne Again SHell) is a popular scripting language for Unix-like operating systems, while PowerShell is commonly used in Windows environments.

#### Automation: The primary purpose of shell scripting is automation. Users can create scripts to perform repetitive tasks, execute multiple commands in sequence, or automate system administration tasks.

#### Control Structures: Shell scripts support control structures such as loops, conditionals, and functions, allowing for more complex and dynamic behavior. This enables scriptwriters to make decisions and repeat actions based on certain conditions.

#### Varbles and Environment: Shell scripts can use variables to store and manipulate data, making it possible to create dynamic and adaptable scripts. They also interact with the environment, using environment variables for configuration and communication with other processes.

#### File Handling: Shell scripts can manipulate files and directories, perform file operations, and handle input/output operations. This is crucial for tasks like data processing, file manipulation, and system configuration.

#### Terminal: A terminal is a program that establishes a connection with the server.

#### Shell: This program interprets shell scripting commands from the terminal and runs on the server. This is the command-line user interface you choose and includes shells such as the Bourne shell, Korn shell, Bourne-Again shell, and C shell.

#### Script: A script is a short program that performs a specific task.

#### Command-line shell: A command-line shell (also known as a command prompt) allows you to instruct your computer through textual commands. 

#### Shell script: A shell script is a script run through a command-line shell

#### Commonly Use Shell for Scripting

##### Commonly used shells for scripting include Bash, sh (Bourne Shell), csh (C Shell), ksh (Korn Shell), and PowerShell (for Windows). The choice of shell depends on the specific requirements of the task, as well as the operating system environment in use.

# 5 types of shells

![Types of Shell](<IMAGES/Tshell.png>)

# What is a shell in Linux?
 
#### * Shell in Linux is a text-based interface wherein users can enter command names, execute programs, and manipulate files such as file handles, file permissions, and directories. Users can access the shell through the terminal window or console, a window displaying a command prompt where users can enter commands

# Capabilities of Shell Script

####  * Shell scripts are incredibly versatile, capable of handling file manipulation, database monitoring, text printing, and more. While the language of shells has conditional operations, looping functions, and command-line arguments, much of the strength of shell programs comes from the ability to call any program through shell scripting. This allows you to design complex programs suited to your needs. 

# Target Audience

#### i. DevOps Engineers: DevOps professionals need to know shell scripting to create and manage automation scripts in CI/CD pipelines, container orchestration, and infrastructure as code (IaC) practices.

#### ii. System administrators need to learn shell scripting in order to make their jobs easier. Shell scripting helps them automate repetitive tasks, control servers, and guarantee that the system is secure and running smoothly.

#### iii. QA Engineers can use shell scripting to make testing easier and faster, which means they don't have to do as much testing by hand.

#### iv. IT support and operations teams utilize shell scripting to fix problems, keep an eye on systems, and do regular maintenance to make sure the systems work at their best.

# Getting Started With Shell Scripting

####  1.Variables: are used to store and manipulate data. They are assigned values using the '=' operator, and the value is accessed using $variable_name.

![Variables](<IMAGES/variable.png>)

![Variables](<IMAGES/variable output.png>)

![Variables](<IMAGES/variable input.png>)

#### 2. “#!” is an operator called shebang which directs the script to the interpreter location. So, if we use”#! /bin/sh” the script gets directed to the bourne-shell..

#  #!/bin/bash

#### 3. Comments: Lines beginning with the '#' character are comments and are ignored by the shell. Comments are used to add explanations and annotations to the script for human readers.

### This is a comment

#### 4. Command Execution:This allows you to capture the output of a command and store it in a variable. The $(command) syntax is used for command substitution.

#### result=$(command)

#### 5. Control Flow

####  a. Conditionals: Conditional statements allow you to execute different blocks of code based on specified conditions. Square brackets are used for testing conditions.

![Conditional statement](<IMAGES/Conditional st.png>)

![Conditional statement](<IMAGES/conditional st1 st.png>)

![Conditional statement](<IMAGES/cond output.png>)

#### b.  Loops: Loops allow you to repeat a block of code. for loops iterate over a list of items, while while loops continue executing as long as a specified condition is true.

![software update](<Images/update.png>)

### 6. Command Subsitution: This feature is useful when you want to capture the result of a command and use it as part of another command or in a variable assignment.

![software update](<Images/update.png>)

### 7.Input and Output: n Bash, input and output are handled through various mechanisms, including command-line arguments, standard input (stdin), standard output (stdout), and standard error (stderr)

![software update](<Images/update.png>)

### 8.Functions: Functions allow you to encapsulate a block of code that can be reused. Functions are defined using the function_name() { ... } syntax.

###  function_name() { # commands }

![software update](<Images/update.png>)
