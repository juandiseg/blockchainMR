class clause:
    entryType:int
    comparison:int
    field:str

    def __init__(self, smartContract, entryType:int, comparison:int, field:str, goalVal):
        self.smartContract = smartContract
        self.conditionMet = False
        self.comparison = comparison
        self.entryType = entryType
        self.field = field
        self.goalVal = goalVal

    def isConditionMet(self):
        return self.conditionMet
    
    def getSmartContract(self):
        return self.smartContract

    def setConditionToMet(self):
        self.conditionMet = True
