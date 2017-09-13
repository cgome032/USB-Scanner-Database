import barcode

ean = barcode.get('code128', '13456789')
#newEan.get_fullcode()

filename = ean.save('code 128')


print(ean)