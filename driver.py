from blockchainExplorer import blockchainExplorer

blockExplorer = blockchainExplorer()

blockExplorer.addSurgery(1,1,[1,2,3,4],"HEART REMOVAL", "REMOVE IT WITH A SPOON", "algo a escribir", "10/10/2023")
blockExplorer.addAllergy(1, "Onions", "21/10/2023", "Don't eat onions.", "Not too serious")
blockExplorer.addAppointment(1, 2, 23, "Leg hurts", "22/12/23", "12:45")
blockExplorer.addDrug(1,1, "Paracetamol", "21/10/2023", "28/10/2023", "Headaches", "Take 2 pills a day.")
blockExplorer.addIncident(1, [2,2,3], "se cayó por las escaleras", "Se cayó pro las escaleras y se hizo un esguince en el tobillo.", "15/10/2023", "Aplicar hielo y tomar antinflamantes")
blockExplorer.addInjury(1, 123, [2,3,4], "Rotura de rodilla", "jugando a voley clavó el pie y partió la rodilla", "21/5/2023", "Le ha pasado varias veces")
blockExplorer.addUserHasAccess(1,2, "21/10/2023")
returned= blockExplorer.searchHistory(1, False, False,False,False,False,False,True)
for a in returned:
    print(a.convertJSON())