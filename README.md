# GitHub step-by-step

## Save GitHub Password with SSH key 

SSH keys are generally more secure than passwords/tokens and save you from re-entering credentials:

Generate an SSH Key (if you don’t already have one):

    ssh-keygen -t ed25519 -C "yourname@ua.edu"

Press Enter to accept default file location (e.g. ~/.ssh/id_ed25519).
Press Enter/Return 3x so in the future you don't have to type any passwords
Add Public Key to GitHub:

        cat ~/.ssh/id_ed25519.pub
        
Go to GitHub SSH settings and paste the copied public key.

Test Your Connection:

      ssh -T git@github.com
      
If successful, you’ll see a “Hi username! You've successfully authenticated…” message.

## Git Init

            git init
            
'git init' turns any directory into a Git repository.

## Use SSH URLs when cloning/pulling/pushing:

            git clone git@github.com:username/repo-name.git

This method means no more password or token prompts, although you may need to unlock your SSH key once per session (if you used a passphrase).


## get a file into your GitHub repository from the command line:

1. If you don’t have a local copy of your repository yet, first clone it from GitHub:

        ## clone SSH 
        git clone https://github.com/username/repository-name.git
        cd repository-name

2. Add the file to Git’s staging area
   
       git add your-file-name

3. Commit your changes

       git commit -m "write your comment"

4. Push changes

       git push origin main

If your default branch is named something else replace main with that branch name.

## pull any changes from the remote repository

    git pull

this will fetch the latest commits and merge them into your local branch.



