from SmartContractor import SmartContract
from clauseator import clause
from data.dataFormats import medicalEntry


class smartContractListeners:
    surgeries : list[clause]
    userAccess : list[clause]
    injury : list[clause]
    incident : list[clause]
    drug : list[clause]
    appointment : list[clause]
    allergy : list[clause]

    def __init__(self):
        self.surgeries = []
        self.userAccess = []
        self.injury = []
        self.incident = []
        self.drug = []
        self.appointment = []
        self.allergy = []

    def addToCorrespondingList(self, clause: clause):
        if clause.entryType == 1:
            self.surgeries.append(clause)
        elif clause.entryType == 2:
            self.userAccess.append(clause)
        elif clause.entryType == 3:
            self.injury.append(clause)
        elif clause.entryType == 4:
            self.incident.append(clause)
        elif clause.entryType == 5:
            self.drug.append(clause)
        elif clause.entryType == 6:
            self.appointment.append(clause)
        elif clause.entryType == 7:
            self.allergy.append(clause)

    def addSmartContract(self, contract:SmartContract):
        clauses = contract.getClauses()
        for i in range(len(clauses)):
            self.addToCorrespondingList(clauses[i])

    def notifyListeners(self, dataTypeCode:int, event:medicalEntry):
        if dataTypeCode == 1:
            self.notify(self.surgeries, event)
        elif dataTypeCode == 2:
            self.notify(self.userAccess, event)
        elif dataTypeCode == 3:
            self.notify(self.injury, event)
        elif dataTypeCode == 4:
            self.notify(self.incident, event)
        elif dataTypeCode == 5:
            self.notify(self.drug, event)
        elif dataTypeCode == 6:
            self.notify(self.appointment, event)
        elif dataTypeCode == 7:
            self.notify(self.allergy, event)

    @staticmethod
    def carryComparison(comparison:int, valToCompare, incomingVal):
        if comparison == 0:
            return valToCompare == incomingVal
        elif comparison == 1:
            return valToCompare != incomingVal
        elif comparison == 2:
            return valToCompare < incomingVal
        elif comparison == 3:
            return valToCompare > incomingVal
        pass

    def notify(self, list:list[clause], event : medicalEntry):
        clausesToBeErased = []
        for clause in list:
            try:
                attribute = getattr(event, clause.field)
                if smartContractListeners.carryComparison(clause.comparison, attribute, clause.goalVal):
                    clause.setConditionToMet()
                    clausesToBeErased.append(clause)
                    smartContract = clause.getSmartContract()
                    if(smartContract.allConditionsAreMet()):
                        smartContract.run()
            except AttributeError:
                print("Err: Field not found. There is an error in one of the clauses.")
                pass
        for clause in clausesToBeErased:
            list.remove(clause)