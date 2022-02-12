def similar_license_plates(plate1, plate2):
    tr = str.maketrans('OQITZSB', '0011258', ' ')
    print(plate1.translate(tr))
    print(plate2.translate(tr))
    return plate1.translate(tr) == plate2.translate(tr)

print(similar_license_plates('A A  A', 'AA A')) # True
print(similar_license_plates('0XB', 'OBX'))