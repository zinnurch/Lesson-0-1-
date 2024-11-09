# phone_book={"zinnur": 89231723357}
# print(phone_book)
# print(phone_book["zinnur"]) #ключ указываем и печатет только номер тел.
# phone_book["anna"]= 89645254046 #так добавляем новый ключ
# print(phone_book)
# del(phone_book["anna"]) #удаление ключа
# print(phone_book)
# phone_book.update({"sasha": 89222222, "ksysha": 8923333}) #через .update добавляем ключи в словарик
# print(phone_book)
# print(phone_book.get("Arkashsa")) #если ключа нет то выводится None
# print(phone_book.get("zinnur")) #если ключ есть, то выводится хначение ключа
# phone_book.pop("zinnur") #метод .pop убирает из списка указанный ключ
# print(phone_book)
# phone_book["zinnur"]=89231723357
# phone_book.keys() # метод .keys показывает что есть в нашем словарике
# print(phone_book.values()) # метод .valuesh показвает только значения в словарике, без ключей
# print(phone_book.items()) # этот метод возвращает целые пары, ключ. значение
set={1,2,3,4,1,2,3,4} #множество в фигурных скобочках
print(set) #хранит только уникальные значения. повторы не выводит
list_=[1, 2, 3, 4, 1, 3, 5, 7]
list_=set(list_)
print(list_)