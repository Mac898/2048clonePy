
class Array2048:
    def __init__(self):
        print("Array 2048 Loaded")
    
    rowTable = {
        "1": [0,0,0,0],
        "2": [0,0,0,0],
        "3": [0,0,0,0],
        "4": [0,0,0,0]
    }
    
    def UpdateTable(self, col, row, value):
        currentcol = self.rowTable[str(col)]
        currentcol[row] = value
        self.rowTable[col] = currentcol[row]
        print(self.rowTable)
    def GetTable(self):
        return self.rowTable
