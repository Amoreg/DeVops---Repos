
# Git

## What is Git:

#### Definition: Git is a free and open-source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Git is easy to learn and has a tiny footprint with lightning-fast performance. Developed by Linus Torvalds in 2005, Git has become one of the most popular version control systems in use today. 

## Important Functions of Git:

### 1. Performance

 #### The raw performance characteristics of Git are very strong when compared to many alternatives. Committing new changes, branching, merging, and comparing past versions are all optimized for performance. The algorithms implemented inside Git take advantage of deep knowledge about common attributes of real source code file trees, how they are usually modified over time, and what the access patterns are. Unlike some version control software, Git is not fooled by the names of the files when determining what the storage and version history of the file tree should be, instead, Git focuses on the file content itself. After all, source code files are frequently renamed, split, and rearranged. The object format of Git's repository files uses a combination of delta encoding (storing content differences), and compression and explicitly stores directory contents and version metadata objects.

### 2. Security

#### Git has been designed with the integrity of managed source code as a top priority. The content of the files as well as the true relationships between files and directories, versions, tags, and commits, all of these objects in the Git repository are secured with a cryptographically secure hashing algorithm called SHA1. This protects the code and the change history against both accidental and malicious changes and ensures that the history is fully traceable. With Git, you can be sure you have an authentic content history of your source code. Some other version control systems have no protections against secret alteration at a later date. This can be a serious information security vulnerability for any organization that relies on software development.











