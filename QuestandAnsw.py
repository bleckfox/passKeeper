''' Этот файл хранит данные о вопросе, о ответе
для внутренней проверки доступа к базе данных
учетных записей.
'''
import shelve
File = shelve.open('QuestandAnsw')
def quest():
      try:
            print(File['question'])
      except KeyError:
          question = input('Введите вопрос: ')
          File['question'] = question
          File.close()
quest()

#теперь для вопроса
def answ():
      File = shelve.open('QuestandAnsw')
      try:
          if File['answer'] == '':
              print('I dont know answer')
              answer = input('Enter answer: ')
              File['answer'] = answer
          answer_s = str(File['answer'])
          return answer_s
      except KeyError:
          answer = input('Enter answer: ')
          File['answer'] = answer
          File.close()
answ()
