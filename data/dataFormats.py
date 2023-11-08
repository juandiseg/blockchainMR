class medicalEntry:
    def __init__(self):
        pass
    
class genesisBlock(medicalEntry):
    def __init__(self):
        self.description = "Blockchain's genesis block."

class surgery(medicalEntry):
    def __init__(self, userID:int, hospitalID:int, surgeonTeamIDs, surgeryName:str, description:str, date:str, notes:str=""):
        self.userID = userID
        self.surgeryName = surgeryName
        self.hospitalID = hospitalID
        self.surgeonTeamIDs = surgeonTeamIDs
        self.description = description
        self.date = date
        self.notes = notes

class userHasAccess(medicalEntry):
    def __init__(self, userID:int, userGrantedAccessID:int, date:str):
        self.userID = userID
        self.userGrantedAccessID = userGrantedAccessID
        self.date = date

class injury(medicalEntry):
    def __init__(self, userID:int, medicalTeamIDs, injury:str, description:str, date:str, notes:str=""):
        self.userID = userID
        self.medicalTeamIDs = medicalTeamIDs
        self.injury = injury
        self.description = description
        self.date = date
        self.notes = notes

class incident(medicalEntry):
    def __init__(self, userID:int, medicalTeamIDs, incident:str, description:str, date:str, notes:str=""):
        self.userID = userID
        self.medicalTeamIDs = medicalTeamIDs
        self.incident = incident
        self.description = description
        self.date = date
        self.notes = notes

class drug(medicalEntry):
    def __init__(self, userID:int, doctorID:int, drug:str, startDate:str, endDate:str, reason:str, notes:str=""):
        self.userID = userID
        self.doctorID = doctorID
        self.drug = drug
        self.startDate = startDate
        self.endDate= endDate
        self.reason= reason
        self.notes= notes

class appointment(medicalEntry):
    def __init__(self, userID:int, doctorID:int, medicalCenter:int, reason:str, date:str, time:str):
        self.userID = userID
        self.doctorID = doctorID
        self.medicalCenter = medicalCenter
        self.reason= reason
        self.date = date
        self.time= time

class allergy(medicalEntry):
    def __init__(self, userID:int, allergy:str, dateOfDiscovery:str, treatment:str, notes:str=""):
        self.userID = userID
        self.allergy = allergy
        self.dateOfDiscovery = dateOfDiscovery
        self.treatment = treatment
        self.notes= notes