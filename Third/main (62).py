def isYearLeap(year):
	if year % 4 != 0:
	    print("El anio ", year, " es bisiesto.")
	    return True
	if year % 100 !=0:
	    print("El anio ", year, " no es bisiesto.")
	    return False
	if year %400 !=0:
	    print("El anio ", year, " es bisiesto.")
	    return True
testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]
for i in range(len(testdata)):
	yr = testdata[i]
	print(yr,"-> ",end="")
	result = isYearLeap(yr)
	if result == testresults[i]:
		print("OK")
	else:
		print("Error")