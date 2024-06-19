# Snowball Game

# 구현 목표
본 프로젝트는 눈싸움 게임이 목적이며, 두 플레이어가 서로 떨어지는 펭귄을 피해 상대에게 눈덩이를 던져 상대방의 HP(체력)을 깎는 것이 게임의 목표이다. 게임 종료 조건은 상대의 HP(체력)이 0이 될 경우 승리한다.

# 구현 기능
* pygame 기반 게임 board(환경) 구현
* 키보드 입력으로 눈덩이 던지기 기능
* 눈덩이에 맞을 시 체력이 깎이는 기능

## Phase2 구현 기능
* 여러 장애물을 제작 -> 장애물 파괴시 점수 획득(펭귄 1점, 북극곰 2점)
* 소리 효과들 삽입(배경음악 삽입, buff 모드시 효과음 삽입)
* 점수가 오르면 buff 모드 진입 -> buff 시 눈 무한대로 던지기 가능(5초)

# Reference
[1] https://github.com/techwithtim/PygameForBeginners

[2] https://github.com/pygame/pygame

# 지원 Operating Systems 및 실행 방법

## 지원 Operating Systems
|OS| 지원 여부 |
|-----|--------|
|windows | :x:  |
| Linux  | :o: |
|MacOS  | :o:  |

## 실행 방법
### MacOS, Linux
1. pygame을 설치한다.
```
pip3 install pygame
```
2. main.py를 실행하면 게임 창이 뜨면서 실행된다.
```
python3 main.py
```

# 실행 예시
![화면 기록 2024-06-01 오후 9 40 54](https://github.com/parkjiung123/project1/assets/72504995/223da201-b4a2-4520-a885-6dd65144508b)

# 게임 방법
- Boy(왼쪽 플레이어)
    1. 이동: 'A' (왼쪽), 'D' (오른쪽), 'W' (위), 'S' (아래)
    2. 눈덩이 던지기: 'V'
- Girl(오른쪽 플레이어)
    1. 이동: '←' (왼쪽), '→' (오른쪽), '↑' (위), '↓' (아래)
    2. 눈덩이 던지기: '/'

# 코드 설명
## main.py
### class Penguin
- Description : 화면 위에서 아래로 떨어지는 펭귄 객체를 나타내는 클래스
  1. Def __init__(self,x,y) : 펭귄 객체의 초기 위치를 설정한다. 'x', 'y': 펭귄의 초기 위치 좌표이다.
  2. Def draw(self) : 펭귄을 화면에 그린다. 펭귄의 위치를 업데이트하여 아래로 이동시킨다.
### class Polarbear:
- Description : 화면 위에서 아래로 떨어지는 북극곰 객체를 나타내는 클래스
  1. Def __init__(self,x,y) : 북극곰 객체의 초기 위치를 설정한다. 'x', 'y': 북극곰의 초기 위치 좌표이다.
  2. Def draw(self) : 북극곰을 화면에 그린다. 북극곰의 위치를 업데이트하여 아래로 이동시킨다.
  3. self.num : 북극곰의 사진은 총 2개이다. 둘 중 몇 번째 사진을 픽할지 랜덤으로 정한다 

### Function
- draw_display
    1. Parameters : 'girl', 'boy': 소녀와 소년 캐릭터의 위치와 크기를 나타내는 Rect 객체이다. 
    'girl_snowball', 'boy_snowball': 소녀와 소년이 던진 눈덩이 리스트이다. 
    'penguins': 현재 화면에 존재하는 펭귄 리스트이다. 
    'girl_hp', 'boy_hp': 소녀와 소년의 HP값이다.
    2. Def draw_display(girl, boy, girl_snowball, boy_snowball, penguins, girl_hp, boy_hp) : 배경, 캐릭터, 눈덩이, 펭귄 및 HP를 화면에 그린다.
- boy_handle_movement
    1. Parameters: 'keys_pressed' : 현재 눌려진 키의 상태를 나타내는 Pygame 키 배열이다.
    'boy': 소년 캐릭터의 위치와 크기를 나타내는 Rect 객체이다.
    2. Def boy_handle_movement(keys_pressed, boy) : 눌려진 키에 따라 소년 캐릭터를 이동시킨다.
- girl_handle_movement
    1. Parameters: 'keys_pressed' : 현재 눌려진 키의 상태를 나타내는 Pygame 키 배열이다.
    'girl': 소녀 캐릭터의 위치와 크기를 나타내는 Rect 객체이다.
    2. Def girl_handle_movement(keys_pressed, girl) : 눌려진 키에 따라 소녀 캐릭터를 이동시킨다.
- handle_snowball
    1. Parameters: 'boy_snowball', 'girl_snowball' : 소년과 소녀가 던진 눈덩이 리스트이다.
    'boy', 'girl': 소년과 소녀 캐릭터의 위치와 크기를 나타내는 Rect 객체이다.
    'penguins': 현재 화면에 존재하는 펭귄 리스트이다.
    2. Def handle_snowball(boy_snowball, girl_snowball, boy, girl, penguins) : 눈덩이가 화면 밖으로 나가거나, 상대방 캐릭터 또는 펭귄과 충돌하는 경우를 처리한다.
- draw_winner
    1. Parameters: 'text' : 승리 메시지를 나타내는 문자열이다.
    2. Def draw_winner(text) : 게임이 끝났을 때 승자를 화면에 표시한다.
- set_boy_buff, set_girl_buff
    1. Parameters: 'boy_point', bp : 현재 boy의 point와 이번 턴에 증가할 포인트이다
    2. 현재 point가 20점 이상이면 던질 수 있는 눈 갯수를 크게 증가시킨다(5초동안)
- main
    1. Description : 게임의 메인 함수이다.
    2. Def main() : 게임 초기 설정을 하고, 메인 루프를 실행하여 사용자 입력과 게임 상태를 업데이트하고 화면을 새로 그린다.