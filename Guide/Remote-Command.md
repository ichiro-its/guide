### Robot IP
Add this env variables to your `~/.bashrc`
```sh
export ITHAARO_NAME='ithaaro'
export ITHAARO_IP='192.168.123.1'

export ARATA_NAME='arata'
export ARATA_IP='192.168.123.2'

export UMARU_NAME='umaru'
export UMARU_IP='192.168.123.3'

export TOMO_NAME='tomo'
export TOMO_IP='192.168.123.4'

// For Default Robot
export ROBOT_NAME=$ARATA_NAME
export ROBOT_IP=$ARATA_IP
```
Set default robot to use with (ex: UMARU)
```sh
$ export ROBOT_NAME=$UMARU_NAME
$ export ROBOT_IP=$UMARU_IP
```
For wifi connection, set IP manually with
```sh
$ export ROBOT_IP=<wifi_ip>
```
### Remote Robot
Add this aliases to your `~/.bash_aliases`
```sh
alias robotremote='ssh -X '$ROBOT_NAME'@'$ROBOT_IP
alias ithaaroremote='ssh -X '$ITHAARO_NAME'@'$ITHAARO_IP
alias arataremote='ssh -X '$ARATA_NAME'@'$ARATA_IP
alias umaruremote='ssh -X '$UMARU_NAME'@'$UMARU_IP
alias tomoremote='ssh -X '$TOMO_NAME'@'$TOMO_IP
```
To remote without login, use ssh-keygen (enter empty passphrase)
```sh
$ ssh-keygen -t rsa
$ ssh-copy-id -i ~/.ssh/id_rsa $ROBOT_NAME'@'$ROBOT_IP
```

### Mount Robot
Add this env variables to your `~/.bashrc`
```sh
export ROBOT_MOUNT_DIR='/home/'$USER'/Share/'
```
Add this aliases to your `~/.bash_aliases`
```sh
alias robotmount='mkdir -p '$ROBOT_MOUNT_DIR''$ROBOT_NAME' & sshfs '$ROBOT_NAME'@'$ROBOT_IP':/home/'$ROBOT_NAME' '$ROBOT_MOUNT_DIR''$ROBOT_NAME
alias robotumount='umount -l '$ROBOT_MOUNT_DIR''$ROBOT_NAME
alias robotcd='cd '$ROBOT_MOUNT_DIR''$ROBOT_NAME
```
- Use `$ robotmount` to mount robot directory
- Use `$ robotumount` to unmount robot directory
- Use `$ robotcd` to change directory to robot directory

### Program Command
Add this aliases to your ~/.bash_aliases
```sh
alias run='./run'
alias runnull='./run >/dev/null 2>&1'
alias runlog='mkdir -p log & ./run > ./log/$(date +%Y-%m-%d_%H:%M).log'
alias runkill='sudo killall run'
```
- Use `$ run` to run program using root
- Use `$ runnull` to run program without logging to terminal
- Use `$ runlog` to run program with logging to `./log/<date>.log`
- Use `$ runkill` to kill run program

### Screen Command
Add this aliases to your ~/.bash_aliases
```sh
alias screenstart='screen -S run'
alias screenresume='screen -d -R run'
```
- Use `$ screenstart` to start screen
- Use `$ screenresume` to resume screen
- Use `ctrl + a` `ctrl + d` to detach screen
- Use `$ exit` within screen to terminate screen

### Git Command
- Use `$ git clone <repository_url>` to clone repository to local
- Use `$ git add <file>` to track a file
- Use `$ git add -A` to track all available files
- Use `$ git commit <file>` to commit a file
- Use `$ git commit -a` to commit all available files
- Use `$ git commit -a -m <description>` to commit all available files with specific description
- Use `$ git status` to view git status
- Use `$ git log` to view git commit log
- Use `$ git branch` to view git branches
- Use `$ git checkout <branch>` to switch branch
- Use `$ git checkout -b <new_branch>` to switch to new branch
- Use `$ git branch -D <branch>` to delete a branch
