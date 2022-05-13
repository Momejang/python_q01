class System:
  def __init__(self):
    self.state = 'S'
  def help(self):
    print(f'사용가능 명령어')
    print(f'1.리스트 출력')
  def exit(self):
    Self.stte = 'Q'

class Character :
  name = ''
  
  def __init__(self, name, lv):
    self.name = name
    self.lv = lv
    self.getInfo()
  def setName(self, name):
    self.name = name
  def setLv(self, ex):
    if(ex > 0):
      self.lv = self.lv + 1
    else:
      print(f'레벨업에 실패하였습니다')
  def getInfo(self):
    printf(f'{self.name} 의 레베은 {self.lv} 입니다')

# 시스템코드 생성
system = System()

# 실행 명령어
while (system.state != 'Q'):
  print(f'명령을 입력해주세요')
  cmd = input('명령')
  print(f'입력한 명령 : {cmd}')

  if(cmd == '종료'):
    system.exit()
  if(cmd == '헬프'):
    system.help()  
