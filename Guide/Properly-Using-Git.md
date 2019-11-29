### Clone from Repository
Either use HTTPS clone (copy/download) project from repository
```sh
$ git clone https://gitlab.com/ICHIRO-ITS/readme
```
Alternatively you could use SSH, so username and password won't be required everytime you push
```sh
$ git clone git@gitlab.com:ICHIRO-ITS/readme.git
```

### Check for Update
Always update your project from origin (default online repository name). if you have unfinished work, and don't want to update yet, you may skip this part.
Make sure you are on master branch (default branch)
```sh
$ git pull origin master
```
Alternatively you may pull from other branch
```sh
$ git pull origin <other_branch>
```

### Make Changes
You could diretly make changes on master branch, or alternatively to avoid conflict, you could switch to temp branch before make any changes.
Use branch name that reasemble changes you gonna make, ex: use branch "walking" if you want to modify walking mechanic of the robot, or branch "object_detection" if you want to modify object detection system of the robot
```sh
$ git checkout -b <temp_branch_name>
```

### Add Changes
After make changes, check again changes you have done using
```sh
$ git status
```
Read the output, if there's is red mark, add changes using
```sh
$ git add <file_name>
```
Alternatively you could add all changes using (make sure you are on root of this project)
```sh
$ git add -A
```

### Commit Changes
After all files marked green in `$ git status`, save all changes as commit using
```sh
$ git commit -a
```
Alternatively you may directly write message using
```sh
$ git commit -a -m "<commit_message>"
```
Use proper commit message that show changes you have done, ex: "Add LBP for ball detection", "Fix initial position", etc.

### Push Changes
After several commit, and you have finished your work, always push (upload) your changes to origin using
Make sure you are on master branch (default branch)
```sh
$ git push origin master
```
If you are modifying from temp branch, switch it to master, update master, then merge change from your temp branch to master
```sh
$ git checkout master
$ git pull origin master
$ git merge <temp_branch>
$ git push origin master
```
And don't forget to delete your temp branch if you won't using it again
if you using temp branch, don't forget to switch to master branch, and merge your temp branch before push it to origin
```sh
$ git branch -D <temp_branch>
```

### Merge Conflict
If there's unresolved merge conflict (shown in `$ git status`), you should resolve it as follow
- Navigate to corresponding file and edit it using your favorite text editor (ex: vscode)
- Either you accept incoming changes or keep your local changes ("as shown with <<< and >>>")
- check again using `$ git status`, save changes if there's no unresolved merge conflict, or repeat if there's.

### Reset Project
If you have done wrong things and the only solution is reset project, you may use following command
- `$ git reset HEAD --hard`, to reset changes to the latest commit
- `$ git reset <commit_code> --hard`, to reset to specific commit (use `$ git log` to view all commit and its code)
- `$ git clean -fd`, to clean unnecessary files and folders
