import pandas as pd

students_grades = {
    'name': ["Иванов Иван", "Петров Петр", "Сидоров Сидор", "Кузнецова Мария", "Смирнова Анна", "Васильев Василий",
             "Алексеева Ольга", "Новиков Никита", "Морозов Михаил", "Федорова Елена"],
    "Математика": [5, 4, 3, 5, 4, 3, 5, 4, 3, 5],
    "Физика": [4, 3, 4, 5, 4, 3, 4, 5, 3, 5],
    "Химия": [3, 4, 5, 5, 4, 3, 4, 3, 4, 5],
    "Биология": [4, 5, 3, 5, 4, 3, 5, 4, 3, 4],
    "История": [5, 3, 4, 5, 4, 3, 5, 4, 4, 5]
}

statistics = {"Предмет": [],
              "Ср. оценка": [],
              "Мед. оценка": [],
              "Стандартное отклонение": [],
              "Q1": [],
              "Q3": [],
              "IQR": [],
              }

df = pd.DataFrame(students_grades)
df.set_index('name', inplace=True)
# Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
print(df.head())
print()

for cat, values in students_grades.items():
    if cat != 'name':
        statistics["Предмет"].append(cat)
        statistics["Ср. оценка"].append(df[cat].mean())
        statistics["Мед. оценка"].append(df[cat].median())
        statistics["Стандартное отклонение"].append(df[cat].std())

        Q1 = df['Математика'].quantile(0.25)
        Q3 = df['Математика'].quantile(0.75)
        IQR = Q3 - Q1

        statistics["Q1"].append(Q1)
        statistics["Q3"].append(Q3)
        statistics["IQR"].append(IQR)

df_stat = pd.DataFrame(statistics)
print(df_stat)

