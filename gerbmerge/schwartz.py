"""
Implement the Schwartizan Transform method of sorting
a list by an arbitrary metric (see the Python FAQ section
4.51).
--------------------------------------------------------------------

This program is licensed under the GNU General Public License (GPL)
Version 3.  See http://www.fsf.org for details of the license.

Rugged Circuits LLC
http://ruggedcircuits.com/gerbmerge
"""

def stripit(pair):
  return pair[1]

def schwartz(List, Metric):
  def pairing(element, M = Metric):
    return (M(element), element)

  paired = map(pairing, List)
  paired.sort()
  return map(stripit, paired)

def stripit2(pair):
  return pair[0]

def schwartz2(List, Metric):
  "Returns sorted list and also corresponding metrics"

  def pairing(element, M = Metric):
    return (M(element), element)

  paired = map(pairing, List)
  paired.sort()
  theList = map(stripit, paired)
  theMetrics = map(stripit2, paired)
  return (theList, theMetrics)
