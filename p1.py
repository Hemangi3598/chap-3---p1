# wapp to read radius from the user
# and find area and circum

radius = float(input("enter radius "))
if radius <=0 :
	print("invalid radius")
else :
	pi=3.1459
	area = pi * radius **2
	circum = 2 * pi * radius
	print(" area = ", round(area , 2))
	print( " circum = ", round(circum, 2))