# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:47:16 2016

@author: bushnelf
"""

from Building import Building
from Resource import Resource


class ProductionBuilding(Building):
    """
    A production building specifically facilitates the production
    of a resource / crop.  It is required that the building be staffed
    in order to be productive.  It is also required that the player
    with the production building also possess plantation(s) of the
    corresponding type.
    """

    def __init__(self, nm, col_slots, clr, cost, vp, sz, qd, crop):
        Building.__init__(self, nm, col_slots, clr, cost, vp, sz, qd)
        self.__resource = crop

    def crop(self):
        return self.__resource

if __name__ == '__main__':
    r = Resource("indigo", 1, "blue")
    pb = ProductionBuilding("indigo plant", 3, "blue", 3, 2, 1, 2, r)
    print "Prod bldg " + pb.name + " costs " + str(pb.cost) + "."
    print "It has " + str(pb.colonist_slots) + " colonist slots."
    print "It produces " + pb.crop().name + " that has value " + \
        str(pb.crop().market_value) + "."
