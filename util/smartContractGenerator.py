import time

from SmartContractor import SmartContract
from clauseator import clause
from data.comparisonTypeCodes import comparisonTypeCodes
from data.dataTypeCodes import dataTypeCodes

def printOla():
    print("Smart Contract Starting to Execute:")
    # Implementation would be here
    time.sleep(0.5)
    print(". ", end="", flush=True)
    time.sleep(0.5)
    print(". ", end="", flush=True)
    time.sleep(0.5)
    print(". ", flush=True)
    time.sleep(0.5)
    print("Smart Contract Fully EXECUTED!")

class smartContractGenerator:
    @staticmethod
    def generate() -> SmartContract:
        sc = SmartContract()
        sc.addClause(clause(sc, dataTypeCodes.getCode("Surgery"), comparisonTypeCodes.getCode("equals"), "userID", 1))
        ola = printOla
        sc.addRunnable(ola)
        return sc