import time

def get_list(val):
    list_of_method = []
    list_of_forbid = ['conjugate','bit_length','from_bytes','to_bytes']
    for atr in dir(val):
        if callable(getattr(val, atr)):
            if atr[:2]!='__':
                if atr not in list_of_forbid:
                    list_of_method.append(atr)
    return list_of_method


def profile(object_to_decorate):

    def the_wrapper_around_function(*args):
        print('Начало работы функции '+object_to_decorate.__name__)
        t = time.clock()
        res = object_to_decorate(*args)
        print("Время выполнения функции: %f" % (time.clock()-t))
        return res

    if str(type(object_to_decorate)) == "<class 'function'>":
        return the_wrapper_around_function
    else:
        return my_shiny_new_decorator(object_to_decorate)



def the_wrapper_around_method(method,*args):
        def new_method(self):
            print('Начало работы функции '+method.__name__)
            t = time.clock()
            res = method(self,*args)
            print("Время выполнения функции: %f" % (time.clock() - t))
            return res
        return new_method

def my_shiny_new_decorator(object_to_decorate):
        list_of_method=get_list(object_to_decorate)
        for attr_name in list_of_method:
            attr = getattr(object_to_decorate, attr_name)
            setattr(object_to_decorate, attr_name, the_wrapper_around_method(attr))
        return object_to_decorate



@profile
def func(num):
    for i in range(100):
        num+=1
        num=num*i*i
    return num*num


@profile
class Lol:
    def __init__(self,val):
        self._value=val

    def _kek(self):
        return self._value


func(1)
numb=Lol(1)
numb._kek()


