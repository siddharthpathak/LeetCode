#Converts Roman input string to int. 

def romanToInt(self, s):
	"""
	:type s: str
	:rtype: int
	"""
	romanDigits = {}
	romanDigits["I"] = 1
	romanDigits["V"] = 5
	romanDigits["X"] = 10
	romanDigits["L"] = 50
	romanDigits["C"] = 100
	romanDigits["D"] = 500
	romanDigits["M"] = 1000
	result = 0
	for n in range(0,len(s)-1):
		if romanDigits[s[n]] < romanDigits[s[n+1]]:
			temp = -romanDigits[s[n]]
		else:
			temp = romanDigits[s[n]]
		result +=temp
	
	return result+romanDigits[s[-1]]
