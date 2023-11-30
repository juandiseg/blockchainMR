from hashlib import sha256

class Block:
    
    def __init__(self, blockID:int, userID:int, dataType:int, data, timestamp:str, doctorID:int=-1, previousHash:str="0", nonce:int=0):
        self.blockID = blockID
        self.userID = userID
        self.doctorID = doctorID
        self.timestamp = timestamp
        self.dataType = dataType
        self.data = data
        self.previousHash = previousHash
        self.nonce = nonce
        self.hash = self.calculateHash()
    
    def print(self):
        print(f"\tblockID : {self.blockID}")
        print(f"\tuserID : {self.userID}")
        print(f"\tdoctorID : {self.doctorID}")
        print(f"\ttimestamp : {self.timestamp}")
        print(f"\tdata_type : {self.dataType}")
        print(f"\tpreviousHASH {self.previousHash}")
        print(f"\thash : {self.hash}")

    def mineBlock(self, difficulty:int=2):
        self.nonce = 0
        self.hash = "aaaaaaaaaaaaaaaaaaaaa"
        while self.hash[0:difficulty] != "0" * difficulty:
            self.nonce+=1
            self.hash = self.calculateHash()
        return self.hash

    def calculateHash(self):
        self.hash = sha256((str(self.blockID) + str(self.userID) + str(self.doctorID) + str(self.dataType) + str(self.timestamp) + str(self.previousHash) + str(self.nonce)).encode('utf-8')).hexdigest()
        return self.hash