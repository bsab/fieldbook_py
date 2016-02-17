from .controller import *
import logging

# Set up logging
log = logging.getLogger('fieldbook-py')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

alive()
