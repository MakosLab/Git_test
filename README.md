# GitHub useful tricks 

#### Save GitHub Password with SSH key 

SSH keys are generally more secure than passwords/tokens and save you from re-entering credentials:

Generate an SSH Key (if you don’t already have one):

    ssh-keygen -t ed25519 -C "your_email@example.com"

Press Enter to accept default file location (e.g. ~/.ssh/id_ed25519).
Enter a passphrase for added security (optional but recommended).
Add Public Key to GitHub:

        cat ~/.ssh/id_ed25519.pub
        
Go to GitHub SSH settings and paste the copied public key.

Test Your Connection:

      ssh -T git@github.com
      
If successful, you’ll see a “Hi username! You've successfully authenticated…” message.

#### Use SSH URLs when cloning/pulling/pushing:

            git clone git@github.com:username/repo-name.git

This method means no more password or token prompts, although you may need to unlock your SSH key once per session (if you used a passphrase).
