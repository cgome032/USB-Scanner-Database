"""
Material class that will be used to keep track of material information taken from server
"""
class material:
    """
        Material class used for taking
    """
    def __init__(self, dictionary):
        """
        :param dictionary: Materials dictionary that is passed through and all the attributes are placed in the material
        instance variables
        """

        self.PlateID = dictionary['PlateID']
        self.MaterialID = dictionary['MaterialID']
        self.ParentID = dictionary['ParentID']
        self.StockNumber = dictionary['StockNumber']
        self.Description = dictionary['Description']
        self.Location = dictionary['Location']
        self.PlateType = dictionary['PlateType']
        self.PlateFileType = dictionary['PlateFileType']
        self.PlatePath = dictionary['PlatePath']
        self.PlateLength = dictionary['PlateLength']
        self.PlateWidth = dictionary['PlateWidth']
        self.PlateArea = dictionary['PlateArea']
        self.PlateUnits = dictionary['PlateUnits']
        self.Rotation = dictionary['Rotation']
        self.Weight = dictionary['Weight']
        self.CreateDate = dictionary['CreateDate']
        self.ReorderLimit = dictionary['ReorderLimit']
        self.ReorderQty = dictionary['ReorderQty']
        self.Supplier = dictionary['Supplier']
        self.HeatNumber = dictionary['HeatNumber']
        self.UnitPrice = dictionary['UnitPrice']
        self.MaterialCost = dictionary['MaterialCost']
        self.Misc1 = dictionary['Misc1']
        self.Misc2 = dictionary['Misc2']
        self.Misc3 = dictionary['Misc3']
        self.CreatedByJob = dictionary['CreatedByJob']
        self.guid_no = dictionary['guid_no']
        self.MaterialDescription = dictionary['MaterialDescription']
        self.ERPPlateNumber = dictionary['ERPPlateNumber']
        self.RootID = dictionary['RootID']

    def __str__(self):
        return str('Your material is: ' + self.Description)