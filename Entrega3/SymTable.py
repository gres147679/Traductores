# -*- coding: utf-8 -*-
# Proyecto Traductores e Interpretadores. Entrega 2
# Realizado por:
# Wilmer Bandres. 1010055
# Gustavo El Khoury. 1010226

class variable():
  def __init__(self,id,type,block = None):
    self.id = id
    self.type = type
    self.lineno = -1
    self.colno = -1
    if block is None:
      self.blocked = 0
    else:
      self.blocked = block    
      
  def setLine(self,line):
    self.lineno = line
  
  def setColumn(self,col):
    self.colno = col
    
  def setType(self,type):
    self.type = type
    
  def __eq__(self,otro):
    return self.id == otro.id
  
  def __str__(self):
    return "variable: " + str(self.id) + " | tipo: " + str(self.type)
  

class SymTable():
  def __init__(self):
    self.lista = []
    
  def insert(self,var):
    error = 0
    if self.isMember(var.id,0):
      error = 1
    else:
      self.lista.append(var)
    return error
    
    
      
    
  def delete(self,var):
    if self.isMember(var.id,0):
      self.lista.remove(var)
    
  def update(self,var):
    pass
  
  def isMember(self,var,verbose):
    try:
      self.lista.index(variable(var,''))
    except ValueError:
      if verbose:
	print "El valor no se encuentra en la tabla de simbolos"
      return 0
    return 1
    
  def find(self,id):
    if self.isMember(id,0):
      return self.lista[self.lista.index(variable(id,''))]
    else:
      return None
    
  def merge(self,nuevaTabla):
    error = None
    for i in nuevaTabla.lista:
      if self.isMember(i.id,0):
	error = (i.lineno,i.colno,i.id)
      else:
	self.insert(i)
    return error
	
  def __str__(self):
    retorno = ''
    for i in self.lista:
      retorno += str(i)
      retorno += '\n'
    return retorno

#lista = SymTable()
#lista.insert(variable('xx1','boolean'))
#print lista.isMember(variable('xx1','boolean'),0)
#lista.delete(variable('xx1','boolean'))
#print lista.isMember(variable('xx1','boolean'),0)
#lista.insert(variable('xx1','boolean'))
#print lista.find('xx12')
