import json

data_source="D:\\Practice\\Python\\08_Mastering_input_output\\temperature_anomaly.json"

with open(data_source,encoding='utf-8') as data:
    anomalies=json.load(data)

print(anomalies['description'])

for year,value in anomalies['data'].items():
    year,value=int(year),float(value)
    print(f"{year} .... {value:6.2f}")

print(anomalies['citation'])