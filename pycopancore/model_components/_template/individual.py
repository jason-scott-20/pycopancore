"""Individual entity type class template.

TODO: adjust or fill in code and documentation wherever marked by "TODO:", 
then remove these instructions
"""

# This file is part of pycopancore.
#
# Copyright (C) 2016 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

# import all interface classes since one typically wants to cross-ref 
# variables between entity types (this is the whole point of having an 
# interface in the first place):
from .interface import * 


class Individual(Individual_):
    """Individual entity type mixin implementation class"""

    # standard methods:
    
    def __init__(self,
                 # ,*,
                 **kwargs):
        """Initialize an instance of Individual."""
        super().__init__(**kwargs) # must be the first line
        # TODO: add custom code here:
        pass

    def deactivate(self):
        """Deactivate an individual."""
        # TODO: add custom code here:
        pass
        super().deactivate() # must be the last line

    def reactivate(self):
        """Reactivate an individual."""
        super().reactivate() # must be the first line
        # TODO: add custom code here:
        pass


    # process-related methods:

    # TODO: add some if needed...
    
    processes = [] # TODO: instantiate and list process objects here