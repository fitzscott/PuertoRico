# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:23:00 2016

@author: bushnelf
"""


class Role:
    """
    The actions chosen by players fulfill roles, e.g.
    settler, captain, builder, craftsman, etc.
    Each role has an action (what the role lets everyone do)
    and a privilege (what it lets its selector do).
    """

    def __init__(self, nm):
        self._name = nm
        self._doubloons = 0
        self._available = True

    @property
    def name(self):
        return(self._name)

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def doubloons(self):
        return(self._doubloons)

    @doubloons.setter
    def doubloons(self, val):
        self._doubloons = val

    @property
    def available(self):
        return(self._available)

    @available.setter
    def available(self, val):
        self._available = val

    def action(self, playboard):
        pass

    def privilege(self, playboard):
        pass

if __name__ == '__main__':
    r = Role("craftsman")
    r.doubloons = 1
    print("Role " + r.name + " has " + str(r.doubloons) + " doubloon.")
