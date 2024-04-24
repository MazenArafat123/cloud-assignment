import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from collections import Counter
nltk.download('punkt')

nltk.download('stopwords')
import string
#read file
file_path ='random_paragraphs.txt'
def read_file(file_path):
    with open(file_path, "r") as file:
        unfilterd_data = file.read()
        return unfilterd_data
    
def remove_punctuanions_and_stop_words(data) :  
    tokenize_words = word_tokenize(data)  
    custom_stop_words = {"'s", "''", "``"}
    stop_words =set(stopwords.words('english'))
    punctuanions =set(string.punctuation)
    filterd_words = [word for word in tokenize_words if word.lower() not in stop_words and word not in punctuanions]
    filterd_words =[word for word in filterd_words if word.lower() not in custom_stop_words ]
    filterd_data = ' '.join(filterd_words)
    return filterd_data
data =read_file(file_path)
filter_data =remove_punctuanions_and_stop_words(data)
filter_data_path ="C:\\Users\\Nour\\OneDrive\\Desktop\\filtered_data.txt"
with open(filter_data_path ,'w') as file :
    file.write(filter_data)
# print (filter_data)
   
filter_data =filter_data.lower()

def count_word(text):
    
    word_counter = Counter(text)
    return word_counter

def count_frequency(text):
    words = text.split()  
    word_counts = count_word(words)
    return word_counts

word_frequency = count_frequency(filter_data)

big_frequency_first = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
for word, count in big_frequency_first.items():
     print(f'{word}: {count}')
print('the most repeated 100 words')

the_big_ones = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:100])
print('the most 100 words are :')
for word, count in the_big_ones.items():
    print(f'{word}: {count}')