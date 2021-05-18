# Dictionary

car = {'brand':'Toyota', 'model':'Prius', 'year':2015, 1:100}
print(car['brand'])
print(car.get('bran', 12)) #.get()メソッドの場合、第一引数がない場合、第二引数を表示する

print(car.get(1))

print(car.keys()) #キー一覧
print(car.values()) #値一覧
print(car.items()) #キー＋値一覧

for k, v in car.items():
  print('key = {}, value = {}'.format(k,v))

if 'bran' in car:
  print('carのブランドは{}'.format(car['brand']))
else:
  print('その情報は存在しません')

