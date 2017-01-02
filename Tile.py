# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:59:35 2016

@author: bushnelf
"""


class Tile:
    """
    Base class for both buildings (e.g. sugar mills & coffee roasters)
    and plantations (e.g. corn & sugar).
    """

    def __init__(self, nm, col_slots, clr):
        self.__name = nm
        self.__colonist_slots = col_slots
        self.__num_colonists = 0
        self.__color = clr

    def game_effect(self):
        pass

    @property
    def name(self):
        return(self.__name)

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def colonist_slots(self):
        return(self.__colonist_slots)

    @colonist_slots.setter
    def colonist_slots(self, val):
        self.__colonist_slots = val

    @property
    def num_colonists(self):
        return(self.__num_colonists)

    @num_colonists.setter
    def num_colonists(self, val):
        self.__num_colonists = val

    @property
    def color(self):
        return(self.__color)

    @color.setter
    def color(self, val):
        self.__color = val

    def can_add_colonist(self):
        return(self.num_colonists < self.colonist_slots)

    def add_colonist(self):
        if self.can_add_colonist():
            self.__num_colonists += 1
        # Should probably throw an exception here - what type?

    def colonist_slots_avail(self):
        return self.__colonist_slots - self.__num_colonists

if __name__ == '__main__':
    tile = Tile("Generic tile", 0, "Puke green")
    print("The generic tile should not be instantiated")
