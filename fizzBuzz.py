#!/usr/bin/env python

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

#gFizzBuzz-Python

def fizzBuzz(number, listBuzz = []):
 if number > 0:
  if not(number%15):
   listBuzz.append("FizzBuzz")
  elif not(number%5):
   listBuzz.append("Buzz")
  elif not(number%3):
   listBuzz.append("Fizz")
  else:
   listBuzz.append(number)
  fizzBuzz(number-1)
 else:
  return listBuzz

def printList(orientation, listBuzz):
  if orientation == "straight":
   listBuzz.reverse()
   print "Printing in straight mode"
  elif orientation == "reverse":
   print "Printing in reverse mode"
  else:
   print "Invalid orientation. Defaulting to straight mode."
  for x in listBuzz:
   print x

if __name__ == '__main__':
 sampleList = []
 fizzBuzz(100, sampleList)
 printList("straight", sampleList)
