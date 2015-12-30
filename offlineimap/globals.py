# Copyright 2013 Eygene A. Ryabinkin.
#
# Module that holds various global objects.

from offlineimap.utils import const

# Holds command-line options for OfflineIMAP.
options = const.ConstProxy()

# From removed module imaplib2.py
MonthNames = [
    None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
Mon2num = dict(zip((x.encode() for x in MonthNames[1:]), range(1, 13)))

def set_options (source):
    """ Sets the source for options variable """
    options.set_source (source)
