class comparisonTypeCodes:

    @staticmethod
    def getComparisons():
        comparisons = []
        comparisons.append("equals")
        comparisons.append("notEqual")
        comparisons.append("greaterThan")
        comparisons.append("lowerThan")
        return comparisons

    @staticmethod
    def getType(typeCode:int):
        comparisons = comparisonTypeCodes.getComparisons()
        if(typeCode >= 0 and len(comparisons) > typeCode):
            return comparisons[typeCode]
        else:
            return None
        
    @staticmethod
    def getCode(typeStr:str):
        comparisons = comparisonTypeCodes.getComparisons()
        for i in range(len(comparisons)):
            if comparisons[i] == typeStr:
                return i 
        return None