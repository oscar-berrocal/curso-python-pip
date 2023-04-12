import random



print("""

[ BIENBENIDO AL JUEGO DE PRIDRA PAPEL O TIJERA ]  
    
    """)



def choose_options():
    
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print("esa opcion no es valida")
        # continue
        return None, None

    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('USER WIN!')
            user_wins += 1 

        else:
            print('papel gana a piedra')
            print('COMPUTER WIN!')
            computer_wins += 1

    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('USER WIN!')
            user_wins += 1

        else:
            print('tijera gana a papel')
            print('COMPUTER WIN!')
            computer_wins += 1

    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('USER WIN!')
            user_wins += 1

        else:
            print('piedra gana a tijera')
            print('COMPUTER WIN!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('Computer =>', computer_wins)
        print('User =>', user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        

        if computer_wins == 2:
            print('Computer =>', computer_wins)
            print('User =>', user_wins)
            print("EL GANADOR DEFINITIVO EL COMPUTADOR")
            break
        if user_wins == 2:
            print('*' * 10)
            print('Computer =>', computer_wins)
            print('*' * 10)
            print('User =>', user_wins)
            print('*' * 10)
            print("EL GANADOR DEFINITIVO EL USUARIO")
            break

run_game()