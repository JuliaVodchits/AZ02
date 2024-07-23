import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)

# Преобразуем столбцы в категориальные данные. Мы можем сделать категории для столбцов "gender" и "department"
# Команда astype преобразует гендер и департамент в категориальный тип, что позволяет работать с этими данными как с категориями.
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

# Чтобы просмотреть уникальные категории, которые есть в датафрейме, напишем и запустим код:
print(df['gender'].cat.categories)
print(df['department'].cat.categories)

# Мы можем также посмотреть числовые коды категорий, прописав:
print(df['gender'].cat.codes)

# Можно добавить новую категорию — например, новый департамент, финансовый отдел. Для этого прописываем место,
# куда хотим добавить новые сведения (department):
df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)
print(df)