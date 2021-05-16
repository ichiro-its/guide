# Setup Git

## Installation

- Install **Git** using `apt` command.
  ```sh
  ~$ sudo apt install git
  ```

## Configure Global User

- Configure global user name and email
  ```sh
  ~$ git config --global user.name 'ICHIRO ITS'
  ~$ git config --global user.email "ichiro.its@gmail.com"
  ```

## Configure SSh Key

- Generate public SSh key with empty passphrase _(just press `Enter` when prompted to type a passphrase)_
  ```sh
  ~$ ssh-keygen -t rsa
  ```
- Open [GitLab.com](https://gitlab.com/users/sign_in)
- Sign In as `ICHIRO-ITS-Admin`
- Open setting for [SSH Keys](https://gitlab.com/profile/keys)
- Add Key as in `~/.ssh/id_rsa.pub`
  ```sh
  ~$ cat ~/.ssh/id_rsa.pub
  ```
