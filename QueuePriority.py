
# 
#Suponemos que las prioridades empiezan desde 0, en casp de empezar de 1
# recordar agregar un +1
		
class ElementListWithPriority:
	def __init_(self,element,elementRight,elementLeft,priority):
	 self.element=element
	 self.elementRight=elementRight
	 self.elementLeft=elementLeft
	 self.priority=priority
	def elementNotOrder(self,element,priority):
		self.element=elemennt
		self.priority=priority
		self.elementRight=null
		self.elementLeft=null
		
#Manejo de lista para mantener las propiedades	 
	def agregarElementRight(self,element):
	    self.elementRight=element
	    element.elementLeft=self
	def agregarElementLeft(self,element):
		self.elementLeft=element
		element.elementRight=self
		
class ListPriority:
		def __init__(self):
			self.listPriority=[]
		def appendElementListPriority(self,element):
#Modificacion del append 		
			self.last.agregarElementRight(element)
			element.agregarElementLeft(self.last)
			self.append(element)
		def addElementOnePosition(self,element,elementLeft,elementRight):
#Metodo que me permite agregar en cualquier posicion solo sabiendo los elementos de los costados		
			element.agregarElementLeft(elementLeft)
			element.agregarElementRight(elementRight)
			self.insert(self.index(elementRight),element)

class ListWithPriority:
	def __init__(self):
	 self.listPriority=ListPriority()
	 self.elementList=ListPriority()
	 
	 	            
	def getRightElement(self,element):
			rightAux=self.elementQueue.index(self.priorityList(element.priority+1))
			return rightAux
			
	def getLeftElement(self,element):
			leftAux=self.elementQueue[self.elementQueue.index((self.priorityList(element.priority+1)) - 1)]
			return leftAux
			
			
	def equalPriority(self,element):    
		   self.elementPriority.appendElementListPriority(element)
		   
	def notEqualorHighPriority(self,element):
			self.listPriority.appendElementListPriority(element)
		    self.elementList.appendElementListPriority(element)
		    
	def highPriority(self,element):
			self.elementLis.addElementOnePosition(element,self.getLeftElement(element),self.getRightElement(element))
			
	def addElementQueuePriority(self,element):
	    if element.priority < self.listPriority.size
			self.notEqualorHighPriority(element)
		elif element.priority > self.listPriority.size
			self.highPriority(element)
		else
			self.equalPriority(element)
			

		
	
	
	
	
	
	


def main():
	
	a=ElementListWithPriority("charlie",1)
	return a

if __name__ == '__main__':
	main()
