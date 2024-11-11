# Gitdump

```
█▀▀ █ ▀█▀ █▀▄ █░█ █▀▄▀█ █▀█  version
█▄█ █ ░█░ █▄▀ █▄█ █░▀░█ █▀▀  2.0.0 
```

## Usage

```
usage: python3 gitdump.py [-h] [-u USERNAME] [-l LOCATION]

Dump all repos of a github account at once.

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        username of the github account
  -l LOCATION, --location LOCATION
                        location to save dumped repos
```

## Notes
- Dump all repositories of a github account (__backup solution__)
- Requires [git](https://git-scm.com/downloads) & [python3](https://www.python.org/downloads/) preinstalled
- Install __rich__ python library `pip install rich`  ([pypi](https://pypi.org/project/rich/))
