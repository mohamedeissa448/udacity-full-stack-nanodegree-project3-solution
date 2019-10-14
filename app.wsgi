#!/usr/bin/python
# Add path to application directory
import sys
sys.path.insert(0, "/var/www/catalog/")

# Import Flask instance from main application file
from catalog import application
