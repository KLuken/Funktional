class Typ:
    pass

class Bool(Typ):
    set = {'True', 'False'}

class Char(Typ):
    pass

class Lizt(list):
    def __init__(self, *value):
        try:
            if self.__has_common_type(value):
                self = value
        except:
               raise TypeError("Not a homogenous list")

    @staticmethod
    def __has_common_type(value):
        for i in range(0, len(value)-2):
            if value[i].__class__.__name__ != value[i+1].__class__.__name__:
                return False
            else:
                continue
        return True

# def _flattened_list(lizt):
#     if isinstance(lizt, list):
#         pass
#     else:
#         raise TypeError("Not a list")
#     flattened_list = []
#     def flatten_list(lizt):
#         for lst in lizt:
#             if isinstance(lst, list):
#                 flatten_list(lst)
#             else:
#                 flattened_list.append(lst)
#         return flattened_list
#     return flatten_list(lizt)

class Tupl(Typ):
    pass

class Innt(Typ):
    pass