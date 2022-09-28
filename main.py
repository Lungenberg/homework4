input_word = 0
word_to_guess = str("apple")

print("Угадай букву!")
print("Как переводится слово 'яблоко' на английском?")
while input_word != word_to_guess:
    input_word = str(input("Введите слово: "))
    if input_word == word_to_guess:
        print("Вы угадали!")
    else:
        print("Неправильно! Попробуйте ещё!")
print("Игра окончена")
