#if文

class ClassA():

  def __init__(self, a):
    self.a = a

  def __bool__(self):
    if self.a =='a':
      return True
    return False


ver = ClassA('a')
print('boolの計算結果: {}'.format(bool(ver)))
if ver:
  print('if文の中の処理')