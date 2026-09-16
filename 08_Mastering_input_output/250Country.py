file_name='D:\\Practice\\Python\\08_Mastering_input_output\\country_info.txt'

countries={}
with open(file_name) as country_file:
    country_file.readline() # read the first line so point if moved to 2 nd line in for loop
    for row in country_file:
        data=row.strip('\n').split('|')
        country,capital,code,code3,dialing,timezone,currecny=data
        # print(country, capital,code,code3,dialing,timezone,currecny,sep="\n \t")
        country_dict={
            'name':country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone':timezone,
            'currency': currecny
        }

    

        # print(country_dict)
        countries[country.casefold()]=country_dict
