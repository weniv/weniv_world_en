#-----------------------#
## 전역에서 사용하는 데이터
map_data = {"height": 5, "width": 5}
map_size = 100
border_size = 1
running_speed = 1

character_data = [
    {
        "character": "licat",
        "character_obj": None,
        "x": 0,
        "y": 0,
        "directions": 0,  # 0(동, 오른쪽), 1(북), 2(서, 왼쪽), 3(남)
        "items": {},
    }
]
default_character = "licat" #character_data[0]
mob_data = []

# 맵 전역 아이템 데이터
# (x, y): {item: 'beeper', count: 1}
item_data = {}

wall_data = {"world": {}}

print_data = []
say_data = []

#-----------------------#
## 시스템 기본 데이터
valid_items = ['fish-1','fish-2','fish-3','diamond','apple','goldbar', 'hp-potion','mp-potion']
edible_items = {'hp-potion':{'hp':20},'mp-potion':{'mp':20}}

wall_blocked = ["wall", "fence"]  # 이동 불가한 벽 종류
wall_types = ["wall", "fence", "door"]  # 벽 종류
wall_type = "wall"  # 현재 선택되어 있는 벽 종류

skill_data={
    'claw-yellow':{'mana':10, 'power':10},
    'claw-white':{'mana':10, 'power':10},
    'beam':{'mana':5, 'power':5},
    'explosion':{'mana':20, 'power':20}}

character_info = {
    'licat':{
        'hp':100,
        'mp':100,
        'skill_data':['claw-yellow','claw-white','beam','explosion']
    }
    }

mob_info = {
    'lion':{
        'hp':250,
        'mp':float("inf"),
    },
    'py':{
        'hp':50,
        'mp':float("inf"),
    },
    'binky':{
        'hp':50,
        'mp':float("inf"),
    },
    'gary':{
        'hp':50,
        'mp':float("inf"),
    },
    'wizard':{
        'hp':50,
        'mp':float("inf"),
    },
    }
    
# 오류 정보
error_message = {'OutOfWorld': 'Out of the map.',
    'FrontIsNotClear': "There are obstacles in the character's path.",
    'InvalidCharacter': 'Not a valid character.',
    'CharacterIsNotExist': 'Characters do not exist.', 
    'CharacterIsNotSelected': 'Character not selected.', 
    'CharacterIsNotMovable': 'Character is immovable.',
    'CharacterIsNotAttackable': 'Character cannot be attacked.',
    'ItemIsNotExist': 'The item does not exist.',
    'AnotherItemIsExist': 'Another item exists.',
    'InvalidItem': 'Not a valid item.',
    'InedibleItem': "It's not an edible item.",
    'WallIsExist': 'Wall Exists.',
    'CannotOpenWall': "Can't open a wall that isn't a door.",
    'ObstacleExist': 'Another character or mob exists.', 
    'MobIsExist': 'A mob with that name already exists in the map.',
    'CharacterIsExist': 'The character already exists on the map.',
    'ArgumentsError':'Invalid argument value.',
    'NotEnoughMana':'MP is not enough.',
    'InvalidSkill':'Not a valid skill.',
    'InvalidMob':'Not a valid mob.',
    'InvalidSyntax':'Used invalid grammar.'
    }
#-----------------------#
## 스토리 데이터

