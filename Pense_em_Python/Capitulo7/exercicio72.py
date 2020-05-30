def eval_loop():
    while True:
        word = input('Digite algo, expressão ou comando: ')
        if word == 'done':
            print(word)
            break
        print(eval(word))


eval_loop()
