import time
import types


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
    def the_wrapper_around_function(val):
        def new_func(*args):
            print('Начало работы функции ' + val.__name__)
            t = time.clock()
            res = val(*args)
            print("Время выполнения функции: %f" % (time.clock() - t))
            return res

        return new_func

    def the_wrapper_around_class(kls):
        print(type(kls))
        list_of_method = get_list(kls)
        for attr_name in list_of_method:
            attr = getattr(kls, attr_name)
            setattr(kls, attr_name, the_wrapper_around_function(attr))
        return kls

    if type(object_to_decorate) is types.FunctionType:
        return the_wrapper_around_function(object_to_decorate)
    else:
        return the_wrapper_around_class(object_to_decorate)



@profile
def func(num):
    for i in range(100):
        num += 1
        num = num*i*i
    return num*num


@profile
class Lol:
    def __init__(self,val):
        self._value=val

    def _kek(self):
        return self._value


func(1)
chis=Lol(1)
chis._kek()


