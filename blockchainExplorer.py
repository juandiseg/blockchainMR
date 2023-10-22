from Blockchain import Blockchain
from data.dataFormats import *
from data.dataTypeCodes import dataTypeCodes

class blockchainExplorer:
    def __init__(self):
        self.DATA_CODES = dataTypeCodes()
        self.blockchain = Blockchain()

    def addSurgery(self, userID:int, hospitalID:int, surgeonTeamIDs, surgeryName:str, description:str, notes:str, date:str):
        self.blockchain.addBlock(userID, self.DATA_CODES.surgery, surgery(userID, hospitalID, surgeonTeamIDs, surgeryName, description, notes, date))

    def addUserHasAccess(self, userID:int, userGrantedAccessID:int, date:str):
        self.blockchain.addBlock(userID, self.DATA_CODES.userHasAccess, userHasAccess(userID, userGrantedAccessID, date))

    def addInjury(self, userID:int, injuryID:int, medicalTeamIDs, injuryTitle:str, description:str, date:str, notes:str=""):
        self.blockchain.addBlock(userID, self.DATA_CODES.injury, injury(userID, injuryID, medicalTeamIDs, injuryTitle, description, date, notes))

    def addIncident(self, userID:int, medicalTeamIDs, incidentTitle:str, description:str, date:str, notes:str=""):
        self.blockchain.addBlock(userID, self.DATA_CODES.incident, incident(userID, medicalTeamIDs, incidentTitle, description, date, notes))

    def addDrug(self, userID:int, doctorID:int, drugTitle:str, startDate:str, endDate:str, reason:str, notes:str=""):
        self.blockchain.addBlock(userID, self.DATA_CODES.drug, drug(userID, doctorID, drugTitle, startDate, endDate, reason, notes))
    
    def addAppointment(self, userID:int, doctorID:int, medicalCenter:int, reason:str, date:str, time:str):
        self.blockchain.addBlock(userID, self.DATA_CODES.appointment, appointment(userID, doctorID, medicalCenter, reason, date, time))
    
    def addAllergy(self, userID:int, allergyTitle:str, dateOfDiscovery:str, treatment:str, notes:str=""):
        self.blockchain.addBlock(userID, self.DATA_CODES.allergy, allergy(userID, allergyTitle, dateOfDiscovery, treatment, notes))

    def searchUserID(self, userID:int):
        listData = []
        for block in self.blockchain.chain:
            if block.userID == userID:
                listData.append(block)                
        return listData
    
    def searchHistory(self, userID:int,surgery:bool=True,userHasAccess:bool=True,injury:bool=True,incident:bool=True,drug:bool=True, appointment:bool=True,allergy:bool=True):
        blocks = self.searchUserID(userID)
        refinedEntries = []
        if surgery and userHasAccess and injury and incident and drug and appointment and allergy:
            for block in blocks:
                refinedEntries.append(block.data)
            return refinedEntries 
        for block in blocks:
            if surgery == True and block.dataType == self.DATA_CODES.surgery:
                refinedEntries.append(block.data)
            if userHasAccess and block.dataType == self.DATA_CODES.userHasAccess:
                refinedEntries.append(block.data)
            if injury and block.dataType == self.DATA_CODES.injury:
                refinedEntries.append(block.data)
            if incident and block.dataType == self.DATA_CODES.incident:
                refinedEntries.append(block.data)
            if drug and block.dataType == self.DATA_CODES.drug:
                refinedEntries.append(block.data)
            if appointment and block.dataType == self.DATA_CODES.appointment:
                refinedEntries.append(block.data)
            if allergy and block.dataType == self.DATA_CODES.allergy:
                refinedEntries.append(block.data)
        return refinedEntries