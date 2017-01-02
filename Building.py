# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 23:01:36 2016

@author: bushnelf
"""

from Tile import Tile


class Building(Tile):
    """
    A building represents the ability to process a resource (e.g., an
    tobacco storage building) or adjust the effect in a given action
    (e.g., small market yielding an extra doubloon with a sale in
    the trader phase or a large warehouse allowing the storage of 2
    kinds of goods / resources in the captain phase).
    """

    def __init__(self, nm, col_slots, clr, cost, vp, sz, qd):
        Tile.__init__(self, nm, col_slots, clr)
        self._cost = cost
        self._victory_points = vp
        self._size = sz
        self._max_quarry_deduction = qd
        self._available = True

    @property
    def cost(self):
        return(self._cost)

    @cost.setter
    def cost(self, val):
        self._cost = val

    @property
    def victory_points(self):
        return(self._victory_points)

    @victory_points.setter
    def victory_points(self, val):
        self._victory_points = val

    @property
    def size(self):
        return(self._size)

    @size.setter
    def size(self, val):
        self._size = val

    def purchase(self):
        self._available = False

if __name__ == '__main__':
    h = Building("hacienda", 1, "purple", 2, 1, 1, 1)
    print("The " + h.name + " building has cost " + str(h.cost))
