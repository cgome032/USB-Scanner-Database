import barcode


class MatBarcode:

    def __init__(self,material_id):
        self.new_barcode = barcode.get('code128', str(material_id))
        #newEan.get_fullcode()
        self.filename = self.new_barcode.save('code 128')
        print(self.new_barcode)