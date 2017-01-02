# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 20:03:53 2016

@author: bushnelf
"""

from ProductionBuilding import ProductionBuilding
from Plantation import Plantation
from Ship import Ship
from Role import Role
from Resource import Resource


class GameBoard:
    """
    GameBoard represents the game board, including all the building
    tiles available for purchase, the colonists available for putting
    on ships, the resources available for production, the doubloons
    available (that actually might not be limited), the cargo and
    colonist ships, victory point chips (limited), the roles, and
    the governor.
    """

    def __init__(self, plyrs):
        self._num_players = plyrs
        self._prod_bldgs = []
        self._violet_bldgs = []
        self._colonists = 0
        self._active_plantations = []
        self._reserve_plantations = []
        self._quarries = []
        self._victory_points = 0
        self._colony_ship = None
        self._cargo_ships = []
        self._goods = [10, 12, 11, 9, 8]
        self._roles = []

    @property
    def colonists(self):
        return self._colonists

    @colonists.setter
    def colonists(self, val):
        self._colonists = val

    def remove_colonists(self, howmany):
        self._colonists -= howmany

    def set_up_ships(self):
        self._colony_ship = Ship("Colonist Ship", 200, "colonists")
        ship_sizes = [[4, 5, 6], [5, 6, 7], [6, 7, 8]]
        for ship_num in range(3):
            ship = Ship("Cargo Ship " + str(ship_num + 1),
                        ship_sizes[self._num_players - 3][ship_num], "")
            self._cargo_ships.append(ship)

    @property
    def cargo_ships(self):
        return self._cargo_ships

    @property
    def goods(self):
        return self._goods

    def corn_idx(self):
        return 0

    def indigo_idx(self):
        return 1

    def sugar_idx(self):
        return 2

    def tobacco_idx(self):
        return 3

    def coffee_idx(self):
        return 4

    def set_up_prod_bldgs(self):
        """
        We will construct the production buildings here, using the basic
        ProductionBuilding class, rather than having separate classes
        for each type of building.
        """

        # set up resources for buildings first, e.g.
        # corn = Resource("Corn", 0, "Yellow", False)
        indigo = Resource("indigo", 1, "Blue", True)
        sugar = Resource("sugar", 2, "White", True)
        tobacco = Resource("tobacco", 3, "Brown", True)
        coffee = Resource("coffee", 4, "Black", True)

        # constructor for production building:
        # __init__(self, nm, col_slots, clr, cost, vp, sz, qd, crop):
        # example call to create a production building:
        # ProductionBuilding("indigo plant", 3, "blue", 3, 2, 1, 2, r)

        for i in range(4):
            b = ProductionBuilding("small indigo plant", 1, "Blue", 1, 1,
                                   1, 1, indigo)
            self._prod_bldgs.append(b)
        for i in range(3):
            b = ProductionBuilding("indigo plant", 3, "Blue", 3, 2, 1, 2,
                                   indigo)
            self._prod_bldgs.append(b)
        for i in range(4):
            b = ProductionBuilding("small sugar plant", 1, "White", 2, 1,
                                   1, 1, sugar)
            self._prod_bldgs.append(b)
        for i in range(3):
            b = ProductionBuilding("sugar plant", 3, "White", 4, 2,
                                   1, 2, sugar)
            self._prod_bldgs.append(b)
        for i in range(3):
            b = ProductionBuilding("tobacco storage", 3, "Brown", 5, 3,
                                   1, 3, tobacco)
            self._prod_bldgs.append(b)
        for i in range(3):
            b = ProductionBuilding("coffee roaster", 3, "Black", 6, 3,
                                   1, 3, coffee)
            self._prod_bldgs.append(b)

    @property
    def prod_bldgs(self):
        return self._prod_bldgs

    def set_up_violet_bldgs(self):
        pass

if __name__ == '__main__':
    gb = GameBoard(4)
    gb.set_up_ships()
    for ship in gb.cargo_ships:
        print ship.name + " has " + str(ship.max_slots) + " capacity."
    print "Game board has " + str(gb.goods[gb.coffee_idx()]) + " coffee."
    gb.set_up_prod_bldgs()
    print "Game board has " + str(len(gb.prod_bldgs)) + " production bldgs."
