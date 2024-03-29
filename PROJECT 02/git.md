
# Git

## What is Git:

#### Definition: Git is a free and open-source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Git is easy to learn and has a tiny footprint with lightning-fast performance. Developed by Linus Torvalds in 2005, Git has become one of the most popular version control systems in use today. 

# Importants Functions of Git:

### 1. * Performance

 #### The raw performance characteristics of Git are very strong when compared to many alternatives. Committing new changes, branching, merging, and comparing past versions are all optimized for performance. The algorithms implemented inside Git take advantage of deep knowledge about common attributes of real source code file trees, how they are usually modified over time, and what the access patterns are. Unlike some version control software, Git is not fooled by the names of the files when determining what the storage and version history of the file tree should be, instead, Git focuses on the file content itself. After all, source code files are frequently renamed, split, and rearranged. The object format of Git's repository files uses a combination of delta encoding (storing content differences), and compression and explicitly stores directory contents and version metadata objects.

### 2. Security

#### Git has been designed with the integrity of managed source code as a top priority. The content of the files as well as the true relationships between files and directories, versions, tags, and commits, all of these objects in the Git repository are secured with a cryptographically secure hashing algorithm called SHA1. This protects the code and the change history against both accidental and malicious changes and ensures that the history is fully traceable. With Git, you can be sure you have an authentic content history of your source code. Some other version control systems have no protections against secret alteration at a later date. This can be a serious information security vulnerability for any organization that relies on software development.

### 3. Flexibility

#### One of Git's key design objectives is flexibility. Git is flexible in several respects: in support of various kinds of nonlinear development workflows, in its efficiency in both small and large projects, and its compatibility with many existing systems and protocols. Git has been designed to support branching and tagging as first-class citizens (unlike SVN) and operations that affect branches and tags (such as merging or reverting) are also stored as part of the change history. Not all version control systems feature this level of tracking.

### 4. Version control with Git

#### Git is the best choice for most software teams today. While every team is different and should do their own analysis, here are the main reasons why version control with Git is preferred over alternatives:

### 5. Git is good

Git has the functionality, performance, security, and flexibility that most teams and individual developers need. These attributes of Git are detailed above. In side-by-side comparisons with most other alternatives, many teams find that Git is very favorable.

### 6. Git is a de facto standard

Git is the most broadly adopted tool of its kind. This makes Git attractive for the following reasons. At Atlassian, nearly all of our project source code is managed in Git. Vast numbers of developers already have Git experience and a significant proportion of college graduates may have experience with only Git. While some organizations may need to climb the learning curve when migrating to Git from another version control system, many of their existing and future developers do not need to be trained on Git. Vast numbers of developers already have Git experience and a significant proportion of college graduates may have experience with only Git. While some organizations may need to climb the learning curve when migrating to Git from another version control system, many of their existing and future developers do not need to be trained on Git. In addition to the benefits of a large talent pool, the predominance of Git also means that many third-party software tools and services are already integrated with Git including IDEs, and our tools like DVCS desktop client Sourcetree, issue and project tracking software, Jira, and code hosting service, 

### 7. Git is a quality open-source project

#### Git is a very well-supported open-source project with over a decade of solid stewardship. The project maintainers have shown balanced judgment and a mature approach to meeting the long-term needs of its users with regular releases that improve usability and functionality. The quality of the open source software is easily scrutinized and countless businesses rely heavily on that quality. Git enjoys great community support and a vast user base. Documentation is excellent and plentiful, including books, tutorials, and dedicated websites. There are also podcasts and video tutorials. Being open source lowers the cost for hobbyist developers as they can use Git without paying a fee. For use in open-source projects, Git is undoubtedly the successor to the previous generations of successful open-source version control systems, SVN, and CVS.

### 8. Collaborative Development:

#### Branching and Merging: Git's robust branching and merging capabilities allow multiple developers to work simultaneously on different features or bug fixes without interfering with each other's work. Changes can be later integrated into the main codebase.
#### Pull Requests: Git hosting platforms, like GitHub and GitLab, leverage pull requests as a way for developers to propose and review changes before merging them into the main branch. This facilitates collaboration and code review.

### 9.Web Development:

#### Frontend and Backend Code: Web development projects, both on the frontend and backend, benefit from Git's version control capabilities. It allows for the management of HTML, CSS, JavaScript, server-side code, and other web development assets.Responsive Design: For responsive web design, Git helps manage different branches for various device resolutions, ensuring a consistent and responsive user experience.

## 10 Collaboration in Mobile Teams:

#### Teams working on mobile apps can use Git to collaborate efficiently, with each developer working on separate features or platforms.

## 11. DevOps and Continuous Integration/Continuous Deployment (CI/CD):

 #### Git integrates seamlessly with CI/CD tools to automate the building, testing, and deployment of software. Changes pushed to a Git repository trigger automated pipelines, ensuring rapid and reliable software delivery.

## 12. Infrastructure as Code (IaC): 
### Git is used to version control infrastructure code, allowing teams to manage and version infrastructure configurations. Tools like Terraform and Ansible are commonly integrated with Git.

## 13. Data Science and Machine Learning:

