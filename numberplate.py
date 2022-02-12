def similar_license_plates(plate1, plate2):
    tr = str.maketrans('OQITZSB', '0011258', ' ')
    return plate1.translate(tr) == plate2.translate(tr)

def solution(plate1,plate2):
    from_char = "OQITZSB"
    to_char = "0011258"
    p1 = plate1.replace(" ", "")
    p2 = plate2.replace(" ", "")
    
    for i in from_char:
        if i in plate1:
            p1 = p1.replace(i, to_char[from_char.index(i)])
        if i in plate2:
            p2 = p2.replace(i, to_char[from_char.index(i)])
    return p1 == p2


print(similar_license_plates('A A  A', 'AA A')) # True
print(similar_license_plates('0XB', 'OBX'))

print(solution('A A  A', 'AA A'))
print(solution('0XB', 'OBX'))