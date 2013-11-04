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

class Instruction:
	def __init__(self)
		self.cpu=0
		self.io=0
		
	def execute(self):
		pass
		
class CpuInstruction:
	
	def __init__(self,command):
		cpuInstructionAux=Instruction()
		cpuInstructionAux.cpu=1
		cpuInstructionAux.command=command
		return cpuInstructionAux
		
	def execute(self,pcb):
		pcb.status="cpu"
		pcb.nextCurrentInstruction
		print "Run in CPU"
		
		
class IoInstruction:
	
	def __init__(self,device)
		ioInstructionAux=Instruction()
		ioInstructionAux.io=0
		ioInstructionAux.device=device
		return ioInstructionAux
		
	def execute(self,pcb)
		pcb.status="io"
		pcb.nextCurrentInstruction
def main():
	
	return 0

if __name__ == '__main__':
	main()

