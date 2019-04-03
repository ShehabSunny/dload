## Dload

This is a cli tool to download files using different protocols.  

### Quick start:
Default download location: `$HOME/data`  

**Download with urls**
```
$ dload -u http://example.com/file 
```
or  

**Download with urls in a file**
```
$ dload -f urls.txt 
```

### Supported protocols (Tested with)
* http
* https
* ftp
* ftps
* sftp
* ssh
* scp

### Dependencies
* Python version: >=3.6.7
* Python package `setuptools` if not already installed.

### Build
**Build the tool using `python setup.py install`**

### Test
**Test with pytest using `pytest dlaod`**

### Using the tool
`dload -h` will show the help information

It takes two mutually exclusive arguments using `-u` or `--urls` and `-f` or `--file`.

## URL arguments `-u` or `--urls`
You can pass the urls directly using the `-u` argument.  
For example:
```
$ dload -u http://www.africau.edu/images/default/sample.pdf
```

multiple urls spparated by space:
```
$ dload -u http://www.africau.edu/images/default/sample.pdf sftp://demo:password@test.rebex.net:22/readme.txt
```

## URLs file argument `-f` or `--file` 
You can pass a file path that has all the URLs separated by newline.
For example:
```
$ dload -f urls.txt
```

## Download path argument `-l` or `--location`
**Default download location is `$HOME/data`**  

You can provide the download location using `-l` or `--location` argument.  
**Note: make sure the directory exists and has write permission**

For example:
```
$ dload -f urls.txt -l ./data
```
