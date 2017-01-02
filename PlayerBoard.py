# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:33:07 2016

@author: bushnelf
"""


class PlayerBoard:
    """
    Represents the player board, where a player keeps buildings, resources,
    colonists, etc.
    """

    def __init__(self, nm):
        self._name = nm
        self._buildings = []
        self._plantations = []
        self._resources = []
        self._unallocated_colonists = 0
        self._victory_points = 0
        self._doubloons = 0
        self._max_building_spaces = 12
        self._max_plantation_spaces = 12

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    def add_building(self, bldg):
        # Need to fix this to check whether we have enough spaces to
        # add a building.
        self._buildings.append(bldg)

    def add_plantation(self, plnt):
        # Need to fix this to check whether we have enough spaces to
        # add a plantation.
        self._plantations.append(plnt)

    def add_resource(self, resrc):
        self._resources.append(resrc)

    def add_colonist(self, col):
        self._unallocated_colonists += col

    def add_victory_points(self, vps):
        self._victory_points += vps

    @property
    def doubloons(self):
        return(self._doubloons)

    @doubloons.setter
    def doubloons(self, val):
        self.doubloons = val

    def update_doubloons(self, dblnz):
        """
        Use this method for receiving or spending money
        """
        self._doubloons += dblnz

    def earn_doubloons(self, dblnz):
        self.update_doubloons(dblnz)

    def spend_doubloons(self, dblnz):
        self.update_doubloons(-1 * dblnz)

    def list_tiles(self, tilearr, open_col_slots=False):
        """
        Return a dictionary of crop names and colonist slots,
        either filled (open_col_slots false) or open (true).
        """
        tiles = {}

        for tidx in range(len(tilearr)):
            crop = tilearr[tidx].name
            if open_col_slots:
                cnt = tilearr[tidx].colonist_slots_avail()
            else:
                cnt = tilearr[tidx].num_colonists
            if crop in tiles:
                newcnt = int(tiles[crop]) + cnt
            else:
                newcnt = cnt
            tiles[crop] = newcnt

        return tiles

    def list_buildings(self, open_col_slots=False):
        """
        Return a dictionary of building names and colonist slots,
        either filled (open_col_slots false) or open (true).
        """
        return self.list_tiles(self._buildings, open_col_slots)

    def list_plantations(self, open_col_slots=False):
        """
        Return a dictionary of plantation crop names and colonist slots,
        either filled (open_col_slots false) or open (true).
        """
        return self.list_tiles(self._plantations, open_col_slots)

if __name__ == '__main__':
    pb = PlayerBoard("Player 1")
    pb.earn_doubloons(5)
    print(pb.name + " has " + str(pb.doubloons) + " doubloons.")
    print("Now she will spend 2 of them.")
    pb.spend_doubloons(2)
    print(pb.name + " has " + str(pb.doubloons) + " doubloons.")
    pb.list_buildings()
    pb.list_plantations()
