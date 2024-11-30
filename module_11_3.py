# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта
#  чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).

def introspection_info(obj):
    obj_type = str(type(obj))

    attributes = dir(obj)

    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    obj_module = getattr(obj, '__module__', 'N/A')

    info_list = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info_list


# Пример использования функции
if __name__ == "__main__":
    class SampleClass:
        def sample_method(self):
            pass

    sample_obj = SampleClass()
    info_list = introspection_info(sample_obj)
    print(info_list)