#### Versioning Data and Notebooks: Data scientists use Git to version control datasets, Jupyter notebooks, and machine learning models. It helps track changes, collaborate with team members, and reproduce experiments. Experiment Tracking: Git enables the tracking of different experimental versions, making it easier to compare results, share findings, and reproduce experiments.

## 14. Technical Documentation:

#### Git is used to version control technical documentation. Teams can collaborate on documentation, track changes, and maintain a history of documentation edits.Git hosting platforms often include wikis that use Git repositories. This allows teams to collaboratively create and maintain knowledge bases.

## 15.  Open Source Contributions:

#### Contributing to Projects: Open source projects often use Git to manage contributions from various contributors. Developers can fork repositories, make changes, and create pull requests to propose changes to the original project.


# Requirements in learning Git#

#### A Desktop or Laptop with good configuration

#### Knowledge of Linux and its command

#### Download and install  an IDE or text editor e.g. Vs code, Vim, or nano.

#### Download Git software and install on your operating system

Create a GitHub account here: [GitHub Pages](https://pages.github.com/).

# GIT INSTALLATION

## Installation on Windows

### Git Installation on Windows 10

#### 1. Download and install Git.

#### 2. Git bash interface.

#### 3. Basic Git commands.

#### 4 Create a local repository.

#### 5. Connect to the remote repository.

#### 6. Push the file to GitHub.


## Installation on  macOS?

### The easiest way to install Git on a Mac is via the stand-alone installer:

#### 1. Download the latest Git for Mac installer.

#### 2. Follow the prompts to install Git.

#### 3. Open a terminal and verify the installation was successful by typing git --version :

## Installing  Git on Linux Ubuntu

#### 1.Debian / Ubuntu (apt-get)

#### 2. From your shell, install Git using apt-get: $ sudo apt-get update $ sudo apt-get install git.

#### 3. Verify the installation was successful by typing git --version : 

#### 4. Configure your Git username and email using the following commands, replacing Emma's name with your own.

### Debian/Ubuntu: Open a terminal. Run the following commands:

#### sudo apt update

![pictures](<images/update command.png>)

#### sudo apt install git

![Git install](<images/git install command2.png>)

# Git commands

#### Git init: Initialize a new Git repository.

#### Git clone: Create a copy of a remote repository on your local machine.

#### Git add: Stage changes for the next commit.

#### Git commit: Record changes to the repository.

#### Git push: Push local changes to a remote repository.

#### Git pull: Fetch changes from a remote repository and merges them into the local branch.

#### Git branch: Create, list, or delete branches.

#### Git merge: Merge changes from one branch into another.

# Git concepts

## Typical Workflow is as follows

#### Get a local copy of the code.

#### Create a branch.

#### Edit files.

#### Add and commit changes to a local machine.

#### Get back in sync with changes committed by others.

#### Push branch to the remote git repository.

#### Merge local branch into local master.

#### Push local master to remote git repository.

![Git workflow](<images/add-commit- push command.png>)

# New Branches

### What's a Branch,

#### A branch, at its most basic, is a copy of a Git project that you can change as you like and then combine with the original project.

#### When you create a new repository in GitHub, there's one branch by default---the "main" branch (previously called "master"). This, as the name implies, is the main container where your production code is stored. That is to say (in most cases, at least), if you push a change directly to the main branch, you're making a change directly to the working product.
The problem? If you push directly to the main, you run the risk of pushing buggy code to the production environment, potentially causing serious issues. That's why you need to create a separate branch to do your work in (and then later submit that branch for review before it's merged into the main branch).

####  Configure a new branch

#### Once you're in the proper directory, you can then create a new branch. Run this command:

#### git checkout -b <your-new-branch-name> Replace <your-new-branch-name> with the actual name that you want to give your branch.

![New branch;Lagos](<images/New branch.png>)

## List branches

#### git branch

![New branch;Lagos](<images/New branch.png>)

### Use the git switch - (Or git checkout - ) to switch to the previous branch you were working with. This is pretty similar to the cd - command, which is used to switch to the previous directory

 #### use < git checkout (branch name)>

![New branch;Lagos](<images/git checkout.png>) 

 # Marging a Branch into another Branch

 #### To merge branches locally, use git checkout to switch to the branch you want to merge into. This branch is typically the main branch. Next, use git merge and specify the name of the other branch to bring into this branch.

![Merging branches](<images/git merge.png>)

# Deleting a branch

## Here are commands to delete the branch locally:

#### 1. git branch -d "branch name"

#### 2. git branch --delete <branch>

#### 3. git branch -D <branchName>

#### 4. git push origin -d "branch name"

#### 5. git push <remote_name> --delete <branch_name>

#### 6. git push <remote_name> :<branch_name>

#### 7. git branch -d <BranchName>

#### 8. git branch -D <branchName>

![Deleting branches](<images/deleting branch.png>)


# Working with Remote Repositories for Collaboration

### Collaboration in Git often involves the use of remote repositories.

A remote repository is a version of your project hosted on a server or an online platform, allowing multiple developers to work together on the same codebase. Git hosting services like GitHub, GitLab, and Bitbucket are popular platforms for managing remote repositories.


















