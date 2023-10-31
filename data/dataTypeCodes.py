class dataTypeCodes:
    def __init__(self):
        self.genesis = 0
        self.surgery = 1
        self.userHasAccess = 2
        self.injury = 3
        self.incident = 4
        self.drug = 5
        self.appointment = 6
        self.allergy = 7

    @staticmethod
    def getType(typeCode:int):
        if typeCode == 0:
            return "Genesis"
        elif typeCode == 1:
            return "Surgery"
        elif typeCode == 2:
            return "UserHasAccess"
        elif typeCode == 3:
            return "Injury"
        elif typeCode == 4:
            return "Incident"
        elif typeCode == 5:
            return "Drug"
        elif typeCode == 6:
            return "Appointment"
        elif typeCode == 7:
            return "Allergy"
        