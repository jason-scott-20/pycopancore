# This file is part of pycopancore.
#
# Copyright (C) 2016 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

"""
Encapsulates states and dynamics of social macro agents.
"""

#
#  Imports
#

#
#  Define class Group
#


class Group(object):
    """
    Encapsulates states and dynamics of social macro agents.
    """

    #
    #  Definitions of internal methods
    #

    def __init__(self,
                 group_identifier,
                 territories=None,
                 member=None,
                 group_connection=None):
        """
        Initialize an instance of 'Group'.

        Parameters
        ----------
        group_identifier : integer
            This integer identifies each group
        territories : np.array
            This array contains cell_identifiers which are the groups
            territories. It has dimensions of (number of cells, 1)
            TODO: Write assert statement into test od model (?) to make shure
            this is always the case
        member : list of tuples of integers
            This list has tupels of integers of the form
            (individual_identifier, cell_identifier)
            This adds up to the memberlist with all individuals affiliated to
            the group and their cell
        group_connection : list
            This lists existing connections of corresponding group
        """

        self.group_identifier = group_identifier
        self.territories = territories
        self.member = member
        self.group_connection = group_connection

    def __str__(self):
        """
        Return a string representation of the object of class individual
        """
        return ('Group with identifier % s, \
                territories % s, \
                member % s, \
                group_connection % s'
                ) % (
                self.group_identifier,
                self.territories,
                self.member,
                self.group_connection)

    def set_territories(self, territories):
        """
        a function to set the territories of a group, territories is a list
        of cell_identifiers
        """
        self.territories = territories

    def set_member(self, member):
        """
        A function that generates a List with all members and the
        following information: individual_identifier, cell identifier
        """
        self.member = member

    def set_group_connection(self, group_connection):
        """
        A function to set the list of connections for the group
        """
        self.group_connection = group_connection

    #
    #  Definitions of further methods
    #

    def get_population(self, member):
        """
        Method to get the amount of individuals in the society. Necessary to
        calculate the total harvest.
        """
        return len(self.member)