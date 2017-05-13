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
	
	def addSpaces(self, string):
		tempstr = ''
		for i in string:
			if not i == ' ':
				tempstr += i + ' '
		return tempstr
		
	def sortByLenght(self, string):
		def SBL(str):
			return len(str)
		templst = string.split(' ')
		templst.sort(key=SBL)
		return ' '.join(templst)

		''' хз что за функция сортировки слов в лексикографическом порядке
	def lexOrder(self, string):
		lexlist = string.split(' ')
		leslist = sorted(lexlist, key=lambda x:(str.lower(x),x))
		return ' '.join(lexlist)
		'''

SFor = StringFormatter()
print(SFor.delNLines('123 123456 1234 1234567 12345', 5))
print(SFor.replaceNumbers('Я тебе сказал на 5 30 прийти'))
print(SFor.addSpaces('Я не заикаюсь!'))
print(SFor.sortByLenght('сортировка слов по размеру'),'(с)Йода')
#print(SFor.lexOrder('Мама мыла раму тридцать восемь раз раза разов'))
