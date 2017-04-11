"""Model class template."""

# This file is part of pycopancore.
#
# Copyright (C) 2017 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

from .. import base  # all models must use the base component
# from ..model_components import copan_global_like_carbon_cycle \
#     as cc
from ..model_components import anderies_carbon_cycle \
    as cc

# from ..model_components import COMPONENT1 as ABBR1


# entity types:

# by mixing the above model components' mixin classes of the same name.
# Only compose those entity types and process taxons that the model needs,
# delete the templates for the unneeded ones, and add those for missing ones:


class World (cc.World,
             base.World):
    """World entity type."""

    pass


class Society (cc.Society,
               base.Society):
    """Society entity type."""

    pass


class Cell (cc.Cell,
            base.Cell):
    """Cell entity type."""

    pass


class Individual (
                  base.Individual):
    """Individual entity type."""

    pass


# process taxa:

class Nature (cc.Nature,
              base.Nature):
    """Nature process taxon."""

    pass


class Metabolism (
                  base.Metabolism):
    """Metabolism process taxon."""

    pass


class Culture (
               base.Culture):
    """Culture process taxon."""

    pass


# Model class:

class Model (cc.Model,
             base.Model):
    """Class representing the whole model."""

    name = "..."
    """our model"""

    description = "..."
    """Longer description"""

    entity_types = [
        World,
        Society,
        Cell,
        # Individual,
    ]
    """List of entity types used in the model"""

    process_taxa = [
        Nature,
        # Metabolism,
        # Culture,
    ]
    """List of process taxa used in the model"""
