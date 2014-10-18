"""
    IniParser - Manipulators INI files
    ==================================
    Utilities to facilitate INI file handling. This is accomplished with an object that inherit all of
    ConfigParser methods and give you new methods.

    Requires
    -----
    ConfigParser module

    Usage
    -----
    Import the IniParser.py file into your project and use the IniParser object.

    Authors & Contributors
    ----------------------
        * Massimo Guidi <maxg1972@gmail.com>,

    License
    -------
    This module is free software, released under the terms of the Python
    Software Foundation License version 2, which can be found here:

        http://www.python.org/psf/license/
"""

__author__ = "Massimo Guidi"
__author_email__ = "maxg1972@gmail.com"
__version__ = '1.0'

import ConfigParser

# -------------------------------------------------- #
# Class to handle INI files (ConfigParser extension) #
# -------------------------------------------------- #
class IniParser(ConfigParser.ConfigParser):

    def def_get(self,section,option,default=None):
        """
        Return section/option value; if section/option pairs not exist will be return default value

        @param section: INI file section
        @param option: INI file option (subsection)
        @param default: Return value if action/option pairs not exist (default None)
        @return: Return INI file section/option value or default value
        """
        if self.has_option(section,option):
            return self.get(section,option)
        else:
            return default
    
    def def_getbool(self,section,option,default=None):
        """
        Return section/option value,converting it into boolean; if section/option pairs not exist will be get
        default value

        @param section: INI file section
        @param option: INI file option (subsection)
        @param default: Return value if action/option pairs not exist (default None)
        @return: Return INI file section/option value or default value,converting it into boolean
        """
        if self.has_option(section,option):
            return self.getboolean(section,option)
        else:
            try:
                return bool(default)
            except (TypeError, ValueError):
                return None

    def def_getfloat(self,section,option,default=None):
        """
        Return section/option value,converting it into float; if section/option pairs not exist will be get
        default value

        @param section: INI file section
        @param option: INI file option (subsection)
        @param default: Return value if action/option pairs not exist (default None)
        @return: Return INI file section/option value or default value,converting it into float
        """
        if self.has_option(section,option):
            return self.getfloat(section,option)
        else:
            try:
                return float(default)
            except (TypeError, ValueError):
                return None

    def def_getint(self,section,option,default=None):
        """
        Return section/option value,converting it into integer; if section/option pairs not exist will be get
        default value

        @param section: INI file section
        @param option: INI file option (subsection)
        @param default: Return value if action/option pairs not exist (default None)
        @return: Return INI file section/option value or default value,converting it into integer
        """
        if self.has_option(section,option):
            return self.getint(section,option)
        else:
            try:
                return int(default)
            except (TypeError, ValueError):
                return None
            
    def put(self,section,option,value=None):
        """
        Set section/option value.
        If section not exist, will be created.

        @param section: INI file section
        @param option: INI file option (subsection)
        @param value: Value to set section/option pair
        """
        # Create section if it not exist,
        if not self.has_section(section):
            self.add_section(section)
        
        # Set section/option value
        self.set(section,option,value)
        
    def save(self,filename):
        """
        Save current information to file.

        @param filename: Output file name with path
        """
        with open(filename, 'wb') as configfile:
            self.write(configfile)  
