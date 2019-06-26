# Reverse Shell

A reverse shell is a program that gives a remote user access to the shell on a target computer.  For instance if you the attacker want
to navigate a computer and launch commands what is the best way to do that?  Through the shell and using commands like ```ls``` and ```cd```.

So to gain access on the target computer with a reverse shell we start up a server on our host machine.  Then we send the clientside script
to the target computer and execute it.  It then establishes a connection with our server and from our server we navigate through the target
computer.

The scripts in this repo give feedback on where the attacker is on the host computer and allows them to use the ```cd``` command.

### Usage

1. Start the server with ```python reverse_shell_server.py```
2. When the ```reverse_shell_client.py``` script is on the target computer just run ```python reverse_shell_client.py```
3. Check the server script output and viola start using the remote shell.

## What it looks like
![reverse](https://github.com/B2Gdevs/reverse_shell/blob/master/reverse_shell.PNG)
