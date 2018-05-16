# Git exercises

## A - First steps
Let's build a toy program and maipulate it with git.
* __1__ - Create a folder for your new project. In your favorite language (Python?), create a program that outputs `Hello world!`.
* __2__ - Initialize this project as a local git repository (hint `git init`)
* __3__ - Make a commit with (only) the file you wrote (no compiled files, `pyc` etc)
* __4__ - To avoid committing bad files, add the `.gitignore` corresponding to your language, and commit it.
* __5__ - Write a file `Readme.txt` file to describe your project (this is not a special git file). Modify your program to ask the user its name. See how you can have modifications in different files. Add both these modifications in a __single__ commit.
* __6__ - Contemplate your work (`git log`, `git diff`, etc)

## B - Branches
Now we're going to make our program do some mathematics. We're using branch to organize.
* __1__ - Write an iterative function to compute the factorial of a number, and commit it.

You now change that function to be an recursive one. You're struggling (yes you are, don't ask questions)! Your friend Mathieu comes in and ask you the factorial of 27, your program is not working. You now decide to organize with branches.

* __2__ - Change your factorial function to something that doesn't work. __Don't__ commit.
* __3__ - Create a new branch to work on that "state of the art" factorial function. Try to change to that branch and notice how it doesn't work. You should have something like
```
...
Please commit your changes or stash them before you switch branches.
Aborting
```
* __4__ - Stash your changes, change branch, and apply your changes in the new branch.
* __5__ - After a long time, you finally figure out how to write a recursive factorial function. Commit that change in your new branch.
* __6__ - Merge that new branch in the `master` branch.
* __7__ - In the `master` branch, you're not happy with that new function (you decided you more of an iterative person). Make a revert commit (`git revert`) to undo the merging.

## C - Making friends
Find someone(s) who also finished the previous experiments. You're a team now and will start a new project.

* __1__ - On Github create a (public) repository (you can choose a different name, it will make things easier). Add a Readme, a .gitignore, and an MIT License (why not? unless you're very protective of your factorial functions).
* __2__ - Clone the repository on your local machine.

Your project is gonna be an ambitious math library. There's already a lot of interest for your work, so you decide not to work in the `master` branch that you keep for people to see.

* __3__ - One of you will create a branch to work on a Fibonacci function, while the other will create another branch to work on `min` and `max` functions. This time, use Github to create the branches. You work and commit in your respective branches. Hint: you're gonna need to use the synchronization commands, such as `git fetch`, `git pull`, `git push`, to work from your computer.
* __4__ - Doing things well, you decide to use `pull request` to add your work in the master branch (remember a `pull request` is just a merge of branches on a remote repository, with a fancy interface). You put some comments, and you discover that each of your code is not documented, so you decide __not to merge__ the `pull request` for now.
* __5__ - Now you will exchange branches and comment each other's code. Commit and push. The commits appear in the open `pull request`. You're happy with it and merge both `pull request`.

## D - Making enemies
* __1__ - On the previous project, you create a new branch to add some linear algebra to your library.
* __2__ - Add a function to compute the sum of two vectors.
* __3__ - Without talking to each other, you both take the initiative to write a dot product function, in that __same file__, and __after__ the sum function.
* __3__ - Commit and push. The last one to commit will have to do a conflict resolution.
