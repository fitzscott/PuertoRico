# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:20:31 2016

@author: bushnelf
"""

from Resource import Resource


class Ship:
    """
    The Ship class represents a container for resources or colonists.
    The colonist ship can contain an arbitrary number of colonists.
    The trading ship can contain a fixed amount of only one type
    of resource / crop at a time.
    """

    def __init__(self, nm, slots, carrying):
        self.name = nm
        self.max_slots = slots
        self.used_slots = 0
        self.carrying = carrying

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def max_slots(self):
        return self.max_slots

    def getresource(self):
        return self.carrying

    def isfull(self):
        return self.max_slots == self.used_slots

    def addresources(self, cnt):
        self.used_slots += cnt
        if self.used_slots > self.max_slots:
            print "Added too many resources to " + self.name
            self.used_slots = self.max_slots

if __name__ == '__main__':
    colonist_ship = Ship("Colonist Ship", 200, "colonists")
    coffee = Resource("coffee", 3, "black")
    tradeship1 = Ship("Trade Ship 1", 4, coffee)
    tradeship1.addresources(4)
    if tradeship1.isfull():
        resrc = tradeship1.getresource()
        print tradeship1.name + " is full (" + str(tradeship1.max_slots) + \
            ") of " + resrc.name
