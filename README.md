# Clear CMIS folder

Remove all content from a CMIS folder. From command-line. Useful when testing a CMIS client.

# Requirements
```
sudo apt-get install python python-setuptools
sudo easy_install cmislib
```

# Usage example
```
./clear-cmis-folder.sh /the/folder http://localhost:8080/alfresco/api/-default-/public/cmis/versions/1.1/atom admin admin
```
