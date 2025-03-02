# Course link : https://www.coursera.org/learn/introduction-git-github/home/module/1
# By : Google
# Name : Git & Git-Hub


# NOTE : VERSION CONTROL SYSTEM 
# - KEEP'S HISTORICAL COPY OF CODE {They help us see what the project was looking before}
# - Every small code-change is taken copy and tracked 
# - Basically, Keeps track of changes made to our files.

# NOTE IF YOU HAVE A SAME COPY OF TWO CODE HOW DO YOU CHECK THE DIFFERENCE ?

# NOTE diff - compares two different files and show the difference 
#       -> diff file_name.py file_name.py

# NOTE : diff -u file1 file2
#       -> shows the changes 
 

# NOTE cat - shows the file content (using CLI)


# NOTE : NEVER COMMIT DIRECTLY ON-TO THE MAIN BRANCH

# 1. Initalizing the folder 

#       -> git init

# 2. Adding a connection (LINK - from git) 

#       -> git remote add origin (LINK)

# 3. Checking for a connection

#       -> git remote -v

# 4. Removing a connection

#       -> git remote rm origin

# 5. Adding / Saving a file

#       -> git add .
# (or)      -> git add filename.extension

# 6. Creating a new branch 

#       -> git branch branch_name

# 6.1 If its on master branch and you want to move to main branch 

#       -> git branch -M main 

# 6.2 and then push 

#       -> git push -u origin main

# 7. Switching to another Branch 

#       -> git checkout branch_name

# 8. To check all the logs

#       -> git log

# 9. Push to a branch 

#       -> git push origin (branch_name)
# (or force push)       -> git push origin main -f

# 10. Pull from a branch 

# 1. create a folder in git 
# 2. create a folder in pc(this folder wont be updated to git)
# 3. copy the link from the github

# OR

#       -> git pull (LINK)
# (or)      -> git pull origin (repo_link)

# 11. How to remove commit
# NOTE : All the prev-commit will be removed and not the whole 
 
# IMPT : copy the commit_address

#       -> git reset commit_address (they are staged basically)

# 12. To delete a file inside a folder

#       -> git rm file_name
# (or)      -> git rm -rf file_name

# 13. Rough note concept
#       -> git stash 
# Hides the file ( File must not be commited ) & brings back when you need it ( SAME AS A ROUGH BOOK )

# 14. To bring back the hidden file 

#       -> git stash pop

# 15. To delete the hidden file 

#       -> git stash clear -- deletes the hidden file 

# 16. https://learngitbranching.js.org/?NODEMO # WORKING OF BRANCH IN GIT (VISUALIZATION)

# 17. To merge file changes to main branch

#       -> git merge main

# 18. Fork -- basically having a copy of the project in your account {the forked url is called upstream url}

# (clone)       -> git clone LINK_ADDRESS