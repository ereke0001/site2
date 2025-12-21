from models import User, Lecture, Test
from datetime import datetime

def init_db(db, app):
    """Initialize the database with the Flask app"""
    with app.app_context():
        db.create_all()
        # Create default user if it doesn't exist
        create_default_user(db)
        # Create sample lectures and tests if they don't exist
        create_sample_data(db)

def create_default_user(db):
    """Create the default user if it doesn't exist"""
    default_user = User.query.first()
    
    if not default_user:
        default_user = User(
            name="Пользователь"
        )
        db.session.add(default_user)
        db.session.commit()
        print("Default user created")

def create_sample_data(db):
    """Create sample lectures and tests if they don't exist"""
    # Check if we have any lectures
    if Lecture.query.count() == 0:
        # Create 10 comprehensive lectures
        lectures_data = [
            {
                "title": "1. Введение в Python",
                "content": '''
                <h1>1. Введение в Python</h1>
                <p>Python - это мощный, интерпретируемый язык программирования высокого уровня, известный своей простотой и читаемостью. Он был создан Гвидо ван Россумом и впервые выпущен в 1991 году.</p>
                
                <h2>Основные особенности Python:</h2>
                <ul>
                    <li>Простота синтаксиса и читаемость кода</li>
                    <li>Интерпретируемый язык (не требует компиляции)</li>
                    <li>Поддержка множества парадигм программирования</li>
                    <li>Обширная стандартная библиотека</li>
                    <li>Кроссплатформенность</li>
                </ul>
                
                <h2>Где используется Python:</h2>
                <ul>
                    <li>Веб-разработка (Django, Flask)</li>
                    <li>Научные вычисления (NumPy, SciPy)</li>
                    <li>Анализ данных (Pandas, Matplotlib)</li>
                    <li>Искусственный интеллект и машинное обучение (TensorFlow, PyTorch)</li>
                    <li>Автоматизация задач</li>
                </ul>
                
                <h2>Первая программа на Python:</h2>
                <pre><code>print("Привет, мир!")</code></pre>
                <p>Эта простая строка выводит текст "Привет, мир!" на экран. В Python для вывода информации используется функция <code>print()</code>.</p>
                '''
            },
            {
                "title": "2. Переменные и типы данных",
                "content": '''
                <h1>2. Переменные и типы данных</h1>
                <p>Переменные в Python используются для хранения данных. В отличие от некоторых других языков программирования, в Python не нужно объявлять тип переменной явно.</p>
                
                <h2>Создание переменных:</h2>
                <pre><code>x = 5
name = "Алексей"
is_student = True</code></pre>
                
                <h2>Основные типы данных в Python:</h2>
                <ul>
                    <li><strong>int</strong> - целые числа (5, -3, 100)</li>
                    <li><strong>float</strong> - числа с плавающей точкой (3.14, -2.5)</li>
                    <li><strong>str</strong> - строки ("Привет", 'Мир')</li>
                    <li><strong>bool</strong> - булевы значения (True, False)</li>
                    <li><strong>list</strong> - списки ([1, 2, 3])</li>
                    <li><strong>dict</strong> - словари ({"ключ": "значение"})</li>
                </ul>
                
                <h2>Примеры работы с переменными:</h2>
                <pre><code>age = 25
height = 1.75
name = "Мария"
hobbies = ["чтение", "плавание", "программирование"]
person = {"имя": "Иван", "возраст": 30}

print(f"Меня зовут {name}, мне {age} лет")</code></pre>
                '''
            },
            {
                "title": "3. Операторы и выражения",
                "content": '''
                <h1>3. Операторы и выражения</h1>
                <p>Операторы в Python используются для выполнения операций над переменными и значениями. Выражение - это комбинация значений, переменных, операторов и вызовов функций.</p>
                
                <h2>Арифметические операторы:</h2>
                <ul>
                    <li><strong>+</strong> - сложение</li>
                    <li><strong>-</strong> - вычитание</li>
                    <li><strong>*</strong> - умножение</li>
                    <li><strong>/</strong> - деление</li>
                    <li><strong>//</strong> - целочисленное деление</li>
                    <li><strong>%</strong> - остаток от деления</li>
                    <li><strong>**</strong> - возведение в степень</li>
                </ul>
                
                <h2>Операторы сравнения:</h2>
                <ul>
                    <li><strong>==</strong> - равно</li>
                    <li><strong>!=</strong> - не равно</li>
                    <li><strong><</strong> - меньше</li>
                    <li><strong>></strong> - больше</li>
                    <li><strong><=</strong> - меньше или равно</li>
                    <li><strong>>=</strong> - больше или равно</li>
                </ul>
                
                <h2>Логические операторы:</h2>
                <ul>
                    <li><strong>and</strong> - логическое И</li>
                    <li><strong>or</strong> - логическое ИЛИ</li>
                    <li><strong>not</strong> - логическое НЕ</li>
                </ul>
                
                <h2>Примеры:</h2>
                <pre><code>a = 10
b = 3

print(a + b)  # 13
print(a / b)  # 3.333...
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000

print(a > b and b > 0)  # True
print(a < 5 or b > 2)   # True</code></pre>
                '''
            },
            {
                "title": "4. Условные операторы",
                "content": '''
                <h1>4. Условные операторы</h1>
                <p>Условные операторы позволяют выполнять разные блоки кода в зависимости от выполнения определенных условий.</p>
                
                <h2>Конструкция if:</h2>
                <pre><code>age = 18

if age >= 18:
    print("Вы совершеннолетний")
elif age >= 13:
    print("Вы подросток")
else:
    print("Вы ребенок")</code></pre>
                
                <h2>Вложенные условия:</h2>
                <pre><code>temperature = 25
is_sunny = True

if temperature > 20:
    if is_sunny:
        print("Отличный день для прогулки!")
    else:
        print("Тепло, но облачно")
else:
    print("Слишком холодно для прогулки")</code></pre>
                
                <h2>Тернарный оператор:</h2>
                <pre><code>age = 20
status = "совершеннолетний" if age >= 18 else "несовершеннолетний"
print(status)</code></pre>
                '''
            },
            {
                "title": "5. Циклы",
                "content": '''
                <h1>5. Циклы</h1>
                <p>Циклы позволяют повторять выполнение блока кода несколько раз. В Python есть два основных типа циклов: <code>for</code> и <code>while</code>.</p>
                
                <h2>Цикл for:</h2>
                <pre><code># Перебор элементов списка
fruits = ["яблоко", "банан", "апельсин"]
for fruit in fruits:
    print(fruit)

# Использование range()
for i in range(5):
    print(f"Число: {i}")</code></pre>
                
                <h2>Цикл while:</h2>
                <pre><code>count = 0
while count < 5:
    print(f"Счетчик: {count}")
    count += 1</code></pre>
                
                <h2>Управление циклами:</h2>
                <ul>
                    <li><strong>break</strong> - прерывает выполнение цикла</li>
                    <li><strong>continue</strong> - переходит к следующей итерации</li>
                </ul>
                
                <pre><code>for i in range(10):
    if i == 3:
        continue  # Пропустить 3
    if i == 7:
        break     # Остановиться на 7
    print(i)</code></pre>
                '''
            },
            {
                "title": "6. Функции",
                "content": '''
                <h1>6. Функции</h1>
                <p>Функции - это блоки кода, которые можно многократно вызывать для выполнения определенной задачи. Они помогают организовать код и сделать его более читаемым и переиспользуемым.</p>
                
                <h2>Определение функции:</h2>
                <pre><code>def greet(name):
    """Функция приветствия"""
    return f"Привет, {name}!"

# Вызов функции
message = greet("Анна")
print(message)</code></pre>
                
                <h2>Параметры и аргументы:</h2>
                <pre><code>def calculate_area(length, width=1):
    """Вычисляет площадь прямоугольника"""
    return length * width

# Позиционные аргументы
area1 = calculate_area(5, 3)

# Именованные аргументы
area2 = calculate_area(width=4, length=6)

# Аргументы по умолчанию
area3 = calculate_area(5)  # ширина будет 1</code></pre>
                
                <h2>*args и **kwargs:</h2>
                <pre><code>def print_info(*args, **kwargs):
    print("Позиционные аргументы:", args)
    print("Именованные аргументы:", kwargs)

print_info(1, 2, 3, name="Иван", age=25)</code></pre>
                '''
            },
            {
                "title": "7. Списки и кортежи",
                "content": '''
                <h1>7. Списки и кортежи</h1>
                <p>Списки и кортежи - это упорядоченные коллекции элементов. Списки изменяемы, а кортежи неизменяемы.</p>
                
                <h2>Списки:</h2>
                <pre><code># Создание списка
numbers = [1, 2, 3, 4, 5]
names = ["Анна", "Петр", "Мария"]
mixed = [1, "привет", True, 3.14]

# Доступ к элементам
print(numbers[0])    # Первый элемент
print(names[-1])     # Последний элемент

# Изменение списка
numbers[0] = 10
numbers.append(6)    # Добавить в конец
numbers.insert(2, 15) # Вставить по индексу

# Удаление элементов
numbers.remove(15)   # Удалить по значению
removed = numbers.pop() # Удалить последний и вернуть его</code></pre>
                
                <h2>Срезы (slices):</h2>
                <pre><code>data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(data[2:5])    # [2, 3, 4]
print(data[:3])     # [0, 1, 2]
print(data[7:])     # [7, 8, 9]
print(data[::2])    # [0, 2, 4, 6, 8] - каждый второй
print(data[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - в обратном порядке</code></pre>
                
                <h2>Кортежи:</h2>
                <pre><code># Создание кортежа
colors = ("красный", "зеленый", "синий")
coordinates = (10, 20)

# Кортежи неизменяемы
# colors[0] = "желтый"  # Это вызовет ошибку!</code></pre>
                '''
            },
            {
                "title": "8. Словари и множества",
                "content": '''
                <h1>8. Словари и множества</h1>
                <p>Словари и множества - это неупорядоченные коллекции данных с уникальными характеристиками.</p>
                
                <h2>Словари (dict):</h2>
                <pre><code># Создание словаря
person = {
    "имя": "Иван",
    "возраст": 30,
    "город": "Москва"
}

student = dict(name="Анна", grade=85, subject="математика")

# Доступ к значениям
print(person["имя"])
print(person.get("возраст"))
print(person.get("профессия", "Не указано"))  # Значение по умолчанию

# Изменение словаря
person["возраст"] = 31
person["профессия"] = "программист"

# Удаление элементов
del person["город"]
age = person.pop("возраст")

# Перебор словаря
for key, value in person.items():
    print(f"{key}: {value}")</code></pre>
                
                <h2>Множества (set):</h2>
                <pre><code># Создание множества
unique_numbers = {1, 2, 3, 4, 5}
colors = set(["красный", "зеленый", "синий", "красный"])  # Дубликаты удаляются

# Операции с множествами
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2        # Объединение {1, 2, 3, 4, 5, 6}
intersection = set1 & set2 # Пересечение {3, 4}
difference = set1 - set2   # Разность {1, 2}
symmetric_diff = set1 ^ set2 # Симметричная разность {1, 2, 5, 6}</code></pre>
                '''
            },
            {
                "title": "9. Работа с файлами",
                "content": '''
                <h1>9. Работа с файлами</h1>
                <p>Python предоставляет удобные средства для чтения из файлов и записи в них.</p>
                
                <h2>Открытие и закрытие файлов:</h2>
                <pre><code># Открытие файла для чтения
file = open("example.txt", "r")
content = file.read()
file.close()

# Открытие файла для записи
file = open("output.txt", "w")
file.write("Привет, мир!\n")
file.close()</code></pre>
                
                <h2>Использование контекстного менеджера (рекомендуемый способ):</h2>
                <pre><code># Чтение файла
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Построчное чтение
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip() удаляет символы новой строки

# Запись в файл
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    
    # Запись списка строк
    lines = ["Строка 1\n", "Строка 2\n", "Строка 3\n"]
    file.writelines(lines)</code></pre>
                
                <h2>Режимы открытия файлов:</h2>
                <ul>
                    <li><strong>"r"</strong> - чтение (по умолчанию)</li>
                    <li><strong>"w"</strong> - запись (удаляет содержимое файла)</li>
                    <li><strong>"a"</strong> - добавление (дописывает в конец файла)</li>
                    <li><strong>"r+"</strong> - чтение и запись</li>
                    <li><strong>"x"</strong> - создание файла (ошибка, если файл существует)</li>
                </ul>
                '''
            },
            {
                "title": "10. Обработка исключений",
                "content": '''
                <h1>10. Обработка исключений</h1>
                <p>Исключения - это события, которые нарушают нормальное выполнение программы. Python предоставляет механизмы для их перехвата и обработки.</p>
                
                <h2>Базовая конструкция try-except:</h2>
                <pre><code>try:
    number = int(input("Введите число: "))
    result = 10 / number
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")</code></pre>
                
                <h2>Блоки else и finally:</h2>
                <pre><code>try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Файл не найден!")
else:
    # Выполняется, если исключений не было
    print("Файл успешно прочитан")
    print(content)
finally:
    # Выполняется всегда
    try:
        file.close()
    except:
        pass  # Файл может быть не открыт</code></pre>
                
                <h2>Создание собственных исключений:</h2>
                <pre><code>class CustomError(Exception):
    """Пользовательское исключение"""
    pass

def validate_age(age):
    if age < 0:
        raise CustomError("Возраст не может быть отрицательным!")
    if age > 150:
        raise CustomError("Возраст не может быть больше 150 лет!")

try:
    validate_age(-5)
except CustomError as e:
    print(f"Ошибка валидации: {e}")</code></pre>
                '''
            }
        ]
        
        for lecture_data in lectures_data:
            lecture = Lecture(
                title=lecture_data["title"],
                content=lecture_data["content"]
            )
            db.session.add(lecture)
        
        db.session.commit()
        print("10 lectures created")
    
    # Check if we have any tests
    if Test.query.count() == 0:
        # Create 10 tests with 10 questions each
        tests_data = [
            {
                "title": "Тест 1: Введение в Python",
                "questions": [
                    {
                        "id": 1,
                        "question": "Кто создал язык программирования Python?",
                        "options": ["Деннис Ричи", "Гвидо ван Россум", "Джеймс Гослинг", "Бьёрн Страуструп"],
                        "correct_answer": 1
                    },
                    {
                        "id": 2,
                        "question": "В каком году был выпущен первый релиз Python?",
                        "options": ["1985", "1989", "1991", "1995"],
                        "correct_answer": 2
                    },
                    {
                        "id": 3,
                        "question": "Какой символ используется для создания комментариев в Python?",
                        "options": ["//", "<!-- -->", "#", "/* */"],
                        "correct_answer": 2
                    },
                    {
                        "id": 4,
                        "question": "Какая функция используется для вывода информации на экран в Python?",
                        "options": ["console.log()", "print()", "echo()", "output()"],
                        "correct_answer": 1
                    },
                    {
                        "id": 5,
                        "question": "Какой файловый расширение имеют Python скрипты?",
                        "options": [".py", ".python", ".pt", ".p"],
                        "correct_answer": 0
                    },
                    {
                        "id": 6,
                        "question": "Что такое интерпретируемый язык программирования?",
                        "options": [
                            "Язык, который компилируется в машинный код",
                            "Язык, который выполняется напрямую без компиляции",
                            "Язык, который работает только в веб-браузере",
                            "Язык, который используется только для мобильных приложений"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 7,
                        "question": "Какой из следующих вариантов НЕ является особенностью Python?",
                        "options": [
                            "Простота синтаксиса",
                            "Интерпретируемость",
                            "Строгая типизация во время компиляции",
                            "Обширная стандартная библиотека"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 8,
                        "question": "Где НЕ применяется Python?",
                        "options": [
                            "Веб-разработка",
                            "Научные вычисления",
                            "Разработка операционных систем",
                            "Анализ данных"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 9,
                        "question": "Как правильно написать первую программу на Python?",
                        "options": [
                            "System.out.println(\"Hello, World!\");",
                            "console.log(\"Hello, World!\");",
                            "print(\"Hello, World!\");",
                            "echo \"Hello, World!\";"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 10,
                        "question": "Какой принцип лежит в основе организации кода в Python?",
                        "options": [
                            "Использование фигурных скобок",
                            "Использование отступов",
                            "Использование точек с запятой",
                            "Использование ключевых слов BEGIN/END"
                        ],
                        "correct_answer": 1
                    }
                ]
            },
            {
                "title": "Тест 2: Переменные и типы данных",
                "questions": [
                    {
                        "id": 1,
                        "question": "Как объявить переменную в Python?",
                        "options": [
                            "var x = 5",
                            "int x = 5",
                            "x = 5",
                            "declare x = 5"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 2,
                        "question": "Какой тип данных представляет целые числа в Python?",
                        "options": ["int", "integer", "whole", "number"],
                        "correct_answer": 0
                    },
                    {
                        "id": 3,
                        "question": "Какой функцией можно определить тип переменной?",
                        "options": ["typeof()", "type()", "getType()", "checkType()"],
                        "correct_answer": 1
                    },
                    {
                        "id": 4,
                        "question": "Какой тип данных используется для хранения текста?",
                        "options": ["text", "string", "char", "str"],
                        "correct_answer": 3
                    },
                    {
                        "id": 5,
                        "question": "Какой результат будет у выражения: type(3.14)?",
                        "options": ["<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'decimal'>"],
                        "correct_answer": 1
                    },
                    {
                        "id": 6,
                        "question": "Как правильно создать список в Python?",
                        "options": [
                            "list = {1, 2, 3}",
                            "list = [1, 2, 3]",
                            "list = (1, 2, 3)",
                            "list = <1, 2, 3>"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 7,
                        "question": "Какой тип данных представляет булевы значения?",
                        "options": ["boolean", "bool", "truefalse", "logic"],
                        "correct_answer": 1
                    },
                    {
                        "id": 8,
                        "question": "Как создать словарь в Python?",
                        "options": [
                            "dict = [key: value]",
                            "dict = {key: value}",
                            "dict = (key: value)",
                            "dict = <key: value>"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 9,
                        "question": "Что произойдет при выполнении кода: x = '5'; y = int(x); print(type(y))?",
                        "options": [
                            "<class 'str'>",
                            "<class 'int'>",
                            "<class 'float'>",
                            "Будет ошибка"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 10,
                        "question": "Какой будет результат выражения: 'Привет' + ' ' + 'мир'?",
                        "options": [
                            "'Приветмир'",
                            "'Привет мир'",
                            "Ошибка",
                            "'Привет, мир'"
                        ],
                        "correct_answer": 1
                    }
                ]
            },
            {
                "title": "Тест 3: Операторы и выражения",
                "questions": [
                    {
                        "id": 1,
                        "question": "Какой оператор используется для целочисленного деления в Python?",
                        "options": ["/", "\\", "//", "%"],
                        "correct_answer": 2
                    },
                    {
                        "id": 2,
                        "question": "Что означает оператор ** в Python?",
                        "options": [
                            "Умножение",
                            "Возведение в степень",
                            "Комментарий",
                            "Деление"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 3,
                        "question": "Какой будет результат выражения: 10 % 3?",
                        "options": ["3", "1", "3.33", "0"],
                        "correct_answer": 1
                    },
                    {
                        "id": 4,
                        "question": "Какой оператор используется для логического И в Python?",
                        "options": ["&", "&&", "and", "|"],
                        "correct_answer": 2
                    },
                    {
                        "id": 5,
                        "question": "Что вернет выражение: 5 > 3 and 2 < 4?",
                        "options": ["True", "False", "Ошибка", "None"],
                        "correct_answer": 0
                    },
                    {
                        "id": 6,
                        "question": "Какой будет результат: not True?",
                        "options": ["True", "False", "1", "0"],
                        "correct_answer": 1
                    },
                    {
                        "id": 7,
                        "question": "Что означает оператор != ?",
                        "options": [
                            "Меньше или равно",
                            "Больше или равно",
                            "Не равно",
                            "Равно"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 8,
                        "question": "Какой будет результат: 2 ** 3 ** 2?",
                        "options": ["64", "512", "18", "729"],
                        "correct_answer": 1
                    },
                    {
                        "id": 9,
                        "question": "Что вернет выражение: 7 // 2?",
                        "options": ["3.5", "3", "4", "3.0"],
                        "correct_answer": 1
                    },
                    {
                        "id": 10,
                        "question": "Какой оператор имеет наивысший приоритет?",
                        "options": [
                            "Сложение (+)",
                            "Умножение (*)",
                            "Возведение в степень (**)",
                            "Деление (/)"
                        ],
                        "correct_answer": 2
                    }
                ]
            },
            {
                "title": "Тест 4: Условные операторы",
                "questions": [
                    {
                        "id": 1,
                        "question": "Какой ключевое слово используется для начала условного оператора в Python?",
                        "options": ["if", "when", "condition", "check"],
                        "correct_answer": 0
                    },
                    {
                        "id": 2,
                        "question": "Какой блок выполняется, если условие в if ложно и есть дополнительное условие?",
                        "options": ["else", "elif", "otherwise", "except"],
                        "correct_answer": 1
                    },
                    {
                        "id": 3,
                        "question": "Сколько блоков else может быть в условном операторе?",
                        "options": ["0", "1", "2", "Не ограничено"],
                        "correct_answer": 1
                    },
                    {
                        "id": 4,
                        "question": "Что будет выведено при выполнении кода: x = 5; if x > 10: print('Больше'); elif x > 3: print('Среднее'); else: print('Меньше')?",
                        "options": ["Больше", "Среднее", "Меньше", "Ничего"],
                        "correct_answer": 1
                    },
                    {
                        "id": 5,
                        "question": "Как правильно записать тернарный оператор в Python?",
                        "options": [
                            "condition ? value_if_true : value_if_false",
                            "value_if_true if condition else value_if_false",
                            "if condition then value_if_true else value_if_false",
                            "condition : value_if_true ? value_if_false"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 6,
                        "question": "Что будет результатом: True and False or True?",
                        "options": ["True", "False", "Ошибка", "None"],
                        "correct_answer": 0
                    },
                    {
                        "id": 7,
                        "question": "Какой оператор используется для проверки равенства?",
                        "options": ["=", "==", "===", ":="],
                        "correct_answer": 1
                    },
                    {
                        "id": 8,
                        "question": "Что будет выведено: x = 0; if x: print('Истина'); else: print('Ложь')?",
                        "options": ["Истина", "Ложь", "0", "Ничего"],
                        "correct_answer": 1
                    },
                    {
                        "id": 9,
                        "question": "Как проверить, что переменная x находится в диапазоне от 1 до 10?",
                        "options": [
                            "if 1 <= x <= 10:",
                            "if x >= 1 and x <= 10:",
                            "Оба варианта верны",
                            "if x in range(1, 11):"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 10,
                        "question": "Что будет выведено: x = None; print('Есть значение' if x else 'Нет значения')?",
                        "options": ["Есть значение", "Нет значения", "None", "Ошибка"],
                        "correct_answer": 1
                    }
                ]
            },
            {
                "title": "Тест 5: Циклы",
                "questions": [
                    {
                        "id": 1,
                        "question": "Какие два основных типа циклов существуют в Python?",
                        "options": [
                            "for и while",
                            "loop и repeat",
                            "iterate и cycle",
                            "do и until"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 2,
                        "question": "Что делает функция range(5)?",
                        "options": [
                            "Создает список [1,2,3,4,5]",
                            "Создает список [0,1,2,3,4,5]",
                            "Создает список [0,1,2,3,4]",
                            "Создает список [1,2,3,4]"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 3,
                        "question": "Для чего используется оператор break в цикле?",
                        "options": [
                            "Для перехода к следующей итерации",
                            "Для выхода из цикла",
                            "Для паузы в выполнении",
                            "Для увеличения счетчика"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 4,
                        "question": "Что будет выведено: for i in range(3): print(i, end=' ')?",
                        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
                        "correct_answer": 0
                    },
                    {
                        "id": 5,
                        "question": "Какой цикл гарантирует хотя бы одну итерацию?",
                        "options": [
                            "for",
                            "while",
                            "do-while",
                            "Ни один из перечисленных"
                        ],
                        "correct_answer": 3
                    },
                    {
                        "id": 6,
                        "question": "Что делает оператор continue в цикле?",
                        "options": [
                            "Завершает цикл",
                            "Переходит к следующей итерации",
                            "Повторяет текущую итерацию",
                            "Останавливает выполнение программы"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 7,
                        "question": "Что будет результатом: i = 0; while i < 3: i += 1; print(i)?",
                        "options": ["1 2 3", "0 1 2", "3", "0 1 2 3"],
                        "correct_answer": 2
                    },
                    {
                        "id": 8,
                        "question": "Как перебрать элементы списка colors = ['red', 'green', 'blue']?",
                        "options": [
                            "for color in colors:",
                            "for i in range(len(colors)):",
                            "while colors:",
                            "Оба первых варианта верны"
                        ],
                        "correct_answer": 3
                    },
                    {
                        "id": 9,
                        "question": "Что будет выведено: for i in range(5): if i == 2: continue; if i == 4: break; print(i, end=' ')?",
                        "options": ["0 1 3", "0 1 2 3", "0 1 2 3 4", "0 1 3 4"],
                        "correct_answer": 0
                    },
                    {
                        "id": 10,
                        "question": "Как создать бесконечный цикл?",
                        "options": [
                            "for ;;",
                            "while True:",
                            "loop:",
                            "repeat:"
                        ],
                        "correct_answer": 1
                    }
                ]
            },
            {
                "title": "Тест 6: Функции",
                "questions": [
                    {
                        "id": 1,
                        "question": "Какое ключевое слово используется для определения функции в Python?",
                        "options": ["func", "function", "def", "define"],
                        "correct_answer": 2
                    },
                    {
                        "id": 2,
                        "question": "Что такое аргументы функции?",
                        "options": [
                            "Переменные внутри функции",
                            "Значения, передаваемые в функцию при вызове",
                            "Возвращаемые значения функции",
                            "Имена функций"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 3,
                        "question": "Как вернуть значение из функции?",
                        "options": ["return", "give", "send", "output"],
                        "correct_answer": 0
                    },
                    {
                        "id": 4,
                        "question": "Что будет результатом: def add(a, b=5): return a + b; print(add(3))?",
                        "options": ["3", "5", "8", "Ошибка"],
                        "correct_answer": 2
                    },
                    {
                        "id": 5,
                        "question": "Что такое *args в определении функции?",
                        "options": [
                            "Словарь именованных аргументов",
                            "Список позиционных аргументов",
                            "Обязательный аргумент",
                            "Специальный тип данных"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 6,
                        "question": "Как передать именованные аргументы в функцию?",
                        "options": [
                            "func(value1, value2)",
                            "func(arg1=value1, arg2=value2)",
                            "func[value1, value2]",
                            "func{arg1: value1, arg2: value2}"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 7,
                        "question": "Что будет выведено: def func(a, b=1, c=2): print(a, b, c); func(5, c=10)?",
                        "options": ["5 1 2", "5 10 2", "5 1 10", "Ошибка"],
                        "correct_answer": 2
                    },
                    {
                        "id": 8,
                        "question": "Что такое **kwargs в определении функции?",
                        "options": [
                            "Список позиционных аргументов",
                            "Словарь именованных аргументов",
                            "Обязательные аргументы",
                            "Специальный тип данных"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 9,
                        "question": "Можно ли в функции изменить глобальную переменную?",
                        "options": [
                            "Нет, никогда",
                            "Да, всегда",
                            "Да, но нужно использовать ключевое слово global",
                            "Только для числовых переменных"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 10,
                        "question": "Что будет результатом: def outer(): x = 1; def inner(): nonlocal x; x = 2; inner(); return x; print(outer())?",
                        "options": ["1", "2", "Ошибка", "None"],
                        "correct_answer": 1
                    }
                ]
            },
            {
                "title": "Тест 7: Списки и кортежи",
                "questions": [
                    {
                        "id": 1,
                        "question": "Как создать пустой список в Python?",
                        "options": [
                            "list = {}",
                            "list = []",
                            "list = ()",
                            "list = <>"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 2,
                        "question": "Как получить длину списка?",
                        "options": ["len(list)", "size(list)", "length(list)", "count(list)"],
                        "correct_answer": 0
                    },
                    {
                        "id": 3,
                        "question": "Какой метод добавляет элемент в конец списка?",
                        "options": ["add()", "push()", "append()", "insert()"],
                        "correct_answer": 2
                    },
                    {
                        "id": 4,
                        "question": "Что означает выражение list[1:4]?",
                        "options": [
                            "Элементы с индексами 1, 2, 3",
                            "Элементы с индексами 1, 2, 3, 4",
                            "Элементы с индексами 0, 1, 2, 3",
                            "Элементы с индексами 2, 3, 4"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 5,
                        "question": "Как удалить элемент из списка по значению?",
                        "options": ["pop()", "remove()", "delete()", "clear()"],
                        "correct_answer": 1
                    },
                    {
                        "id": 6,
                        "question": "Чем отличаются списки и кортежи?",
                        "options": [
                            "Списки быстрее, кортежи изменяемы",
                            "Списки изменяемы, кортежи неизменяемы",
                            "Списки используют [], кортежи используют {}",
                            "Нет различий"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 7,
                        "question": "Как создать кортеж с одним элементом?",
                        "options": [
                            "tuple = (element)",
                            "tuple = (element,)",
                            "tuple = [element]",
                            "tuple = {element}"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 8,
                        "question": "Что будет результатом: list = [1, 2, 3]; list[1] = 10; print(list)?",
                        "options": [
                            "[1, 2, 3]",
                            "[1, 10, 3]",
                            "Ошибка",
                            "[10, 2, 3]"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 9,
                        "question": "Как объединить два списка?",
                        "options": [
                            "list1.add(list2)",
                            "list1 + list2",
                            "list1.join(list2)",
                            "list1.merge(list2)"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 10,
                        "question": "Что будет результатом: list = [0, 1, 2, 3, 4]; print(list[::-1])?",
                        "options": [
                            "[0, 1, 2, 3, 4]",
                            "[1, 2, 3, 4]",
                            "[4, 3, 2, 1, 0]",
                            "Ошибка"
                        ],
                        "correct_answer": 2
                    }
                ]
            },
            {
                "title": "Тест 8: Словари и множества",
                "questions": [
                    {
                        "id": 1,
                        "question": "Как создать пустой словарь в Python?",
                        "options": [
                            "dict = []",
                            "dict = {}",
                            "dict = ()",
                            "dict = <>"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 2,
                        "question": "Как получить значение из словаря по ключу?",
                        "options": [
                            "dict[key]",
                            "dict.getKey(key)",
                            "dict.get(key)",
                            "Оба первых варианта верны"
                        ],
                        "correct_answer": 3
                    },
                    {
                        "id": 3,
                        "question": "Как добавить новый элемент в словарь?",
                        "options": [
                            "dict.add(key, value)",
                            "dict[key] = value",
                            "dict.push(key, value)",
                            "dict.append(key, value)"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 4,
                        "question": "Что такое множество (set) в Python?",
                        "options": [
                            "Упорядоченная коллекция с повторяющимися элементами",
                            "Неупорядоченная коллекция с уникальными элементами",
                            "Упорядоченная коллекция с уникальными элементами",
                            "Неупорядоченная коллекция с повторяющимися элементами"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 5,
                        "question": "Как создать множество?",
                        "options": [
                            "set = []",
                            "set = {}",
                            "set = set()",
                            "set = ()"
                        ],
                        "correct_answer": 2
                    },
                    {
                        "id": 6,
                        "question": "Какой метод удаляет элемент из множества?",
                        "options": ["remove()", "delete()", "pop()", "Оба первых варианта верны"],
                        "correct_answer": 3
                    },
                    {
                        "id": 7,
                        "question": "Что будет результатом операции: {1, 2, 3} | {3, 4, 5}?",
                        "options": [
                            "{1, 2, 3, 4, 5}",
                            "{3}",
                            "{1, 2, 4, 5}",
                            "Ошибка"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 8,
                        "question": "Как получить список всех ключей словаря?",
                        "options": [
                            "dict.keys()",
                            "dict.values()",
                            "dict.items()",
                            "dict.list()"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 9,
                        "question": "Что будет результатом: dict = {'a': 1, 'b': 2}; print('a' in dict)?",
                        "options": ["True", "False", "1", "Ошибка"],
                        "correct_answer": 0
                    },
                    {
                        "id": 10,
                        "question": "Как создать множество из списка [1, 2, 2, 3, 3, 4]?",
                        "options": [
                            "set([1, 2, 2, 3, 3, 4])",
                            "{1, 2, 2, 3, 3, 4}",
                            "Оба варианта верны",
                            "set(1, 2, 2, 3, 3, 4)"
                        ],
                        "correct_answer": 2
                    }
                ]
            },
            {
                "title": "Тест 9: Работа с файлами",
                "questions": [
                    {
                        "id": 1,
                        "question": "Как открыть файл для чтения в Python?",
                        "options": [
                            "open(filename, 'r')",
                            "open(filename, 'read')",
                            "read(filename)",
                            "file.open(filename, 'r')"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 2,
                        "question": "Какой режим используется для записи в файл с заменой содержимого?",
                        "options": ["'r'", "'w'", "'a'", "'x'"],
                        "correct_answer": 1
                    },
                    {
                        "id": 3,
                        "question": "Для чего используется контекстный менеджер with?",
                        "options": [
                            "Для ускорения выполнения кода",
                            "Для автоматического закрытия файлов",
                            "Для открытия нескольких файлов одновременно",
                            "Для шифрования файлов"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 4,
                        "question": "Какой метод читает весь файл целиком?",
                        "options": ["readline()", "readlines()", "read()", "readall()"],
                        "correct_answer": 2
                    },
                    {
                        "id": 5,
                        "question": "Как записать строку в файл?",
                        "options": [
                            "file.write(string)",
                            "file.writeline(string)",
                            "file.writelines(string)",
                            "file.append(string)"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 6,
                        "question": "Что произойдет, если открыть несуществующий файл в режиме 'r'?",
                        "options": [
                            "Файл будет создан",
                            "Будет ошибка FileNotFoundError",
                            "Функция вернет None",
                            "Файл будет открыт как пустой"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 7,
                        "question": "Какой режим открывает файл для добавления данных в конец?",
                        "options": ["'r+'", "'w'", "'a'", "'x'"],
                        "correct_answer": 2
                    },
                    {
                        "id": 8,
                        "question": "Как правильно закрыть файл?",
                        "options": [
                            "file.close()",
                            "close(file)",
                            "file.end()",
                            "Оба первых варианта верны при использовании with"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 9,
                        "question": "Что делает метод readline()?",
                        "options": [
                            "Читает весь файл",
                            "Читает одну строку",
                            "Читает все строки в список",
                            "Читает определенное количество символов"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 10,
                        "question": "Какой параметр нужно добавить при работе с текстовыми файлами на русском языке?",
                        "options": [
                            "encoding='utf-8'",
                            "charset='utf-8'",
                            "language='ru'",
                            "unicode=True"
                        ],
                        "correct_answer": 0
                    }
                ]
            },
            {
                "title": "Тест 10: Обработка исключений",
                "questions": [
                    {
                        "id": 1,
                        "question": "Какой блок используется для обработки исключений?",
                        "options": ["catch", "except", "handle", "resolve"],
                        "correct_answer": 1
                    },
                    {
                        "id": 2,
                        "question": "Какой блок выполняется всегда, независимо от наличия исключений?",
                        "options": ["always", "final", "finally", "end"],
                        "correct_answer": 2
                    },
                    {
                        "id": 3,
                        "question": "Какое исключение возникает при делении на ноль?",
                        "options": [
                            "ValueError",
                            "ZeroDivisionError",
                            "ArithmeticError",
                            "MathError"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 4,
                        "question": "Как перехватить несколько типов исключений?",
                        "options": [
                            "except (TypeError, ValueError):",
                            "except TypeError or ValueError:",
                            "except TypeError, ValueError:",
                            "except [TypeError, ValueError]:"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 5,
                        "question": "Как получить информацию об исключении?",
                        "options": [
                            "except Exception as e:",
                            "except Exception e:",
                            "except Exception -> e:",
                            "except Exception (e):"
                        ],
                        "correct_answer": 0
                    },
                    {
                        "id": 6,
                        "question": "Какой блок выполняется, если исключение НЕ возникло?",
                        "options": ["then", "else", "otherwise", "success"],
                        "correct_answer": 1
                    },
                    {
                        "id": 7,
                        "question": "Как вызвать исключение вручную?",
                        "options": ["throw", "raise", "exception", "error"],
                        "correct_answer": 1
                    },
                    {
                        "id": 8,
                        "question": "Какое исключение возникает при попытке преобразовать буквы в число?",
                        "options": [
                            "TypeError",
                            "ValueError",
                            "NumberFormatException",
                            "ConversionError"
                        ],
                        "correct_answer": 1
                    },
                    {
                        "id": 9,
                        "question": "Что будет результатом: try: print(1/0); except: print('Ошибка'); else: print('Успех')?",
                        "options": ["Ошибка", "Успех", "Ошибка Успех", "Ничего"],
                        "correct_answer": 0
                    },
                    {
                        "id": 10,
                        "question": "Как создать собственное исключение?",
                        "options": [
                            "class MyError(Exception): pass",
                            "exception MyError: pass",
                            "def MyError(Exception): pass",
                            "raise MyError"
                        ],
                        "correct_answer": 0
                    }
                ]
            }
        ]
        
        for test_data in tests_data:
            test = Test(
                title=test_data["title"],
                questions=test_data["questions"]
            )
            db.session.add(test)
        
        db.session.commit()
        print("10 tests with 10 questions each created")