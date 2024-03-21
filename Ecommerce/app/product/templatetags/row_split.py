from django import template

register = template.Library()

@register.filter(name='row_split')
def row_split(list_data, split_size):
    if list_data is None:
        return [] 
    
    input_data = []
    i = 0
    for data in list_data:
        input_data.append(data)
        i = i + 1
        if i == split_size:
            yield input_data
            
            input_data = []
            i = 0
    if input_data:
        yield input_data