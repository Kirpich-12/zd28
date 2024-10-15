
data_s =  open('input.txt', 'r')
data = data_s.read()
x1, y1, x2, y2, xa, ya = data.split()

x1, y1, x2, y2, xa, ya = int(x1), int(y1), int(x2), int(y2), int(xa), int(ya)

if x1 != x2 and y1 == y2: # симетрия по оси x
    if ya > y1:           # точка выше оси симметрии 
        yb =  y1 - (ya - y1)
    else:
        yb = y1 + (y1 -ya)
    ans = (str(xa) + ' ' + str(yb))
else:
    if xa > x1:
        xb = x1 - (xa - x1)
    else:
        xb = x1 + (x1 - xa)
    ans = (str(xb) + ' ' + str(ya))

output_data = open('output.txt', 'w')
output_data.write(ans)
#запись

data_s.close()
output_data.close()
#ОБЯЗАТЕЛЬНО не забывать