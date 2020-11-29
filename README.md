# ignorefile

Download .gitignore file for a language of your choice.

# Description

**ignorefile** is a command line tool that downloads ```.gitignore``` file of a language/Framework using a third party API by [Toptotal](https://www.toptal.com/developers/gitignore).

## Install

```
pip install ignorefile
 ```


## Usage

`ignorefile <language>`: Download .gitignore for \<language> and adds it the current working directory.
eg:
```
ignorefile python
```
if a .gitignore file already exists, the user will have the choice:

```
$ ignorefile django
.gitignore already exists, [A]ppend, [O]verride, [Q]uit?
```
If you choose append option, all duplicates in the .gitignore file will be removed.
eg:
```
### C ###
*.obj
*.out
### C++ ##
*.obj
*.out

```

### Options

```
Options:
  --list     list all available languages/Frameworks.
  --version  Show the version and exit.
  --help     Show this message and exit.
```

### License
MIT