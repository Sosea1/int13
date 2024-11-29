# Код преобразует dict в нормально читаемый вид
# step_int формирует отступ для вложенных элементов
# Для вложенных словарей используется рекурсия
test_dict = {
    'First':'First_value',
    'Second': {
        'Second_Inner_Dict':'Inner_value'
        },
        'Second_Second_Inner_Dict': {
            'Inner_Dict': {
                'Inner_Inner_Dict': {
                    'Keeeey':'Valuuue'
                    }
                }
            }
        }
test_dict_2 = {
    '1': {
    'child': '1/child/value'
    },
    '2':'2/value'
}

def my_code(data: dict, step_int = 0): 
    res = ""
    def recurtion(data: dict, step_int: int, res: str):
        for key, value in data.items():  
            res+='  ' * step_int + f"{key}:"+'\n'      
            if isinstance(value, dict):  
                res = recurtion(value, step_int+1, res=res) 
            else:    
                res+='  ' * (step_int+1) + f"{value}"+'\n'
        return res
        
    res = recurtion(data=data, step_int=step_int, res=res)          
    return res

print('----test_dict------\n'+my_code(test_dict))
print('----test_dict_2------\n'+my_code(test_dict_2))