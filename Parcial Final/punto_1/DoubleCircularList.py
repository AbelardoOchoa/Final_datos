from DoubleNode import Nodo
class DoubleCircularList:

    """
    Clase hecha por:
    Abelardo Ochoa
    Jhon Jiménez
    Laureano Lafaurie
    Geovani Pérez
    """
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def punto1(self, k, n):
        P = self.PTR
        print("¿Desea intercambiar con un nodo a la derecha o a la izquierda?")
        try:
          direccion = int(input("1 para izquierda, 2 para derecha:\n"))
        except:
          print("Error de tipo, debe ingresar un número entero.")
          print("Ejecute nuevamente.")
        try:
          match direccion:
              case 1: 
                data = self.buscarK(k)
                self.intercambio_izq(data, n)
              case 2:
                data = self.buscarK(k) 
                self.intercambio_der(data, n)
              case _: 
                print("Opción invalida.")
        except:
          return


    def intercambio_der(self, data, cant):
      P = self.PTR
      while P.data != data:
        P = P.next
      aux = P.data
      Q = P
      for k in range(cant):
        Q = Q.next
      for i in range(cant):
        P.data = P.next.data
        P.next.data = aux
        P = P.next
        aux = P.data
      Q = Q.prev
      aux2 = Q.data
      for j in range(cant - 1):
        Q.data = Q.prev.data
        Q.prev.data = aux2
        Q = Q.prev
        aux2 = Q.data
      
    def intercambio_izq(self, data, cant):
      P = self.PTR
      while P.data != data:
        P = P.prev
      aux = P.data
      Q = P
      for k in range(cant):
        Q = Q.prev
      for i in range(cant):
        P.data = P.prev.data
        P.prev.data = aux
        P = P.prev
        aux = P.data
      Q = Q.next
      aux2 = Q.data
      for j in range(cant - 1):
        Q.data = Q.next.data
        Q.next.data = aux2
        Q = Q.next
        aux2 = Q.data
      
    def buscarK(self, k):
      P = self.PTR
      k -= 1
      for i in range(k):
        P = P.next
      x = P.data
      return x

    def AddNodeQueue(self, data):
        P = Nodo(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            P.prev = self.ULT
            self.ULT.next = P
            self.ULT = P
            self.ULT.next = self.PTR
            self.PTR.prev = self.ULT

    def AddNodeStack(self, data):
      P = Nodo(data)
      if(self.PTR == None):
        self.ULT = self.PTR = P
      self.PTR.prev = P
      P.next = self.PTR
      P.prev = self.ULT
      self.PTR = P
      self.ULT.next = P

    def AddAfter(self, target, new):
      P = self.PTR
      Q = self.ULT
      while(P.data != target and Q.data != target and P.next != Q and P != Q):
        P = P.next; Q = Q.prev
      if(Q == self.ULT and Q.data == target):
        R = Nodo(new) 
        R.next = self.PTR
        R.prev = Q
        self.PTR.prev = R
        Q.next = R
        self.ULT = R
      elif(P.data == target):
        R = Nodo(new) 
        R.next = P.next 
        R.prev = P
        P.next.prev = R
        P.next = R
      elif(Q.data == target):
        R = Nodo(new) 
        R.next = Q.next 
        R.prev = Q
        Q.next.prev = R
        Q.next = R
      else:
        print("No se encontró el nodo con data " + str(target))
                
    def AddBefore(self, target, new):
      P = self.PTR
      Q = self.ULT
      while(P.data != target and Q.data != target and P.next != Q and P != Q):
        P = P.next; Q = Q.prev
      if(P == self.PTR and P.data == target):
        R = Nodo(new) 
        R.next = P
        R.prev = self.ULT
        P.prev = R
        self.ULT.next = R
        self.PTR = R
      elif(Q.data == target):
        R = Nodo(new) 
        R.next = Q
        R.prev = Q.prev
        Q.prev.next = R
        Q.prev = R
      elif(P.data == target):
        R = Nodo(new) 
        R.next = P
        R.prev = P.prev
        P.prev.next = R
        P.prev = R
      else:
        print("No se encontró el nodo con data " + str(target))
    
    def Delete(self, target):
      P = self.PTR
      Q = self.ULT
      while(P.data != target and Q.data != target and P.next != Q and P != Q):
        P = P.next; Q = Q.prev
      if(P == self.PTR and P == self.ULT and P.data == target):
        self.PTR = None
        self.ULT = None
      elif(P == self.PTR and P == self.ULT and P.data != target):
        print("No se encontró el nodo con data " + str(target))
      elif(P == self.PTR and P.data == target): 
        self.PTR = P = P.next 
        P.prev = self.ULT
        self.ULT.next = P
      elif(Q == self.ULT and Q.data == target):
        self.ULT = Q = Q.prev
        Q.next = self.PTR
        self.PTR.prev = Q
      elif(P.data == target):
        P.prev.next = P.next
        P.next.prev = P.prev
        P.next = P.prev = None      
      elif(Q.data == target):
        Q.prev.next = Q.next
        Q.next.prev = Q.prev
        Q.next = Q.prev = None
      else:
        print("No se encontró el nodo con data " + str(target))
                                                       
    
    def Recorrido(self):
      P = self.PTR
      Fin = 0
      if self.PTR != None and self.ULT != None:
        print("ULT<->", end = "")
        while (Fin == 0):
          print(P.data, end="<->")
          if(P == self.ULT):
            Fin = Fin + 1
          else:
            P = P.next
        print("PTR")
      else:
        print("La lista está vacía.")
        
  
    def Busqueda(self, target):
      P = self.PTR 
      Q = self.ULT
      if P == None and Q == None:
        return
      elif P == self.PTR and P == self.ULT and P.data == target:
        return True
      elif P == self.PTR and P == self.ULT and P.data != target:
        return False
      else:
        while(P.data != target and Q.data != target and P.next != Q and P != Q):
          P = P.next; Q = Q.prev
        if(P.data == target or Q.data == target):
          #print("Sí existe el valor.")
          return True
        else:
          #print("No existe el valor.")
          return False
        
    def DeleteRep(self, target):
      sw = True
      while sw:
        aux = self.Busqueda(target)
        if aux:
          self.Delete(target)
        else:
          sw = False

    def DeleteLes(self, les):
        P = les.PTR
        Q = self.PTR
        tamaño = len(les)
        linked = []
        aux = 0
        c = 0; x = 0; k = 1
        while(P != None and x < 1000):
            x += 1
            if P.data == Q.data:
                aux += 1
                linked.append(P.data)
                P = P.next; Q = Q.next
            else:
                c += 1
                Q = self.PTR; P = les.PTR
                k = 1
                for i in range(c):
                    Q = Q.next
                    k += 1
                aux = 0
                for i in range(len(linked)):
                    linked.remove(linked[0])
        if aux == tamaño:
            for j in range(aux):
                self.DeleteK(k)
            self.DeleteLes(les)

    def DeleteMulti(self, linked):
        for i in range(len(linked)):
            self.Delete(linked[i])
        
    def DeleteK(self, k):
        P = self.PTR
        c = 1
        while c != k:
            c += 1
            P = P.next
        if(P == self.PTR and k == 1): 
            self.PTR = P = P.next 
            P.prev = self.ULT
            self.ULT.next = P
        elif(P == self.ULT and k == len(self)):
            self.ULT = P = P.prev
            P.next = self.PTR
            self.PTR.prev = P
        else:
            P.prev.next = P.next
            P.next.prev = P.prev
            P.next = P.prev = None   
            
    def DeleteLesRep(self, les):
        P = les.PTR
        while P != None:
            self.DeleteRep(P.data)
            P = P.next
    
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        aux = 0
        respuesta += "ULT<->"
        try:
            while (aux != 1):
                respuesta = respuesta + str(P.data) + "<->"
                P = P.next
                if P == self.PTR:
                    aux += 1
            respuesta = respuesta + "PTR"
            return respuesta
        except:
            return "Lista vacía."
    
    def __len__(self):
        count = 0
        aux = 0
        try:
            node = self.PTR
            while aux != 1:
                count += 1
                node = node.next
                if node == self.PTR:
                    aux += 1
            return count
        except:
            return 0

    def addMultiple(self, multiple):
        for i in range(len(multiple)):
            self.AddNodeQueue(multiple[i])

    def invertir(self):
        P = self.PTR
        Q = self.ULT
        while (Q != self.PTR):
            if(P.next == Q):
                P.next.next = P
                Q = P
                P = self.PTR
            else:
                P = P.next
        P = self.PTR
        Q = self.ULT
        while (P != self.ULT):
            if(Q.prev == P):
                Q.prev.prev = Q
                P = Q
                Q = self.ULT
            else:
                Q = Q.prev
        P = self.PTR
        Q = self.ULT
        self.PTR = Q
        self.ULT = P
        self.PTR.prev = self.ULT
        self.ULT.next = self.PTR