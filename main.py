"""
### Задача 1: Средние расходы по семестрам  
Джон записал свои ежемесячные расходы за прошлый год:  
```python
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
```  
Напишите программу, которая с помощью цикла `for` вычисляет средние расходы Джона за первый семестр (январь–июнь) и второй семестр (июль–декабрь).  
"""
"""
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

def first_semester():
    sum = 0
    for i in range(6):
        sum += monthly_spending[i]    
    return sum / 6

print(first_semester())
"""
"""
def second_semestr():
    sum = 0
    for i in range(6, 12):
        sum += monthly_spending[i]    
    return sum / 6

print(second_semestr())  
    
"""


"""
### Задача 2: Кто тратил больше?  
У Джона есть друг Сэм, который также записал свои ежемесячные расходы за прошлый год:  
```python
john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]
```  
Напишите программу, которая сравнивает расходы Джона и Сэма по месяцам и подсчитывает количество месяцев, в которых Джон тратил больше.  

---

john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]

def compare_spending(john_spending, sam_spending):
    months = 0
    for john, sam in zip(john_spending, sam_spending):
        if john > sam:
            months += 1
    return months

months= compare_spending(john_monthly_spending, sam_monthly_spending)
print(f"Джон тратил больше в {months} месяце")




### Задача 3: Список друзей  
У Пола и Тины есть списки друзей:  
```python
paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
```  
Объедините оба списка в один, исключив дублирующиеся имена.  

#paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
#tina_friends = ["Tim", "Susan", "Mary", "Josh"]

#pt_friends = list(set(paul_friends) | set(tina_friends))
#print(pt_friends)





---

### Задача 4: Общие друзья  
Используя те же списки друзей Пола и Тины, напишите программу, которая с помощью цикла находит их общих друзей.  


#paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
#tina_friends = ["Tim", "Susan", "Mary", "Josh"]

#c = []

#for i in paul_friends:
  #  if i in tina_friends:
 #       c.append(i)
#print(c)        
---

### Задача 5: Игроки в баскетбол  
В спортивном клубе зарегистрированы игроки:  
```python
football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}
```  
Напишите программу, которая определяет игроков, зарегистрированных только в баскетболе (не в футболе и не в волейболе).  


#football_players = {"Eve", "Tom", "Richard", "Peter"}  
#volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
#basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}

#basketball_players_only = basketball_players - (football_players | volleyball_players)
#print(basketball_players_only)




---

### Задача 6: Подсчёт голосов  
Результаты опроса о любимом языке программирования:  
```python
poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]
```  
Используя словарь, подсчитайте количество голосов за каждый язык.  
poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]

votes_counted = {}

for item in poll_results:
    if item in votes_counted:
        votes_counted[item] += 1
    else:
        votes_counted[item] = 1
        

print(votes_counted)
---

### Задача 7: Подсчёт очков  
Три друга играют в игру, где каждый игрок зарабатывает очки в трёх раундах. Их результаты:  
```python
scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]
```  
Создайте словарь, где ключами будут имена игроков, а значениями — их суммарные очки.  

---
scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]

games = {}

scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]

games = {}

for player, points in scores:
    if player in games:
        games[player] += points
    else:
        games[player] = points
print(games)


### Задача 8: Статистика списка  
Дан список чисел:  
```python
numbers = [10, 3, 5, 9, 18, 3, 0, 7]
```  
Напишите функцию, которая возвращает максимальное значение, сумму и среднее арифметическое чисел в списке.  

numbers = [10, 3, 5, 9, 18, 3, 0, 7]

def task8(input):
    return {
        "sum": sum(input),
        "max": max(input),
        "avg": sum(input) / len(input)
    }

print(task8(input))
---

### Задача 9: Длинные и короткие слова  
Дан список слов:  
```python
word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
```  
Напишите программу, которая определяет самое длинное и самое короткое слово в списке.  

word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]

def wordss(input_string):
    longest_word = max(word_list, key=len)
    minimal_word = min(word_list, key=len)
    return longest_word, minimal_word

longest, minimal = wordss(word_list)

print(longest, minimal)
---

### Задача 10: Фильтрация по частоте  
Дан список чисел:  
```python
number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]
```  
Создайте новый список, содержащий только числа, которые встречаются в оригинальном списке не менее трёх раз.  

---

### Задача 11: Второй лучший результат  
Дан список результатов экзамена:  
```python
exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]
```  
Напишите программу, которая определяет второй по величине результат в списке.  

--- 
"""
