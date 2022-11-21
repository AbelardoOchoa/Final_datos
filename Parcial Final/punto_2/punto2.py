from MultiList import MultiList
liga = MultiList()
liga.addMultiple([["Caimanes de Barranquilla",1],
                ["Gigantes de Barranquilla", 2],
                ["Tigres de Cartagena", 3],
                ["Vaqueros de Monteria", 4],
                ["Getsemani Leones de La Trinidad", 5]])
liga.Recorrido()

liga.AddMultipleToBranch([["Hernu00e1n Guzmu00e",	5],
                        ["Jasier Herrera",	10],
                        ["Ramu00f3n Ulacio",	4],
                        ["Eduin Villa",	1],
                        ["Josu00e9 Puerta",	3],
                        ["u00c1ngel Vilchez",	4],
                        ["Kermin Guardia",	23],
                        ["Hugo Beltru00e1n",	1],
                        ["Juan Diaz",	7],
                        ["Wirkin Estu00e9vez",	0],
                        ["Rodrigo Benoit",	6],
                        ["Gabriel Pu00e9rez",	10],
                        ["Yaramil Hiraldo",	1],
                        ["Wilson Lu00f3pez",	3],], 2)
liga.AddMultipleToBranch([["Porfilio L\u00f3pez",	"1"]
                        ["Euclides Leyer",	"1"],
                        ["Eduar L\u00f3pez",	"3"],
                        ["Reiver Sanmartin",	"14"],
                        ["Ezequiel Zabaleta",	"15"],
                        ["Erling Moreno",	"0"],
                        ["Yhonatan Barrios",	"2"],
                        ["Kevin Escorcia",	"9"],
                        ["Elkin Alcal\u00e1",	"6"],
                        ["Guillermo Z\u00fa\u00f1",	"9"],
                        ["Sugar Ray Marim\u00f3n",	"1"],
                        ["Jos\u00e9 Valdespina",	"0"],
                        ["Yeizer Marrugo",	"0"],
                        ["Sergio Palacio",	"0"],
                        ["Jos\u00e9 Altamiranda",	"0"],
                        ["Jhon Vergara",	"0"],
                        ["Alberto Torres",	"0"], 3])
liga.AddToBranch(["None",	0], 5)


liga.RecorridoTotal()