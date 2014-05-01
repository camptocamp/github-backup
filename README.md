github-backup
=============

A simple script to backup the most important informations (repositories, wikis, pull requests+comments, issues+comments, teams and members) of your GitHub organization in a readable and usable format.

Structure of backed up files
----------------------------

    .
    ├── members
    │   ├── members-2014-04-29.tar.bz2
    │   │   ├── member1.json
    │   │   └── member2.json
    │   └── members-2014-04-30.tar.bz2
    │       ├── member1.json
    │       ├── member2.json
    │       └── member3.json
    ├── private-repos
    │   └── ...
    ├── public-repos
    │   └── repo1-id-2014-04-30.tar.bz2
    │       ├── repo1
    │       ├── repo1-collaborators.json
    │       ├── repo1-issues-comments.json
    │       ├── repo1-issues.json
    │       ├── repo1.json
    │       ├── repo1-pulls-comments.json
    │       ├── repo1-pulls.json
    │       └── repo1.wiki
    └── teams
        ├── teams-2014-04-29.tar.bz2
        │   ├── team1.json
        │   └── team2.json
        └── teams-2014-04-30.tar.bz2
            ├── team1.json
            ├── team2.json
            └── team3.json

Directories `public-repos/repo1-id-2014-04-30.tar.bz2/repo1` and `public-repos/repo1-id-2014-04-30.tar.bz2/repo1.wiki` are simply the sourse of Git repositories (see clone --mirror for more information)

Usage
-----

Create a simple configuration file (e.g. github-backup.conf) with the following infos:

    [github-backup]

    username: XXX
    password: XXX
    organization: camptocamp
    destdir: /your/backup/folder

And run the script like this:

    $ ./github-backup.py -c github-backup.conf

