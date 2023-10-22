from Block import Block
from data.dataFormats import *
from datetime import datetime

class Blockchain:
    def __init__(self, difficulty:int=2):
        genesisB = Block(0, 0, 0, genesisBlock(), "19/10/2023")
        self.chain = [genesisB]
        self.difficulty = difficulty
    
    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]
    
    def addBlock(self, userID:int, dataCode:int, data:jsonConverter):
        blockID = self.getLatestBlock().blockID + 1
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        newBlock = Block(blockID, userID, dataCode, data, timestamp, self.getLatestBlock().hash)
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            prevBlock = self.chain[i-1]
            currBlock = self.chain[i]
            if currBlock.previousHash != prevBlock.hash:
                return False
            if currBlock.mineBlock(self.difficulty) != currBlock.hash:
                return False
        return True

    def print(self):
        print("Blockchain summary: ")
        for i in range(len(self.chain)):
            print("{")
            self.chain[i].print()
            if i == len(self.chain)-1:
                print("}")
            else:
                print("},")
        print(f"Is the blockchain corrupted: {not self.isChainValid()}.")