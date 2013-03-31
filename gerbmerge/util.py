#!/usr/bin/env python
"""
Various utility functions

--------------------------------------------------------------------

This program is licensed under the GNU General Public License (GPL)
Version 3.  See http://www.fsf.org for details of the license.

Rugged Circuits LLC
http://ruggedcircuits.com/gerbmerge
"""

def in2gerb(value):
  """Convert inches to 2.5 Gerber units"""
  return int(round(value*1e5))

def gerb2in(value):
  """Convert 2.5 Gerber units to inches"""
  return float(value)*1e-5
