class System:
  def __init__(self):
    self.state = 'S'
  def help(self):
    print(f'사용가능 명령어')
    print(f'1.헬프')
    print(f'2.종료')
    print(f'3.캐릭터생성')
    print(f'4.캐릭터정보')
  def exit(self):
    self.state = 'Q'

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

    print(f'{self.name} 의 레벨은 {self.lv} 입니다')

# 시스템코드 생성
system = System()
# 캐릭터 저장공간
chArr = []

# 실행 명령어
while (system.state != 'Q'):
    print(f'#############################################')
    print(f'명령을 입력해주세요. -헬프 (명령어 리스트 출력)')
    cmd = input('명령 :')
    print(f'입력한 명령 : {cmd}')

    if(cmd == '종료'):
        system.exit()

    if(cmd == '헬프'):
        system.help()

    if(cmd == '캐릭터생성'):
        name = input('캐릭터 이름 입력:')
        lv = 1
        chArr.append(Character(name, lv))

    if(cmd == '캐릭터정보'):
        if(len(chArr) < 1):
            print(f'생성된 캐릭터가 없습니다')
        else:
            for x in chArr:
                x.getInfo()
