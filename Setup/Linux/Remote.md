### Setup Remote Server
Install openssh-server
```sh
$ sudo apt-get install openssh-server sshfs
```

### Setup Samba Share
Install samba
```sh
$ sudo apt-get install samba samba-common python-glade2 system-config-samba
```
Add samba user (using current user password)
```sh
$ sudo smbpasswd -a $USER
```
In `/etc/samba/smb.conf` add this at the bottom
```
[<current_user>]
        path = /home/<current_user>
        writeable = yes
        valid users = <current_user>
```