story_data = {
    # 1번 스토리
    1: {
        "map_width": 5,
        "map_height": 1,
        "wall": {  # (x, y): "wall", 'fence', 'door'
        },
        "item": {
            (0, 1): {"item": "fish-1", "count": 1},
            (0, 2): {"item": "fish-1", "count": 1},
            (0, 3): {"item": "fish-1", "count": 1},
            (0, 4): {"item": "fish-1", "count": 1},
        },
    },
    # 2번 스토리
    2: {
        "map_width": 5,
        "map_height": 5,
        "wall": {  # (x, y): "wall", 'fence', 'door'
            (0.5, 0): "wall",
            (1.5, 2): "wall",
            (2.0, 0.5): "wall",
            (2.0, 1.5): "wall",
            (2.0, 2.5): "door",
            (2.0, 3.5): "wall",
            (2.5, 1): "wall",
            (2.5, 3): "wall",
        },
        "item": {
            (2, 2): {"item": "diamond", "count": 1},
        },
    },
    # 3번 스토리
    3: {
        "map_width": 5,
        "map_height": 5,
        "wall": {  # (x, y): "wall", 'fence', 'door'
            (0.5, 1): "wall",
            (0.5, 2): "wall",
            (0.5, 3): "wall",
            (1.0, 0.5): "wall",
            (1.0, 3.5): "wall",
            (2.0, 0.5): "wall",
            (2.0, 3.5): "wall",
            (3.0, 0.5): "wall",
            (3.0, 3.5): "wall",
            (3.5, 1): "wall",
            (3.5, 2): "wall",
            (3.5, 3): "wall",
        },
        "item": {
            (0, 1): {"item": "fish-1", "count": 1},
            (0, 3): {"item": "fish-1", "count": 1},
            (2, 4): {"item": "fish-1", "count": 1},
            (4, 1): {"item": "fish-1", "count": 1},
            (4, 0): {"item": "fish-1", "count": 1},
            (2, 0): {"item": "fish-1", "count": 1},
        },
    },
    # 4번 스토리
    4: {
        "map_width": 5,
        "map_height": 1,
        "wall": {  # (x, y): "wall", 'fence', 'door'
        },
        "item": {
            (0, 1): {"item": "fish-1", "count": 2},
            (0, 2): {"item": "fish-2", "count": 5},
            (0, 3): {"item": "fish-3", "count": 10},
        },
    },
    # 5번 스토리
    5: {
        "map_width": 1,
        "map_height": 1,
        "wall": {  # (x, y): "wall", 'fence', 'door'
        },
        "item": {},
        "basic_code":"announcement = 'CEO Licat, Team Lead Mura, Manager Hati'"
    },
    # 6번 스토리
    6: {
        "map_width": 5,
        "map_height": 1,
        "wall": {  # (x, y): "wall", 'fence', 'door'
        },
        "item": {
            (0, 0): {"item": "goldbar", "count": 2},
            (0, 1): {"item": "goldbar", "count": 2},
            (0, 2): {"item": "goldbar", "count": 5},
            (0, 3): {"item": "goldbar", "count": 1},
            (0, 4): {"item": "fish-3", "count": 15},
        },
    },
    # 7번 스토리
    7: {
        "map_width": 5,
        "map_height": 2,
        "wall": {  # (x, y): "wall", 'fence', 'door'
            (0.5, 4): "wall",
            (1.0, 3.5): "door",
        },
        "item": {
            (0, 1): {"item": "fish-1", "count": 12},
            (0, 2): {"item": "goldbar", "count": 15},
        },
    },
    # 8번 스토리
    8: {
        "map_width": 5,
        "map_height": 5,
        "wall": {  # (x, y): "wall", 'fence', 'door'
            (0.5, 1): "wall",
            (0.5, 2): "wall",
            (0.5, 3): "wall",
            (0.5, 4): "wall",
            (1.5, 1): "wall",
            (1.5, 2): "wall",
            (1.5, 3): "wall",
            (1.5, 4): "wall",
            (2.5, 1): "wall",
            (2.5, 2): "wall",
            (2.5, 3): "wall",
            (2.5, 4): "wall",
            (3.5, 1): "wall",
            (3.5, 2): "wall",
            (3.5, 3): "wall",
            (3.5, 4): "wall",
        },
        "item": {
            (0, 3): {"item": "fish-1", "count": 1},
            (0, 4): {"item": "fish-1", "count": 1},
            (1, 3): {"item": "fish-1", "count": 2},
            (1, 4): {"item": "fish-1", "count": 3},
            (2, 3): {"item": "fish-1", "count": 3},
            (2, 4): {"item": "fish-1", "count": 1},
            (3, 3): {"item": "fish-1", "count": 8},
            (3, 4): {"item": "fish-1", "count": 1},
            (4, 2): {"item": "fish-1", "count": 1},
            (4, 3): {"item": "fish-1", "count": 2},
            (4, 4): {"item": "fish-1", "count": 1},
        },
    },
    # 9번 스토리
    9: {
        "map_width": 5,
        "map_height": 5,
        "wall": {  # (x, y): "wall", 'fence', 'door'
            (1.0, 0.5): "wall",
            (1.0, 1.5): "wall",
            (1.0, 2.5): "wall",
            (1.0, 3.5): "wall",
            (2.0, 0.5): "wall",
            (2.0, 1.5): "wall",
            (2.0, 2.5): "wall",
            (2.0, 3.5): "wall",
            (3.0, 0.5): "wall",
            (3.0, 1.5): "wall",
            (3.0, 2.5): "wall",
            (3.0, 3.5): "wall",
            (4.0, 0.5): "wall",
            (4.0, 1.5): "wall",
            (4.0, 2.5): "wall",
            (4.0, 3.5): "wall",
        },
        "item": {
            (4, 0): {"item": "fish-1", "count": 1},
            (3, 1): {"item": "fish-1", "count": 3},
            (4, 2): {"item": "fish-1", "count": 1},
            (2, 3): {"item": "fish-1", "count": 5},
            (3, 4): {"item": "fish-1", "count": 7},
        },
    },
    # 10번 스토리
    10: {
        "map_width": 2,
        "map_height": 5,
        "wall": {  # (x, y): "wall", 'fence', 'door'
            (0.5, 0): "wall",
            (1.5, 1): "wall",
            (2.5, 0): "wall",
            (3.5, 1): "wall",
        },
        "item": {
            (1, 0): {"item": "goldbar", "count": 1},
            (1, 1): {"item": "fish-2", "count": 1},
            (2, 0): {"item": "goldbar", "count": 1},
            (2, 1): {"item": "fish-3", "count": 1},
            (3, 0): {"item": "goldbar", "count": 1},
            (3, 1): {"item": "fish-1", "count": 1},
            (4, 0): {"item": "fish-3", "count": 1},
            (4, 1): {"item": "fish-1", "count": 1},
        },
    },
    # 11번 스토리
    11: {
        "map_width": 5,
        "map_height": 5,
        "wall": {  # (x, y): "wall", 'fence', 'door'
            (0.5, 0): "wall",
            (0.5, 2): "wall",
            (1.5, 1): "wall",
            (1.5, 2): "wall",
            (1.5, 3): "wall",
            (2.5, 0): "wall",
            (2.5, 1): "wall",
            (2.5, 3): "wall",
            (3.5, 1): "wall",
            (3.5, 3): "wall",
            (4.0, 0.5): "wall",
            (4.0, 2.5): "wall",
        },
        "item": {
            (0, 1): {"item": "diamond", "count": 1},
            (1, 0): {"item": "diamond", "count": 2},
            (1, 1): {"item": "diamond", "count": 3},
            (2, 0): {"item": "diamond", "count": 3},
            (2, 1): {"item": "diamond", "count": 1},
            (3, 4): {"item": "diamond", "count": 1},
            (4, 2): {"item": "diamond", "count": 1},
            (4, 4): {"item": "goldbar", "count": 1},
        },
    }, 
    # 12번 스토리
    12: {
        "map_width": 5,
        "map_height": 5,
        "wall": {  
            (0.0, 0.5):	"wall",
            (0.0, 2.5):	"wall",
            (1.0, 0.5):	"wall",
            (1.0, 1.5):	"wall",
            (1.0, 2.5):	"wall",
            (1.0, 3.5):	"wall",
            (2.0, 0.5):	"wall",
            (2.0, 1.5):	"wall",
            (2.0, 2.5):	"wall",
            (2.0, 3.5):	"wall",
            (3.0, 0.5):	"wall",
            (3.0, 1.5):	"wall",
            (3.0, 2.5):	"wall",
            (3.0, 3.5):	"wall",
            (4.0, 1.5):	"wall",
            (4.0, 3.5):	"wall"
        },
        "item": {
                (1, 0): { "item": "fish-2", "count": 1 },
                (3, 1): { "item": "fish-2", "count": 1 },
                (2, 4): { "item": "fish-2", "count": 1 },
                (4, 0): { "item": "hp-potion", "count": 1 },
                (1, 3): { "item": "hp-potion", "count": 1 },
                (0, 3): { "item": "diamond", "count": 1 },
                (2, 2): { "item": "diamond", "count": 1 },
                (3, 4): { "item": "fish-3", "count": 1 },
                (4, 4): { "item": "goldbar", "count": 1 },
                (2, 1): { "item": "goldbar", "count": 1 },
                (5, 0): { "item": "fish-3", "count": 3 }
        },
    },
    13: {
        "map_width": 1,
        "map_height": 1,
        "wall": {  # (x, y): "wall", 'fence', 'door'
        },
        "item": {
        },
        "basic_code":'''
        s = [
            '   + -- + - + -   ',
            '   + --- + - +   ',
            '   + -- + - + -   ',
            '   + - + - + - +   '
        ]
        '''
    },
    14: {
        "map_width": 1,
        "map_height": 1,
        "wall": {  # (x, y): "wall", 'fence', 'door'
        },
        "item": {
        },
        "basic_code":'''
        # Tuple-based colleague information
        crew_info = [
            ("Javadog", 95, "a lifelong Java enthusiast curious about Python. When Python expert Licat suggested him to be a colleague, Javadog felt curious and gave him a small test. Impressed by Licat's wisdom in solving the problem, he became Licat's colleague. He wants to try various things with Python."),
            ("Gary", 85, "met on a ship heading to algorithmic treasures. During a discussion about who would take the remaining seat, Licat suggested the idea of considering the weak using a page replacement algorithm. Gary was impressed and became Licat's colleague."),
            ("SoulGom", 1, "a henchman of Pie and Sun. Moves with infinite power as an NPC and acts as the gatekeeper of the last gate of Pie and Sun. Disguised as a cafe owner, but easily recognized.")
        ]
        '''
    },
    15: {
        "map_width": 5,
        "map_height": 5,
        "wall": { 
            (0.5, 0.0): "wall",
            (0.5, 2.0): "wall",
            (1.0, 0.5): "wall",
            (1.0, 1.5): "wall",
            (1.0, 3.5): "wall",
            (1.5, 0.0): "wall",
            (1.5, 3.0): "wall",
            (1.5, 4.0): "wall",
            (2.0, 1.5): "wall",
            (2.0, 3.5): "wall",
            (2.5, 2.0): "wall",
            (2.5, 3.0): "wall",
            (3.0, 0.5): "wall",
            (3.5, 0.0): "wall",
            (3.5, 2.0): "wall",
            (3.5, 3.0): "wall",
            (4.0, 1.5): "wall",
            (4.0, 3.5): "wall"
        },
        "item": {
            (1, 1): { "item": "hp-potion", "count": 4 },
            (0, 2): { "item": "hp-potion", "count": 3 },
            (1, 3): { "item": "hp-potion", "count": 2 },
            (0, 4): { "item": "hp-potion", "count": 1 },
            (2, 0): { "item": "hp-potion", "count": 4 },
            (3, 1): { "item": "hp-potion", "count": 6 },
            (3, 0): { "item": "mp-potion", "count": 3 },
            (4, 1): { "item": "hp-potion", "count": 4 },
            (3, 2): { "item": "hp-potion", "count": 7 },
            (2, 4): { "item": "hp-potion", "count": 5 },
            (4, 4): { "item": "hp-potion", "count": 4 },
            (2, 3): { "item": "mp-potion", "count": 2 },
            (5, 0): { "item": "hp-potion", "count": 9 }
            },
        "basic_code":"# Number of potions Licat has consumed\npotion_counts = [0, 0, 0, 0]"
    },
    16: {
        "map_width": 1,
        "map_height": 1,
        "wall": { 
        },
        "item": {
        },
        "basic_code":'''
        character = ['Licat', 'Gary', 'Javadog', 'Binky', 'Mura', 'SoulGom', 'Delegate No.1']
        stone = ['Peace Stone', 'Space Stone', 'Mind Stone', 'Reality Stone', 'Time Stone', 'Soul Stone', 'Power Stone']
        '''
    },
    17: {
        "map_width": 4,
        "map_height": 3,
        "wall": {  # (x, y): "wall", 'fence', 'door'
            (0.5, 0): "wall",
            (0.5, 1): "wall",
            (0.5, 2): "wall",
            (1.5, 1): "wall",
            (1.5, 2): "wall",
            (1.5, 3): "wall"
        },
        "item": {
            (2, 0): { "item": "fish-1", "count": 3 },
            (0, 2): { "item": "fish-2", "count": 1 },
            (1, 3): { "item": "fish-2", "count": 2 },
            (2, 2): { "item": "fish-3", "count": 3 },
            (1, 0): { "item": "fish-1", "count": 4 },
            (0, 3): { "item": "fish-3", "count": 2 }
            }
    },
    18: {
        "map_width": 1,
        "map_height": 1,
        "wall": {},
        "item": {},
        "basic_code":"items = [['carrot', 3], ['apple', 5], ['carrot', 6], ['grape', 4], ['carrot', 7]]"
    },
    19: {
        "map_width": 1,
        "map_height": 1,
        "wall": {},
        "item": {},
        "basic_code":'''
        # Check conditions for cooking
        required_ingredient = ["carrot", "lettuce", "onion", "tomato"]
        required_freshness = 5
        required = [False, False, False, False]

        items = [{"name": "carrot", "freshness": 7},
            {"name": "apple", "freshness": 5},
            {"name": "carrot", "freshness": 6},
            {"name": "grape", "freshness": 4}, 
            {"name": "carrot", "freshness": 8}, 
            {"name": "lettuce", "freshness": 8},
            {"name": "onion", "freshness": 2}, 
            {"name": "tomato", "freshness": 5}]
    '''
    },
    20: {
        "map_width": 4,
        "map_height": 4,
        "wall": {
                (0.5, 1.0): "wall",
                (0.5, 2.0): "wall",
                (1.0, 0.5): "wall",
                (1.0, 2.5): "wall",
                (2.0, 0.5): "wall",
                (2.0, 2.5): "wall",
                (2.5, 1.0): "wall",
                (2.5, 2.0): "wall"},
        "item": {
            (0, 3): { "item": "diamond", "count": 6 },
            (0, 1): { "item": "goldbar", "count": 2 },
            (1, 0): { "item": "diamond", "count": 1 },
            (1, 3): { "item": "goldbar", "count": 7 },
            (2, 0): { "item": "goldbar", "count": 1 },
            (3, 2): { "item": "diamond", "count": 4 },
            (3, 3): { "item": "diamond", "count": 9 }
        },
        "basic_code":'''
        class Treasure:
            # Define class
            pass

        # Create instance
        gold = Treasure('gold', 0)
        diamond = Treasure('diamond', 0)

        # Instance list
        treasure_list = [gold, diamond]

        # Print each instance
        for treasure in treasure_list:
            print(treasure)
        '''
    },
    21: {
        "map_width": 1,
        "map_height": 1,
        "wall": {},
        "item": {},
        "basic_code":'''
        class TribeMember:
            pass

        class PortalQueue:
            pass

        tribe_members = [
            TribeMember('member1'), 
            TribeMember('member2'),
            TribeMember('member3'),
            TribeMember('member4'),
            TribeMember('member5')
        ]
        portal_queue = PortalQueue()

        # Create member instances and add to the queue
        for member in tribe_members:
            portal_queue.enter_portal(member)

        # Transport all tribe members
        result = portal_queue.transport_all()
        print(result)
        '''
    },
    22: {
        "map_width": 7,
        "map_height": 5,
        "wall": {
            (0.5, 0): "wall",
            (0.5, 1): "wall",
            (0.5, 4): "wall",
            (0.5, 6): "wall",
            (1.0, 2.5) : "wall",
            (1.0, 4.5) : "wall",
            (1.0, 5.5) : "wall",
            (1.5, 1): "wall",
            (1.5, 2): "wall",
            (1.5, 5): "wall",
            (2.0, 1.5) : "wall",
            (2.0, 4.5) : "wall",
            (3.0, 0.5) : "wall",
            (3.0, 2.5) : "wall",
            (3.0, 4.5) : "wall",
            (3.5, 1): "wall",
            (3.5, 4): "wall",
            (4.0, 1.5) : "wall",
            (4.0, 5.5) : "wall"
            },
        "item": {
            (4, 6): { "item": "diamond", "count": 1 },
        },
        "basic_code":'''
        class PathRecorder:
            # Define class
            pass
        path_recorder = PathRecorder()
        ''',
        "mob_data": [
            {
            "name": "wizard",
            "mob": "wizard",
            "x": 2,
            "y": 3,
            "directions": 3,
            },
            {
            "name": "binky1",
            "mob": "binky",
            "x": 4,
            "y": 0,
            "directions": 0,
            },
            {
            "name": "py1",
            "mob": "py",
            "x": 1,
            "y": 5,
            "directions": 0,
            "hp": 50,
            "power": 10
            },
            {
            "name": "gary1",
            "mob": "gary",
            "x": 2,
            "y": 6,
            "directions": 0,
            "hp": 50,
            }
        ]
    }
}
