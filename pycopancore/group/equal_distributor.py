# This file is part of pycopancore.
#
# Copyright (C) 2016 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

"""
Equal_Distributor is a subclass of 'Group' and describes a more specific
behaviour of macro agents in the coevolutionary system.
"""

#
#  Imports
#

from .abstract_group import Group

#
#  Define class MacroAgents
#


class EqualDistributor(Group):
    """
    Equal_Distributor is a subclass of 'Group' and describes a more specific
    behaviour of macro agents.
    """

    #
    #  Definitions of internal methods
    #

    def __init__(self,
                 group_identifier,
                 territories=None,
                 member=None,
                 group_connection=None,
                 group_stock=None,
                 group_harvest=None,
                 group_strategy=None):
        """
        Initializes an instance of 'Equal_Distributor'.
        Inherits group_identifier, territories and member from 'Group'.

        Parameters
        ----------
        group_identifier: integer
            This integer identifies each group
        territories: list of integers
            This list contains cell_identifiers which are the groups
            territories
        member: list of tuples of integers
            This list has tuples of integers of the form
            (individual_identifier, cell_identifier)
            This adds up to the memberlist with all individuals affilitated to
            their group and their cell
        group_connection: list
            This lists existing connections of corresponding group
        group_stock: float
            Summed up stock of territories
        group_harvest: float
            Total harvest of one group
        group_strategy: integer
            The strategy of a group [1 denotes sus.; 0 denotes non-sus.]
            Results from member's strategy.
        """
        super(EqualDistributor, self).__init__(group_identifier,
                                               territories,
                                               member,
                                               group_connection
                                               )
        self.group_stock = None
        self.group_harvest = None
        self.group_strategy = None

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return (super(EqualDistributor, self).__str__() +
                ('group_stock % s, \
                 group_harvest % s, \
                 group_strategy % s'
                 ) % (
                 self.group_stock,
                 self.group_harvest,
                 self.group_strategy
                 )
                )

    def set_group_stock(self, group_stock):
        """
        A function to set the total stock of a group.
        """
        self.group_stock = group_stock

    def set_group_harvest(self, group_harvest):
        """
        A function to set the total harvest of a group.
        """
        self.group_harvest = group_harvest

    def set_group_strategy(self, group_strategy):
        """
        A function to set group's strategy.
        """
        self.group_strategy = group_strategy

    #
    #  Definitions of further methods
    #
    
    def get_ingredients(self):
        """
        This function returns a list of tuples, each of the form (label, type,
        list of affected variables, specification). Entries of each tuple are
        specified in the following clarification

        Clarification
        -------------
        label : string
            The denotation of the dynamical system
        type : string
            The type of the dynamics. Can be either "explicit", "derived",
            "ODE", "step" or "event"
        list of affected variables: any dtype
            List of all variables that are affected from the specified dynamics
        specification : any dtype
            Further specifications that are necessary for the global
            integration (e.g. methods to solve the specified dynamics)
        """
        return []

    def calculate_deathrate():
        """
        Method to calculate the deathrate in dependence of the harvest
        """

    def calculate_birthrate():
        """
        Method to calculate the birthrate in dependece of the harvest
        """