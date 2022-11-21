class MultiNodo:
    def __init__(self, equipo, posicion):
        self.equipo = equipo
        self.posicion = posicion
        self.next = None
        self.jugadores = LinkedList()
    
    def __repr__(self):
        return str(self.equipo, self.posicion)

class Nodo:
    def __init__(self, nombre, carreras):
        self.nombre = nombre
        self.carreras = carreras
        self.next = None
        #self.jugadores = LinkedList()
    
    def __repr__(self):
        return str(self.nombre, self.carreras)

class MultiList:
    def __init__(self):
        self.PTR = None
        self.ULT = None
        
    def AddNodeQueue(self, codigo, cantidad):
        P = MultiNodo(codigo, cantidad)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
        
    def AddNodeStack(self, codigo, cantidad):
        p = MultiNodo(codigo, cantidad)
        if(self.PTR == None):
            self.ULT = p
        p.next = self.PTR
        self.PTR = p
    
    
    def AddToBranch(self, data, pos):
        P = self.PTR
        c = 1
        while(c != pos):
            c += 1
            P = P.next
        P.jugadores.AddNodeQueue(data[0], data[1])
        #print(P.branch)

    def AddMultipleToBranch(self, lista, pos):
        for i in range(len(lista)):
            self.AddToBranch(lista, pos)

    def Delete(self, target):
        P = self.PTR 
        AnteP = None 
        while(P.codigo != target and P != None):
            AnteP = P 
            P = P.next 
        if(P == self.PTR): 
            self.PTR = P.next 
            P.next = None 
            P = self.PTR 
        else:
            if(P == self.ULT):
                self.ULT = AnteP 
                P = self.ULT 
                P.next = None
            try:
                if(P.codigo == target):
                    AnteP.next = P.next 
                    P.next = None 
                    P = AnteP.next 
            except:
                print("No se encontró el nodo con data " + str(target))

                
    def Recorrido(self):
        P = self.PTR
        while (P != None):
            print(P.equipo, "- " + str(P.posicion), end=" -> ")
            P = P.next
        print("None")

    def RecorridoBranch(self, pos):
        P = self.PTR
        c = 1
        while P != None and c != pos:
            c += 1
            P = P.next
        print(P.jugadores)

    def RecorridoTotal(self):
        for i in range(len(self)):
            print()
            print(f"Jugadores del equipo {i+1}:")
            self.RecorridoBranch(i+1)
      
    def Invertir(self):
        P = self.PTR
        Q = self.ULT
        anteP = None
        while (Q != self.PTR):
            if(P == Q):
                P.next = anteP
                Q = anteP
                anteP = None
                P = self.PTR
            else:
                anteP = P
                P = P.next
        P = self.PTR
        Q = self.ULT
        P.next = None
        self.PTR = Q
        self.ULT = P

    def Ordenar(self):
        P = self.PTR
        Q = self.PTR
        t = 0
        while(P != None):
            Q = P
            Q = Q.next
            while(Q != None):
              if(P.data > Q.data):
                t = P.data
                P.data = Q.data
                Q.data = t
            Q = Q.next
        P = P.next

    def AddOrdered(self, code, cantidad):
      if(self.PTR == None):
        P = MultiNodo(code, cantidad)
        self.PTR = P
        self.UlT = P
      else:
        P = self.PTR
        anteP = None
        while(P != None and P.codigo < code):
          anteP = P
          P = P.next
        if(P.codigo == code):
          print("No se aceptan repetidos.")
        else:
          Q = MultiNodo(code, cantidad)
          Q.next = P
          if(anteP != None):
            anteP.next = Q
            if(Q.next == None):
              self.ULT = Q
              anteP = Q
          else:
            self.PTR = Q
            P = Q

    def addMultiple(self, multiple):
        for i in range(len(multiple)):
            self.AddNodeQueue(multiple[i][0], multiple[i][1])

    def __repr__(self):
        respuesta = ""
        P = self.PTR
        if len(self) > 0:
            while (P != None):
                respuesta = respuesta + str(P.jugadores.nombre) + str(P.jugadores.carreras) + " -> "
                P = P.next
            respuesta = respuesta + "None"
            return respuesta
        else:
            return "Lista vacía."

    def __len__(self):
        count = 0
        node = self.PTR
        try:
            while node != None:
                count += 1
                node = node.next
            return count
        except:
            return 0


