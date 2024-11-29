import pandas as pd
import matplotlib.pyplot as plt
file_path = 'titanic.parquet'  
df = pd.read_parquet(file_path)#грузим в таблицу
print(df.head())
csv_output_path = 'titanic.csv' #переводим  в csv
df.to_csv(csv_output_path, index=False, encoding='utf-8')  
print(f'Файл сохранен как: {csv_output_path}') #выводим              
csv_file_path = 'titanic.csv' 
df = pd.read_csv(csv_file_path)
survival_counts = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0) # кол-во,делаем так,чтобы показывало жив ли чел
survival_percentage = survival_counts.div(survival_counts.sum(axis=1), axis=0) * 100 # считаем проц для классов
survival_percentage.plot(kind='bar', stacked=True, color=['lightblue,' 'lightpink'],  figsize=(10, 6)) # blue-не выжил,pink-выжил
plt.title('Выживаемость пассажиров Титаника') # заголовк гистограммы
plt.xlabel('Класс билета') #ник столбцов диограммы
plt.xticks(rotation=0)
plt.legend(['Не выжили', 'Выжили'])
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%')) # ось в процах,plt.gca() ось для графика,задаю формат с помощью lamda
plt.ylim(0, 100) # предел от 0 до 100
plt.tight_layout()
plt.show()