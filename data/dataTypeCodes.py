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
        self.smartcontract = 8

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
        else:
            return "Smart Contract"
        
    @staticmethod
    def getCode(type:str):
        if type == "Surgery":
            return 1
        elif type == "UserHasAccess":
            return 2
        elif type == "Injury":
            return 3
        elif type == "Incident":
            return 4
        elif type == "Drug":
            return 5
        elif type == "Appointment":
            return 6
        elif type == "Allergy":
            return 7
        else:
            return None
        