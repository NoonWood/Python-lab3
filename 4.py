class StringFormatter:
	def delNLines(self, string, n):
		wordslist = string.split(' ')
		for i in wordslist:
			if len(i) < n:
				wordslist.remove(i)
		return ' '.join(wordslist)
		
	def replaceNumbers(self, string):
		tempstr = string.translate(str.maketrans('0123456789', '**********'))
		return tempstr

	#vers 1
	def addSpaces(self, string):
		tempstr = ''
		for i in string:
			if not i == ' ':
				tempstr += i + ' '
		return tempstr
	#vers 2
	def addSpaces2(self, string):
		return ' '.join(list(string))
		
	def sortByLenght(self, string):
		def SBL(str):
			return len(str)
		templst = string.split(' ')
		templst.sort(key=SBL)
		return ' '.join(templst)

	def lexOrder(self, string):
		lexlist = string.split(' ')
		leslist = sorted(lexlist, key=lambda x:(str.lower(x),x))
		return ' '.join(lexlist)
			
SFor = StringFormatter()

print(SFor.delNLines('123 123456 1234 1234567 12345', 3))
print(SFor.replaceNumbers('Я тебе сказал на 7 30 прийти'))
print(SFor.addSpaces('Я не заикаюсь!'))
print(SFor.addSpaces2('Я не заикаюсь!'))
print(SFor.sortByLenght('Сортировка слов по размеру сказал Йода'))
print(SFor.lexOrder('Сортировка слов по лексическому, что бы это не значило, значению'))
