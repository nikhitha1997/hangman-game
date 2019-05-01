from models import WordList #from model importing the wordlist table
import random               #importing random module

def load_data():     #load data function
	all_words = WordList.select()
	
	x = random.randint(1, len(all_words)) #selecting the random word from wordlist
	print(x)

	data_list = [] #empty list 

	data = WordList.select().where(WordList.id==x) #data consist of word,hint,id
	print(data)
	for i in data:
		print(i.word, i.hint)
		data_list.append([i.word, i.hint])#appending the word and hint to the data list
		
	return data_list

def add_data(word, hint):#add_data function
	WordList.create(word=word, hint=hint)


if __name__ == "__main__":
	load_data()
