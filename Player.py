# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:01:14 2016

@author: bushnelf
"""

from PlayerBoard import PlayerBoard


class Player:
    """
    The Player class will have a reference to a player board,
    plus the logic of how to fill it, etc.
    """

    def __init__(self, nm):
        self._pb = PlayerBoard(nm)
        self._role = None

    def add_plantation(self, plnt):
        self._pb.add_plantation(plnt)

    def add_prod_bldg(self, bldg):
        self._pb.add_building(bldg)

    def assign_role(self, rol):
        self._role = rol

    def take_action(self, rol):
        # rol.action(self._pb.list_buildings(), self._pb.list_plantations())
        rol.action(self._pb)

if __name__ == '__main__':
    """
    Depending on the functionality required, these imports may need to
    move back to the top.  For now, though, they are not required.
    """
    from Resource import Resource
    from Plantation import Plantation
    from ProductionBuilding import ProductionBuilding

    p = Player("George")
    r = Resource("tobacco", 3, "brown")
    plnt1 = Plantation("tobacco", 1, "brown", r)
    p.add_plantation(plnt1)
    plnt2 = Plantation("tobacco", 1, "brown", r)
    p.add_plantation(plnt2)
    r2 = Resource("indigo", 1, "blue")
    pb = ProductionBuilding("indigo plant", 3, "blue", 3, 2, 1, 2, r2)
    plants = p._pb.list_plantations(True)
    for plnt in list(plants.keys()):
        print plnt + ": " + str(plants[plnt])
