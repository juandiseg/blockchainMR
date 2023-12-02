from abc import abstractmethod
from clauseator import clause

class SmartContract():
    clauses : list[clause]

    def __init__(self):
        self.clauses = []

    def addRunnable(self, var):
        self.runnable = var

    def addClause(self, newClause:clause):
        self.clauses.append(newClause)

    def getClauses(self) -> list[clause]:
        return self.clauses

    def allConditionsAreMet(self):
        for clause in self.clauses:
            if(not clause.isConditionMet()):
                return False
        return True
    
    def run(self):
        self.runnable()