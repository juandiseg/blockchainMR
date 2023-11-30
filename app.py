from SmartContractor import SmartContract
from blockchainExplorer import blockchainExplorer, refinedSearch
from Block import Block
from clauseator import clause
from data.comparisonTypeCodes import comparisonTypeCodes
from data.dataFormats import *
from data.dataTypeCodes import dataTypeCodes
from flask import Flask, request
import json

import jsonpickle
from util.smartContractGenerator import smartContractGenerator

app = Flask(__name__)
blockExplorer = blockchainExplorer()
blockExplorer.addSmartContract(smartContractGenerator.generate())

@app.route('/data/<userID>', methods=['GET'])
def getUserInfo(userID):
    searchDetails = refinedSearch(**request.get_json(silent=False))
    transferable = []
    for block in blockExplorer.searchHistory(int(userID), searchDetails):
        transferable.append(transferableJSON(block))      
    return jsonpickle.encode(transferable, unpicklable=False)

@app.route('/data/appointment/<doctorID>', methods=['GET'])
def getAppointmentsForDoctors(doctorID):
    transferable = []
    for block in blockExplorer.searchAppointmentsDoctor(int(doctorID)):
        transferable.append(transferableJSON(block)) 
    return jsonpickle.encode(transferable, unpicklable=False)

@app.route('/data/access/<doctorID>', methods=['GET'])
def getAccessGrantsForDoctor(doctorID):
    transferable = []
    for block in blockExplorer.searchAccessGrantsForDoctor(int(doctorID)):
        transferable.append(transferableJSON(block)) 
    return jsonpickle.encode(transferable, unpicklable=False)

@app.route('/data/surgery', methods=['POST'])
def addSurgery():
    data = surgery(**request.get_json(silent=False))
    blockExplorer.addSurgery(data)
    return "Successfully added!"

@app.route('/data/userAccess', methods=['POST'])
def addUserAccess():
    data = userHasAccess(**request.get_json(silent=False))
    blockExplorer.addUserHasAccess(data)
    return "Successfully added!"

@app.route('/data/injury', methods=['POST'])
def addInjury():
    data = injury(**request.get_json(silent=False))
    blockExplorer.addInjury(data)
    return "Successfully added!"

@app.route('/data/incident', methods=['POST'])
def addIncident():
    data = incident(**request.get_json(silent=False))
    blockExplorer.addIncident(data)
    return "Successfully added!"

@app.route('/data/drug', methods=['POST'])
def addDrug():
    data = drug(**request.get_json(silent=False))
    blockExplorer.addDrug(data)
    return "Successfully added!"

@app.route('/data/appointment', methods=['POST'])
def addAppointment():
    data = appointment(**request.get_json(silent=False))
    blockExplorer.addAppointment(data)
    return "Successfully added!"

@app.route('/data/allergy', methods=['POST'])
def addAllergy():
    data = allergy(**request.get_json(silent=False))
    blockExplorer.addAllergy(data)
    return "Successfully added!"

@app.route("/data/populate", methods=['GET'])
def populateBlockchain():
    blockExplorer.populateBlockchain()
    return "DONE"

class transferableJSON():
    def __init__(self, block:Block):
        self.type = dataTypeCodes.getType(block.dataType)
        self.data = block.data