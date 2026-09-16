file_name='D:\\Practice\\Python\\08_Mastering_input_output\\country_info.txt'

with open(file_name) as country_file:
    for row in country_file:
        data=row.strip('\n').split('|')
        print(data)