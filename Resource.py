# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:12:31 2016

@author: bushnelf
"""


class Resource:
    """
    Covers crops produced in plantations, e.g. Corn,
    Indigo, Sugar, Tobacco, and Coffee.
    """

    def __init__(self, nm, val, clr, bldg=True):
        self._name = nm
        self._mkt_val = val
        self._color = clr
        self._bldg_reqd = bldg

    @property
    def name(self):
        return(self._name)

    @name.setter
    def name(self, nm):
        self._name = nm

    @property
    def market_value(self):
        return(self._mkt_val)

    @market_value.setter
    def market_value(self, mv):
        self._mkt_val = mv

    @property
    def color(self):
        return(self._color)

    @color.setter
    def color(self, clr):
        self._color = clr

    @property
    def building_required(self):
        return(self._bldg_reqd)

    @building_required.setter
    def building_required(self, bldg):
        self._bldg_reqd = bldg

if __name__ == '__main__':
    corn = Resource("Corn", 0, "Yellow", False)
    print("Corn's value is " + str(corn.market_value))
    if corn.building_required:
        print("Corn requires a building")
    else:
        print("Corn _does not_ require a building")
