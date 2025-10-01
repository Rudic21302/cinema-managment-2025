def load_data(file_path, str_to_dict_func):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [str_to_dict_func(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_data(file_path, data_list, dict_to_str_func):

    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(dict_to_str_func(item) + '\n')

def generate_next_id(data_list, prefix):

    if not data_list:
        return f"{prefix}1"
        
    max_num = 0
    for item in data_list:
        if 'id' in item and item['id'].startswith(prefix):
            try:
                num = int(item['id'][len(prefix):])
                max_num = max(max_num, num)
            except ValueError:
                continue
    
    return f"{prefix}{max_num + 1}"

def find_by_id(data_list, item_id):

    for item in data_list:
        if item.get('id') == item_id:
            return item
    return None

def find_index_by_id(data_list, item_id):

    for index, item in enumerate(data_list):
        if item.get('id') == item_id:
            return index
    return -1

def format_header(headers):

    header_row = ''
    separator_row = ''
    
    for name, width in headers:
        header_row += f"{name:{width}} | "
        separator_row += '-' * width + '-+-'
    
    return f"{header_row.rstrip(' |')}\n{separator_row.rstrip('-+')}"

def format_row(data_dict, keys_order, widths):

    row = ''
    for key, width in zip(keys_order, widths):
        value = str(data_dict.get(key, ''))
        row += f"{value:{width}} | "
    
    return row.rstrip(' |')