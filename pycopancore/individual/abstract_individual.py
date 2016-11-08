# This file is part of pycopancore.
#
# Copyright (C) 2016 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license


"""
Encapsulates states and dynamics of individuals.
"""

#
#  Imports
#


#
#  Define class Individual
#

class Individual(object):
    """
    Encapsulates states and dynamics of individuals.
    """

    #
    #  Definitions of internal methods
    #

    def __init__(self,
                 individual_identifier,
                 group_affiliation=None,
                 cell_affiliation=None,
                 individual_connection=[],
                 individual_update_time=None
                 ):
        """
        Initialize an instance of individuals:
        The objects of Individual define social micro agents with basic
        parameters that are necessary to describe their behaviour.

        Parameters
        ----------
        individual_identifier : integer
            This is a number which identifies each individual
        group_affiliation : integer
            This is a number which indicates to which group the individual
            is affiliated
        cell_affiliation : integer
            This is a number which indicates to which cell the individual
            is affiliated
        individual_connection: list
            This list shows existing connections of the individual
        individual_update_time : float
            The individual_update_time assigns a time for each individual
            after that adaption and rewiring happens.
        """

        self.individual_identifier = individual_identifier
        self.group_affiliation = group_affiliation
        self.cell_affiliation = cell_affiliation
        self.individual_connection = individual_connection
        self.individual_update_time = individual_update_time

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return ('Individual with identifier % s, \
                group % s, \
                cell % s, \
                individual_connection % s, \
                update_time % s '
                ) % (
                self.individual_identifier,
                self.group_affiliation,
                self.cell_affiliation,
                self.individual_connection,
                self.individual_update_time)

    def set_cell_affiliation(self, cell_affiliation):
        """
        A function to set the location or cell of an individual
        """
        self.cell_affiliation = cell_affiliation

    def set_group_affiliation(self, group_affiliation):
        """
        A function to set the group membership of an individual
        """
        self.group_affiliation = group_affiliation

    def set_update_time(self, update_time):
        """
        A function to set the update_time of the individual
        """
        self.update_time = update_time

    def set_individual_connection(self, individual_connection):
        """
        A function to set the individual_connection of the individual
        """
        self.individual_connection = individual_connection

    def add_individual_connection(self, individual_connection):
        """
        A function to add the individual_connection to the individuals 
        list of connections
        """
        self.individual_connection.append(individual_connection)
    #
    #  Definitions of further methods
    #