class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNodeQueue(self, nombre, carreras):
        P = Nodo(nombre, carreras)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
        
    def AddNodeStack(self, data):
      p = Nodo(data)
      if(self.PTR == None):
        self.ULT = p
      p.next = self.PTR
      self.PTR = p

    def AddAfter(self, target, new):
        P = self.PTR
        while(P != None and P.data != target):
            P = P.next
        if(P == self.ULT):
            Q = Nodo(new) 
            Q.next = None
            P.next = Q 
            self.ULT = Q
        else:
            try:
                if(P.data == target):
                    Q = Nodo(new) 
                    Q.next = P.next 
                    P.next = Q 
            except:
                print("No se encontró el nodo con data " + str(target))
                
    def AddBefore(self, target, new):
        P = self.PTR
        anteP = None
        while(P != None and P.data != target):
            anteP = P
            P = P.next
        if(P == self.PTR):
            Q = Nodo(new) 
            self.PTR = Q
            Q.next = P
        else:
            try:
                if(P.data == target):
                    Q = Nodo(new) 
                    Q.next = P
                    anteP.next = Q
                    P.next = None
            except:
                print("No se encontró el nodo con data " + str(target))
    
    def Delete(self, target):
        P = self.PTR 
        AnteP = None 
        while(P.data != target and P != None):
            AnteP = P 
            P = P.next 
        if(P == self.PTR): 
            self.PTR = P.next 
            P.next = None 
            P = self.PTR 
        else:
            if(P == self.ULT):
                self.ULT = AnteP 
                P = self.ULT 
                P.next = None
            try:
                if(P.data == target):
                    AnteP.next = P.next 
                    P.next = None 
                    P = AnteP.next 
            except:
                print("No se encontró el nodo con data " + str(target))
              
    def Recorrido(self):
        P = self.PTR
        while (P != None):
            print(P.data, end="->")
            P = P.next
        print("None")
      
    def Invertir(self):
        P = self.PTR
        Q = self.ULT
        anteP = None
        while (Q != self.PTR):
            if(P == Q):
                P.next = anteP
                Q = anteP
                anteP = None
                P = self.PTR
            else:
                anteP = P
                P = P.next
        P = self.PTR
        Q = self.ULT
        P.next = None
        self.PTR = Q
        self.ULT = P

    def Ordenar(self):
      P = self.PTR
      Q = self.PTR
      t = 0
      while(P != None):
        Q = P
        Q = Q.next
        while(Q != None):
          if(P.data > Q.data):
            t = P.data
            P.data = Q.data
            Q.data = t
          Q = Q.next
        P = P.next

    def OrdenarS(self):
      P = self.PTR
      Q = self.PTR
      t = 0
      while(P.next != None):
        Q = Q.next
        while(Q != None):
          if(P.data > Q.data):
            t = P.data
            P.data = Q.data
            Q.data = t
          Q = Q.next
        P = P.next
  
    def AddOrdered(self, dato):
      if(self.PTR == None):
        P = Nodo(dato)
        self.PTR = P
        self.UlT = P
      else:
        P = self.PTR
        anteP = None
        while(P != None and P.data < dato):
          anteP = P
          P = P.next
        if(P.data == dato):
          print("No se aceptan repetidos.")
        else:
          Q = Nodo(dato)
          Q.next = P
          if(anteP != None):
            anteP.next = Q
            if(Q.next == None):
              self.ULT = Q
              anteP = Q
          else:
            self.PTR = Q
            P = Q
            
    def E1(self, lis):
      P = self.PTR
      P2 = lis.PTR
      anteP = None
      while(P2 != None):
        anteP = P
        P = self.PTR
        while(P != None):
          if(P.data == P2.data):
            while(P.data == P2.data and P == self.PTR):
              #Caso PTR 
              self.PTR = P.next 
              P.next = None 
              P = self.PTR 
          if(P.data == P2.data and P == self.ULT):
              #Caso ULT
              self.ULT = anteP
              P = self.ULT
              P.next = None
          if(P.data == P2.data):  
            anteP.next = P.next 
            P.next = None
            P = anteP.next 
          else:
            anteP = P
            P = P.next
        P2 = P2.next 
          
          
    def E2(self):
      P = self.PTR
      Q = P
      anteP = None
      anteQ = None
      C = 0; rep = 0; V = []
      while(P != None):
        Q = self.PTR
        while(Q != None):
          if(P.data == Q.data):
            rep = rep + 1
          Q = Q.next
        if(rep <= 1):
          C = C+1
          V.append(P.data)
        rep = 0
        anteP = P
        P = P.next
      print("El número de nodos que no se repiten es: "+ str(C))
      print("\nY son:")
      for i in range(len(V)):
        print(V[i])
 


    def E4(self):
      P = self.PTR
      anteP = None
      while(P != None):
        if(P.data < 0):
          if(P == self.PTR):
            Q = Nodo(-1000) 
            self.PTR = Q
            Q.next = P
            anteP = P
            P = P.next
          else:
            try:
              if(P.data < 0):
                Q = Nodo(-1000) 
                Q.next = P
                anteP.next = Q 
                anteP = P
                P =  P.next
            except:
                print("Error")
        elif(P.data > 0):
          if(P == self.ULT):
            Q = Nodo(1000) 
            Q.next = None
            P.next = Q 
            self.ULT = Q
            P = P.next
            P = P.next
          else:
            try:
                if(P.data > 0):
                    Q = Nodo(1000)
                    Q.next = P.next
                    P.next = Q 
                    anteP = P
                    P = P.next
                    anteP = P
                    P = P.next
            except:
                print("Error")
        else:
          if(P == self.PTR): 
            self.PTR = P.next 
            P.next = None 
            P = self.PTR 
          else:
            if(P == self.ULT):
                self.ULT = anteP 
                anteP.next = None
            try:
                if(P.data == 0):
                    anteP.next = P.next
                    P.next = None 
                    P = anteP.next 
            except:
              print("Error")
    def E8(self):
      P = self.PTR
      C = 0; t = 0
      sw = True
      k = int(input("\nDigite el k nodo a eliminar en la lista.\n"))
      while(P != None):
        C = C + 1
        if(C == k):
          t = P.data
          self.Delete(P.data)
          sw = False
        P = P.next
      if(sw):
        print("No se encontró el " + str(k) + "° nodo en la lista y esta quedó igual:")
      else:
        print("\nEl nodo borrado fue " +str(t) + " y la lista quedó así:")
        
    def E9(self, lista2):
      P = self.PTR
      P2 = lista2.PTR
      sw = False; eq = False
      C1 = 0; C2 = 0
      while(P != None):
        C1 = C1 + 1
        P = P.next 
        
      while(P2 != None):
        C2 = C2 + 1
        P2 = P2.next
        
      P = self.PTR; P2 = lista2.PTR
      print("\nComprobamos si las listas tienen la misma cantidad de nodos y si es así las ordenamos.")
      if(C1 == C2):
        eq = True
        self.Ordenar()
        lista2.Ordenar()
        print("\nLas listas ordenadas quedan de la siguiente manera:")
        self.Recorrido()
        lista2.Recorrido()
      else: 
        eq = False
        print("\nLas listas no tienen la misma cantidad de nodos.\n")
      while(P != None and eq == True):
        if(P.data == P2.data):
          sw = True
        else:
          sw = False 
          break 
        P = P.next
        P2 = P2.next
      if(sw):
        print("Las listas son semejantes.")
      else:
        print("Las listas no son semejantes.")

    def punto1(self, lista2):
      P = self.PTR
      P2 = lista2.PTR
      sw = False; eq = False
      C1 = 0; C2 = 0
      while(P != None):
        C1 = C1 + 1
        P = P.next 
        
      while(P2 != None):
        C2 = C2 + 1
        P2 = P2.next
        
      P = self.PTR; P2 = lista2.PTR
      print("\nComprobamos si las listas tienen la misma cantidad de nodos. De no ser así no serán semejantes.")
      if(C1 == C2):
        eq = True
      else: 
        eq = False
        print("\nLas listas no tienen la misma cantidad de nodos.\n")
      while(P != None and eq == True):
        if(P.data == P2.data):
          sw = True
        else:
          sw = False 
          break 
        P = P.next
        P2 = P2.next
      if(sw):
        print("Las listas son semejantes.")
      else:
        print("Las listas no son semejantes.")
        
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        if len(self) > 0:
            while (P != None):
                respuesta = respuesta + str(P.nombre) + " - " + str(P.carreras) + " -> "
                P = P.next
            respuesta = respuesta + "None"
            return respuesta
        else:
            return "Lista vacía."
    
    def __len__(self):
        count = 0
        node = self.PTR
        try:
            while node != None:
                count += 1
                node = node.next
            return count
        except:
            return 0
        

    def addMultiple(self, multiple):
        for i in range(len(multiple)):
            self.AddNodeQueue(multiple[i])