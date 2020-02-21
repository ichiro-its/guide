### Setup Git
Install git
```sh
$ sudo apt-get install git
```
Setup global user name and email
```sh
$ git config --global user.name 'ichiro-'$USER
$ git config --global user.email "ichiro.its@gmail.com"
```
Generate public ssh key (enter empty passphrase)
```sh
$ ssh-keygen -t rsa
```
- Open [GitLab.com](https://gitlab.com/users/sign_in)
- Sign In as `ICHIRO-ITS-Admin`
- Open setting for [SSH Keys](https://gitlab.com/profile/keys)
- Add Key as in `~/.ssh/id_rsa.pub`
