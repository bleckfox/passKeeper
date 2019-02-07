# Создание файла учетных записей
import shelve
import QuestandAnsw


########################################
''' Создаю функцию, в ней пишу код добавления новых учетных записей.
    Введенные значения записываю как ключ и значение соответственно в файл.
'''
def add_account():
        while True:
            add_account = input('Хотите добавить аккаунт?\n'
                                'Да (добавить)\n'
                                'Enter (не добавлять)\n').lower()
            if add_account == 'да':
                account = input('Введите логин: ')
                password = input('Введите пароль: ')
                Account_File[account] = password
                print('---------------------------')
            elif add_account != 'да':
                print('---------------------------')
                break
########################################
''' Тоже самое только удаляю данные из файла.
    Удаляю ключ, а вместе с ним удаляется значение.
'''
def pop_account():
        while True:
            pop_account = input('Хотите удалить аккаунт?\n'
                                'Да (удалить)\n'
                                'Enter (не удалять)\n').lower()
            if pop_account == 'да':
                account = input('Введите логин: ')
                Account_File.pop(account, 'Такого логина уже нет')
                print('Аккаунт успешно удалён.')
            elif pop_account != 'да':
                print('---------------------------')
                break
########################################


'''Выбираем аккаунт из списка'''

########################################
def choose_login():
        while True:
                print('---------------------------')
                print(list(Account_File.keys()))
                print('---------------------------')
                choose_login = input('Выберите логин: ')
                if choose_login in Account_File.keys():
                        print(str(Account_File[choose_login]))
                        print('---------------------------')
                elif choose_login == '':
                        print('Идем дальше.')
                        print('---------------------------')
                        break
                elif choose_login not in Account_File.keys():
                        print('///////////////////////////')
                        print('Такого логина нет.')
                        print('///////////////////////////')
                        continue
#######################################
#                                     #
#######################################
Account_File = shelve.open('Account')
user_dict = {}
final_dict = {}

answer = QuestandAnsw.answ()

#Проверка пользователя для доступа к базе учетных записей(файлу).
while True:
        test = input('Введите ответ на вопрос или Enter, чтобы выйти: ')
        if test == answer:
                while True:
                        choose_login()
                        #подключаю написанные выше функции
                        add_account()
                        pop_account()
                        stop = input('Хотите закрыть программу?  ')
                        if stop == 'да':
                                break
                        
        elif test == '':
                print('Выход из общего цикла')
                break                
        elif test != answer:
                test = input('Попробуйте ещё раз:  ')
                print('---------------------------')
                continue
        
        

Account_File.close()
exit_input = input('Нажмите Enter чтобы закрыть окно. ')
del exit_input
