#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Remove all content from a CMIS folder.
#
# Requirements:
# sudo apt-get install python python-setuptools
# sudo easy_install cmislib
#
# Usage example:
# ./clear-cmis-folder.sh http://localhost:8080/alfresco/api/-default-/public/cmis/versions/1.1/atom admin admin

from cmislib import CmisClient
import os, sys

# Defaults
path = '/the/folder'
url = 'http://localhost:8080/alfresco/api/-default-/public/cmis/versions/1.1/atom'
user = 'admin'
password = 'admin'

# Get arguments from command line
try:
  path = sys.argv[1]
  url = sys.argv[2]
  user = sys.argv[3]
  password = sys.argv[4]
except:
  print 'Using default connection parameters'

# Connect
try:
  client = CmisClient('http://localhost:8080/alfresco/api/-default-/public/cmis/versions/1.1/atom', 'admin', 'admin')
  repo = client.defaultRepository
except:
  print 'Failed to connect to server'
  quit()

# Delete children
folder = repo.getObjectByPath(path)
for child in folder.getChildren().getResults():
  print 'Deleting ' + child.properties['cmis:name'] + '    (' + str(child) + ')'
  if(type(child is Folder)):
    child.deleteTree()
  else:
    child.delete()
print 'Done.'
