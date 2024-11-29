from collections import Counter # для подсчета частоты элементов
import docx # чтобы работать в docx
import re 
import pandas as pd #бб,чтобы работать с таблицами и анализа данных
import matplotlib.pyplot as plt
file_path = 'lion.docx'
doc = docx.Document(file_path)
text = []
for paragraph in doc.paragraphs:
 text.append(paragraph.text) # извлечение текста в список
full_text = ' '.join(text)
words = re.findall(r'\b\w+\b', full_text.lower()) #/- граница слова,\w+ последовательность букв
word_count = Counter(words)
total_words = sum(word_count.values()) #общее кол-во слов
df_words = pd.DataFrame(word_count.items(), columns=['Слово', 'Частота'])
df_words['Процент'] = (df_words['Частота'] / total_words) * 100 # + столбец и считаем встречаемость слов
print(df_words)
output_file_words = 'word_frequency.csv' # сохроняем в csv
df_words.to_csv(output_file_words, index=False, encoding='utf-8')
print(f'Результаты частоты слов сохранены в файл: {output_file_words}')
letters = re.findall(r'[а-яА-ЯёЁ]', full_text.lower()) # остаются русские буквы,также извлекаем от  а-я A-Я и еЁ
letter_count = Counter(letters)
df_letters = pd.DataFrame(letter_count.items(), columns=['Буква', 'Частота']) #создаю DataFrame
total_letters = sum(letter_count.values()) #кол-во
df_letters['Процент'] = (df_letters['Частота'] / total_letters) * 100 # + столбец и считаем встречаемость слов
plt.bar(df_letters['Буква'], df_letters['Частота'], color='orange') #столбчатая диаграмма                                        
plt.title('Частота встречаемости букв') #заголовок
plt.xlabel('Буквы')                         
plt.ylabel('Частота')                        
plt.xticks(rotation=45) # угол поворта 
plt.grid(axis='y') # упрощение оценки гистограммы
plt.tight_layout() # избегаем наложения элементов
plt.show() # на экран