#import utils

data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():
  
  keys, values = utils.get_population()
  print(keys, values)
    
  country = input('Type Country => ')
  results = utils.population_by_country(data, country)
  print(results)


#Para realizar el reto:
import utils
import read_csv3
import charts

def run_arg():
  data = read_csv3('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage', data]))
  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result)>0:
    country = result[0]
    print(country)
    labels, values = utils.get_population_arg(country)
    charts.generate_bar_chart(country['Country'], labels, values)
  
if __name__ == '__main__':
  run_arg()
  #run()