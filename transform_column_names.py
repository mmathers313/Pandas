import pandas as pd

# Данная простая функция преобразует заголовки полей DataFrame в змеиный регистр.

def transform_column_names(df):
  df.columns = df.columns.str.lower() # преобразуем заголовки полей df в строковые
  df.columns = df.columns.str.strip() # избавимся он лишних пробелов вначале и в конце текста
  df.columns = df.columns.str.replace(" ", "_") # пробелы внутри заголовков заменим на _
  return 
