import sys
class BookEdition:
	def __init__(self, name, author, edition, ISBN, booktype, rating, language="English"):
		self.name = name.lower()
		self.author = author.lower()
		self.edition = edition
		self.ISBN = ISBN
		self.booktype = booktype.lower()
		self.rating = rating
		self.language = language

	def get_name(self):
		return self.name

	def get_author(self):
		return self.author

	def get_edition(self):
		return self.edition

	def get_ISBN(self):
		return self.ISBN

	def get_booktype(self):
		return self.booktype

	def get_language(self):
		return self.language

	def get_rating(self):
		return self.rating

	def get_relavance(self):
		# Introducing a slight bias assuming the user prefers books
		# in English. 
		r = 0
		if(self.language == "English"):
			r+=1
		return r + self.rating

	def __gt__(self, other):

		return self.get_relavance() < other.get_relavance()

	def __str__(self):
		s = "=================================="+"\n"\
			"Book name: "+self.get_name()+"\n"\
			"Author   : "+self.get_author()+"\n"\
			"Edition  : "+self.get_edition()+"\n"\
			"ISBN     : "+self.get_ISBN()+"\n"\
			"Booktype : "+self.get_booktype()+"\n"\
			"Rating   : "+str(self.get_rating())+"\n"\
			"language : "+self.get_language()+"\n"
		return s

class Book:
	def __init__(self, name, author):
		self.name = name
		self.author = author

	def get_name(self):
		return self.name

	def get_author(self):
		return self.author


#Adding Harry Potter and the Half-Blood Prince
hbpArray = []
hbpArray.append(BookEdition("Harry Potter and the Half-Blood Prince",
							"J.K Rowling",
							"01",
							"9781408855706",
							"Paperback",
							4.5,
							"English"))

hbpArray.append(BookEdition("Harry Potter and the Half-Blood Prince",
							"J.K Rowling",
							"01",
							"1408855941",
							"Hardcover",
							4,
							"English"))

hbpArray.append(BookEdition("Harri Potter i napivkrovnyi prynts",
							"J.K Rowling",
							"01",
							"9667047296",
							"Hardcover",
							5,
							"Ukrainian"))


hbpArray.append(BookEdition("Harry Potter and the Half-blood Prince",
							"J.K Rowling",
							"01",
							"9654822318",
							"Paperback",
							4,
							"Hebrew"))

poaArray = []
poaArray.append(BookEdition("Harry Potter and the Prisoner of Azkaban",
							"J.K Rowling",
							"01",
							"1408855674",
							"Paperback",
							4,
							"English"))

poaArray.append(BookEdition("Harry Potter e il prigioniero di Azkaban",
							"J.K Rowling",
							"01",
							"886715267X",
							"Paperback",
							4,
							"Italian"))


bookLibrary = {}

hbpbook = Book("Harry Potter and the Half-Blood Prince", "J.K Rowling")
bookLibrary[hbpbook] = hbpArray
poabook = Book("Harry Potter and the Prisoner of Azkaban", "J.K Rowling")
bookLibrary[poabook] = poaArray

try:
	search_term = sys.argv[1]
	search_term = search_term.lower() #lower case

	for b in bookLibrary:
		#b for book
		bucket = []

		for be in bookLibrary[b]:
			# print(be.get_name()+","+be.get_author()+","+be.get_edition()+","+str(be.get_ISBN())+","+be.get_booktype()+","+str(be.get_rating())+","+be.get_language())
			#be for bookedition
			if search_term in be.get_name():
				bucket.append(be)
			if search_term in be.get_author():
				bucket.append(be)
			if search_term in be.get_ISBN():
				bucket.append(be)

		#If there are relavant editions
		if(len(bucket) != 0):
			bucket.sort()
			print(bucket[0])

except:
	print('Error: Please provide your search term as argument.\n - python BookSearch.py \"<SEARCH_TERM>\"')