from MultiList import MultiList
liga = MultiList()
liga.addMultiple([["Caimanes de Barranquilla",1],
                ["Gigantes de Barranquilla", 2],
                ["Tigres de Cartagena", 3],
                ["Vaqueros de Monteria", 4],
                ["Getsemani Leones de La Trinidad", 5]])
liga.Recorrido()

liga.AddMultipleToBranch([["Elkin Alcalu00e1", 28],
                        ["Rodrigo Benoit", 55],
                        ["Randy Consuegra",	27],
                        ["Luis De u00c1vila", 21],
                        ["Juan Du00edaz", 20],
                        ["Elniery Garcu00eda", 41],
                        ["Donald Goodson", 67],
                        ["Yaramil Hiraldo", 42],
                        ["Joel Inoa", 37],
                        ["Francisco Jimu00e9nez", 42],
                        ["Porfirio Lu00f3pez", 99],
                        ["Eduar Lu00f3pez",	16],
                        ["Deivy Mu00e9ndez", 25],
                        ["Luis Moreno",	31],
                        ["Jeffry Niu00f1o",	69],
                        ["Fernando Pu00e9rez", 47],
                        ["Ronald Ramu00edrez", 46]], 1)

liga.AddMultipleToBranch([["Hernu00e1n Guzmu00e", 5],
                        ["Jasier Herrera",	10],
                        ["Ramu00f3n Ulacio", 4],
                        ["Eduin Villa",	1],
                        ["Josu00e9 Puerta",	3],
                        ["u00c1ngel Vilchez", 4],
                        ["Kermin Guardia", 23],
                        ["Hugo Beltru00e1n", 1],
                        ["Juan Diaz", 7],
                        ["Wirkin Estu00e9vez", 0],
                        ["Rodrigo Benoit", 6],
                        ["Gabriel Pu00e9rez", 10],
                        ["Yaramil Hiraldo",	1],
                        ["Wilson Lu00f3pez", 3]], 2)

liga.AddMultipleToBranch([["Porfilio Lu00f3pez", 1],
                        ["Euclides Leyer",	1],
                        ["Eduar Lu00f3pez",	3],
                        ["Reiver Sanmartin", 14],
                        ["Ezequiel Zabaleta", 15],
                        ["Erling Moreno", 0],
                        ["Yhonatan Barrios", 2],
                        ["Kevin Escorcia", 9],
                        ["Elkin Alcalu00e1", 6],
                        ["Guillermo Zu00fau00f1",9],
                        ["Sugar Ray Marimu00f3n", 1],
                        ["Josu00e9 Valdespina",	0],
                        ["Yeizer Marrugo",	0],
                        ["Sergio Palacio",	0],
                        ["Josu00e9 Altamiranda", 0],
                        ["Jhon Vergara", 0],
                        ["Alberto Torres", 0]], 3)

liga.AddMultipleToBranch([["Luis Ortega", 10],
                        ["Pedro Echemendia", 1],
                        ["Carlos De u00c1vila",	3],
                        ["Edinson Fru00edas", 4],
                        ["Carlos Ocampo",	6],
                        ["Sebastiu00e1n Escobar", 9],
                        ["Jaider Rocha", 1],
                        ["Carlos Diaz",	0],
                        ["Luis Pu00e9rez", 0],
                        ["Jhon Peluffo", 0],
                        ["Ely Moru00f3n", 10],
                        ["Misael Siverio",	11],
                        ["Cody Mincey",	8],
                        ["Hernando Meju00eda",	0],
                        ["Josu00e9 Rodruedguez", 1],
                        ["Juan Polo", 2],
                        ["u00c1ngel Vilchez", 1],
                        ["Jorge Martu00ednez", 4],
                        ["Reynaldo Polanco", 1],
                        ["u00c1lvaro Galindo", 6]], 4)                    

liga.AddToBranch(["None",	0], 5)


#liga.RecorridoTotal()