with open('demo.txt', 'r') as file:
    str= file.read()
    word_list = str.split()

word = max(word_list)
print("Longest word: ",word)

