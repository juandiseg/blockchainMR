from Blockchain import Blockchain
from data.dataFormats import *
from data.dataTypeCodes import dataTypeCodes

class refinedSearch:  
    def __init__(self, surgery:bool=True,userHasAccess:bool=True,injury:bool=True,incident:bool=True,drug:bool=True, appointment:bool=True,allergy:bool=True):
        self.surgery = surgery
        self.userHasAccess = userHasAccess
        self.injury = injury
        self.incident = incident
        self.drug = drug
        self.appointment = appointment
        self.allergy = allergy

    def allTrue(self):
        return self.surgery and self.userHasAccess and self.injury and self.incident and self.drug and self.appointment and self.allergy

class blockchainExplorer:
    def __init__(self):
        self.DATA_CODES = dataTypeCodes()
        self.blockchain = Blockchain()

    def populateBlockchain(self):
        userID = 100200310
        self.blockchain.addBlock(userID, self.DATA_CODES.surgery, surgery(userID, 1, [1,2,3], "TEST NAME SURGERY", "TEST DESCRIPTION SURGERY", "29/10/2023"))
        self.blockchain.addBlock(userID, self.DATA_CODES.userHasAccess, userHasAccess(userID,12, "29/10/2023"))
        self.blockchain.addBlock(userID, self.DATA_CODES.injury, injury(userID, [1,2,3], "TEST NAME INJURY", "TEST DESCRIPTION INJURY", "29/10/2023", "TEST INJURY NOTES"))
        self.blockchain.addBlock(userID, self.DATA_CODES.incident, incident(userID, [1,2,3], "TEST NAME INCIDENT", "TEST DESCRIPTION INCIDENT", "30/10/2023", "TEST INCIDENT NOTES"))
        self.blockchain.addBlock(userID, self.DATA_CODES.drug, drug(userID, 12, "TEST NAME DRUG", "30/10/2023", "05/11/2023", "TEST DRUG REASON", "TEST DRUG NOTES"))
        self.blockchain.addBlock(userID, self.DATA_CODES.appointment, appointment(userID, 4, 12, "TEST APPOINTMENT REASON", "06/11/2023", "TEST APPOINTMENT TIME"))
        self.blockchain.addBlock(userID, self.DATA_CODES.allergy, allergy(userID, "TEST NAME ALLERGY", "06/11/2023", "TEST ALLERGY DESCRIPTION"))

    def addSurgery(self, data:surgery):
        self.blockchain.addBlock(data.userID, self.DATA_CODES.surgery, data)

    def addUserHasAccess(self, data:userHasAccess):
        self.blockchain.addBlock(data.userID, self.DATA_CODES.userHasAccess, data)

    def addInjury(self, data:injury):
        self.blockchain.addBlock(data.userID, self.DATA_CODES.injury, data)

    def addIncident(self, data:incident):
        self.blockchain.addBlock(data.userID, self.DATA_CODES.incident, data)

    def addDrug(self, data:drug):
        self.blockchain.addBlock(data.userID, self.DATA_CODES.drug, data)
    
    def addAppointment(self, data:appointment):
        self.blockchain.addBlock(data.userID, self.DATA_CODES.appointment, data)
    
    def addAllergy(self, data:allergy):
        self.blockchain.addBlock(data.userID, self.DATA_CODES.allergy, data)

    def searchUserID(self, userID:int):
        listData = []
        for block in self.blockchain.chain:
            if block.userID == userID:
                listData.append(block)    
        return listData
    
    def searchHistory(self, userID:int, details:refinedSearch):
        blocks = self.searchUserID(userID)
        refinedEntries = []
        if details.allTrue():
            return blocks 
        
        for block in blocks:
            if details.surgery and block.dataType == self.DATA_CODES.surgery:
                refinedEntries.append(block)
            if details.userHasAccess and block.dataType == self.DATA_CODES.userHasAccess:
                refinedEntries.append(block)
            if details.injury and block.dataType == self.DATA_CODES.injury:
                refinedEntries.append(block)
            if details.incident and block.dataType == self.DATA_CODES.incident:
                refinedEntries.append(block)
            if details.drug and block.dataType == self.DATA_CODES.drug:
                refinedEntries.append(block)
            if details.appointment and block.dataType == self.DATA_CODES.appointment:
                refinedEntries.append(block)
            if details.allergy and block.dataType == self.DATA_CODES.allergy:
                refinedEntries.append(block)
        return refinedEntries
    