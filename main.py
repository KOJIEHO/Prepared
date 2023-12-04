###### Сохранение фото из интернета ######
Photo = requests.get('Адресс страницы')
Photo_option = open('Название фото', 'wb')
Photo_option.write(Photo.content)
Photo_option.close()


###### Открытие и запись данных в csv файл ######
# Открытие и запись названий столбцов в csv файл #
with open("Data1.csv", "a", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        ["Столбец №1", "Столбец №2", "MСтолбец №3", ..., "Столбец №"]
    )
# Открытие и запись данных в каждый столбец в csv файл #
with open("Data1.csv", "a", encoding='utf-16', newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        [Данные для столбца №1, Данные для столбца №2, Данные для столбца №3, ..., Данные для столбца №N]
    )
    
   
###### Создние БД, запись данных в БД, выгрузка данных из БД ######
base = sqlite3.connect('Название БД.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS Название Таблицы(Название столбца №1, Название столбца №2, Название столбца №3, ..., Название столбца №N")')
base.commit()

cur.execute('INSERT INTO Название Таблицы VALUES(?, ?, ..., N)', (Данные для столбца №1, Данные для столбца №2, Данные для столбца №3, ..., Данные для столбца №N))
base.commit()

info = cur.execute('SELECT Название Столбца FROM Название Таблицы').fetchall()

cur.execute('DELETE FROM Название Таблицы')
base.commit()
