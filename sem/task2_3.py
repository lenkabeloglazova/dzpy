n = int(input("Введите число: "))

count = 0
result = 0

for i in range(n) :

    temp = int(input(f"{i + 1}-день: "))

    if(temp > 0) :

        count = count + 1
        
        if(count > result) :
            result = count

    else :
        count = 0

print(f"Количество дней с средней температурой больше 0 градусов: {result}")
