# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 23:17:16 2016

@author: bushnelf
"""

from Tile import Tile
from Resource import Resource


class Plantation(Tile):
    """
    Includes tiles that produce a resource, e.g. Indigo and Tobacco.
    """

    def __init__(self, nm, col_slots, clr, resrc):
        Tile.__init__(self, nm, col_slots, clr)
        self._resource = resrc

    @property
    def resource(self):
        return(self._resource)

    @resource.setter
    def resource(self, resrc):
        self._resource = resrc

    def produce(self):
        return self.num_colonists

    def fullname(self):
        return self.resource.name + " plantation"

if __name__ == '__main__':
    corn = Resource("corn", 0, "Yellow", False)
    corn_plantation = Plantation("corn", 1, "Yellow", corn)
    print("Corn plantations have " + str(corn_plantation.colonist_slots) +
          " slot(s) for colonists.")
    print("Corn plantation can produce " + str(corn_plantation.produce()) +
          " corn.")
    print("Adding a colonist next...")
    corn_plantation.add_colonist()
    print("Corn plantation can produce " + str(corn_plantation.produce()) +
          " corn.")
