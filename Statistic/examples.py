from statistics import mean, median, mode, multimode 

numbers = [2, 1, 3, 7, 1, 5, 4, 8, 1, 0, 5, 9, 3, 6, 5, 9, 10]

print(f'Среднее арифметическое: {mean(numbers)}', f'Медиана: {median(numbers)}', f'Мода: {mode(numbers)}', f'Список мод: {multimode(numbers)}', sep='\n')