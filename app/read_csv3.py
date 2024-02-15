import csv

#Para cargarlo 
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
      print('***'*5)
      print(row)

#Tenemos que transformarlo en una lista
def read_csv2(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    for row in reader:
      iterable = zip(header, row)
      print(list(iterable))

#Para obtener una lista de diccionarios en donde tengo clave valor, para consular la info con la columna
def read_csv3(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key:value for key, value in iterable}
      data.append(country_dict)
    return data
      
if __name__ == '__main__':
  #read_csv3('data.csv')
  data = read_csv3('data.csv')
  print(data[0])