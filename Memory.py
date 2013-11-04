#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sin título.py
#  
#  Copyright 2013 C <charlie@linuxmint>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
class MemoryPhysical:
#Pensar que variables maneja la memoria
	def __init__(self):
		self.dictionary={}
		
		
	def mkMemory(self):
		
	 for (dirMemory) in range(0,256):
		self.dictionary[dirMemory]=dirMemory
		
	def sizeMemoryEmpty(self):
		return (256-len(self.dictionary.values()))
		
	def put(self,program):
		if ( self.sizeMemoryEmpty() > program.lengthProgram()):
			self.programAux=program
			for instruction in program.listInstruction :
				self.dictionary[0] =instruction
			
	def put2(self,dirMemory,instruction):
		self.instrucionAux=instruction
		self.dictionary[dirMemory]=self.instructionAux
		
	def get(self,dirMemory):
		return self.dictionary[dirMemory]
	   
def main():
	x=MemoryPhysical()
	x.mkMemory()
	print x.dictionary[12]

if __name__ == '__main__':
	main()

