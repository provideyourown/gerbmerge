#!/usr/bin/env python
"""
Various utility functions

--------------------------------------------------------------------

This program is licensed under the GNU General Public License (GPL)
Version 3.  See http://www.fsf.org for details of the license.

Rugged Circuits LLC
http://ruggedcircuits.com/gerbmerge
"""

import config


def in2gerb(value):
# add metric support (1/1000 mm vs. 1/100,000 inch)
    if config.Config['measurementunits'] == 'inch':
      """Convert inches to 2.5 Gerber units"""
      return int(round(value*1e5))
    else: #convert mm to 5.3 Gerber units
      return int(round(value*1e3))

def gerb2in(value):
# add metric support (1/1000 mm vs. 1/100,000 inch)
    if config.Config['measurementunits'] == 'inch':
      """Convert 2.5 Gerber units to inches"""
      return float(value)*1e-5
    else: #convert 5.3 Gerber units to mm
      return float(value)*1e-3
