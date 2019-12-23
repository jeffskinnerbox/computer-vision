<!--
Maintainer:   jeffskinnerbox@yahoo.com / www.jeffskinnerbox.me
Version:      0.0.1
-->


[Git][02] is a distributed version control system,
meaning the entire history of the repository is transferred to the client during the cloning process.
For projects containing large files,
particularly large files that are modified regularly,
this initial clone can take a huge amount of time,
as every version of every file has to be downloaded by the client.

[Git LFS][01] (Large File Storage) is a Git extension that reduces
the impact of large files in your repository by downloading
the relevant versions of them _lazily_.
This means large files are downloaded during the [checkout][03]
process rather than during [cloning][04] or [fetching][05].

>**NOTE:**GitHub will warn you when pushing files larger than 50 MB.
>You will not be allowed to push files larger than 100 MB.
>See more information [here][08].

# Intalling Git LFS
There are [multiple ways to install Git LFS][06],
but I using your the `apt`package manager.

```bash
# install git-lfs
sudo apt-get install git-lfs
```

# Initializing Git LFS
To create a new Git LFS aware repository,
you'll need to run `git lfs install` after you create the repository
and then navigate to your Git repository
(where the `.git` directory is located)
and activate Git LFS as below:

```bash
# initialize the git repository
cd ~/src/computer-vision
git init

# initialize large file store (lfs)
git lfs install
```

This installs a special pre-push [Git hook][07] in your repository
that will transfer Git LFS files to the server when you git push.

Now take a look at the directory `~/src/computer-vision/.git/hooks`.
You'll find Git hooks have been added/updated and contain Git LFS commands.
Also a directory `~/src/computer-vision/.git/lfs` is added which is the local cache.

# Configurating Git LFS
Now that we have installed Git LFS for our repository,
it is time to configure which file types we want to associate with Git LFS.
This information will be added to a `.gitattributes` file in your repository
(this should be commit and push to your remote repository).
The easiest way to associate a file type with Git LFS is by means of the `git lfs track`
command as shown below:

```bash
# associate all video & image files to Git LFS
git lfs track "*.mp4" "*.avi" "*.webm" "*.mkv" "*.ogv"
git lfs track "*.bmp" "*.gif" "*.jpg" "*.png" "*.tif" "*.svg"

# associate data sets to Git LFS
git lfs track "*.dat" "*.csv"

# associate binary files to Git LFS
git lfs track  "*.caffemodel"
```

This information is stored in the `~/src/computer-vision/.gitattributes`  file
and if you `cat` this file you'll see the following:

```
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.avi filter=lfs diff=lfs merge=lfs -text
*.webm filter=lfs diff=lfs merge=lfs -text
*.mkv filter=lfs diff=lfs merge=lfs -text
*.jpg filter=lfs diff=lfs merge=lfs -text
*.png filter=lfs diff=lfs merge=lfs -text
*.tif filter=lfs diff=lfs merge=lfs -text
*.svg filter=lfs diff=lfs merge=lfs -text
*.bmp filter=lfs diff=lfs merge=lfs -text
*.gif filter=lfs diff=lfs merge=lfs -text
*.dat filter=lfs diff=lfs merge=lfs -text
*.csv filter=lfs diff=lfs merge=lfs -text
*.caffemodel filter=lfs diff=lfs merge=lfs -text
```

>**NOTE:** I you list any of the above file types in your `.gitignore` file,
>they will not be managed bu Git LFS.

# Initiate Your Repository
And once you do the initial `git add` those files
are effected by Git LFS tracking rules can be listed:

```bash
# do your initial add
git add --all

# list files being tracked via git lfs
git lfs ls-files

# do your commit to the repository
git commit -m"initial commit to repository"
```

# Git LFS with an Existing Repository
The above text shows how to enable Git LFS when starting a new repository
and we know which files we want to associate with Git LFS.
But what if you want to enable Git LFS to your existing repository?
You can do so the same way as we have done for a new repository.
From that moment on, new files or updates to files will be tracked by Git LFS.
But the commits before you have enabled Git LFS, will not be automatically migrated.

There is a way however to migrate your entire repository.
You have to migrate all your existing branches following the example command below:

```bash
git lfs migrate import --include="*.mp4,*.avi,*.webm,*.mkv" --include-ref=refs/heads/master
```

The above example shows the command which should be used if you had
forgotten to associate `.mp4`, `.avi`, `.webm`, `.mkv`
file types to our previous created repository.

# Sources
* [Git LFS](https://www.atlassian.com/git/tutorials/git-lfs)
* [Why and How to Use Git LFS](https://dzone.com/articles/git-lfs-why-and-how-to-use)



[01]:https://git-lfs.github.com/
[02]:https://git-scm.com/
[03]:https://www.atlassian.com/git/tutorials/using-branches/git-checkout
[04]:https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone
[05]:https://www.atlassian.com/git/tutorials/syncing/git-fetch
[06]:https://www.atlassian.com/git/tutorials/git-lfs#installing-git-lfs
[07]:https://www.atlassian.com/git/tutorials/git-hooks
[08]:https://help.github.com/en/github/managing-large-files/working-with-large-files
[09]:
[10]:
