resp = {'success': True,
 'timestamp': 1656491220,
 'date': '2022-06-29',
 'base': 'USD',
 'rates': {'LME-ALU': 12.86028,
  'LME-XCU': 3.7815455187015,
  'STEEL-HR': 46.48935467341,
  'USD': 1}}

def copperPrice():
    copperPrice = (1/resp['rates']['LME-XCU'])*35.724

    return copperPrice

def steelPrice():
    steelPrice = (1/resp['rates']['STEEL-HR'])*35.724

    return steelPrice

def aluminiumPrice():
    aluminiumPrice = (1/resp['rates']['LME-ALU'])*35.724

    return aluminiumPrice

