import peewee as pw    #importing the peewee

db = pw.SqliteDatabase('hangman.db')  #creating the hangman database

class WordList(pw.Model): #wordlist table    
	word = pw.TextField()
	hint = pw.TextField()

	class Meta:
		database = db

db.connect()
db.create_tables([WordList])