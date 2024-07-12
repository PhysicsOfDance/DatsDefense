import os
from dotenv import load_dotenv

from src.models import Base
load_dotenv()

from api import *
from src.drawer import draw_map

def main():
#     print(f"Token is {os.getenv('TOKEN')}")
#     msg, participating = participate()
#     print(msg)
#     if not participating:
#         print("Exiting")
#         return None
    
    # for base in get_dynamic_objects()['base']:
    base = {
        "attack": 10,
        "health": 100,
        "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
        "isHead": True,
        "lastAttack": {
            "x": 1,
            "y": 1
        },
        "range": 5,
        "x": 1,
        "y": 1
    }
    print(Base(**base))

    # print(get_dynamic_objects())
    # print()
    # print(get_static_objects())

    # drawer_input = {'realmName': 'test-day1-3', 'zpots': [{'x': 193, 'y': 435, 'type': 'default'}, {'x': 210, 'y': 434, 'type': 'default'}, {'x': 192, 'y': 435, 'type': 'default'}, {'x': 210, 'y': 432, 'type': 'default'}, {'x': 210, 'y': 435, 'type': 'default'}, {'x': 195, 'y': 429, 'type': 'default'}, {'x': 210, 'y': 427, 'type': 'default'}, {'x': 210, 'y': 422, 'type': 'default'}, {'x': 195, 'y': 434, 'type': 'default'}, {'x': 195, 'y': 427, 'type': 'default'}, {'x': 209, 'y': 435, 'type': 'default'}, {'x': 210, 'y': 430, 'type': 'default'}, {'x': 197, 'y': 435, 'type': 'default'}, {'x': 204, 'y': 435, 'type': 'default'}, {'x': 195, 'y': 428, 'type': 'default'}, {'x': 195, 'y': 421, 'type': 'default'}, {'x': 195, 'y': 425, 'type': 'default'}, {'x': 208, 'y': 435, 'type': 'default'}, {'x': 213, 'y': 435, 'type': 'default'}, {'x': 195, 'y': 422, 'type': 'default'}, {'x': 210, 'y': 428, 'type': 'default'}, {'x': 207, 'y': 435, 'type': 'default'}, {'x': 194, 'y': 435, 'type': 'default'}, {'x': 210, 'y': 420, 'type': 'default'}, {'x': 195, 'y': 424, 'type': 'default'}, {'x': 203, 'y': 435, 'type': 'default'}, {'x': 206, 'y': 435, 'type': 'default'}, {'x': 210, 'y': 426, 'type': 'default'}, {'x': 200, 'y': 435, 'type': 'default'}, {'x': 195, 'y': 430, 'type': 'default'}, {'x': 195, 'y': 431, 'type': 'default'}, {'x': 212, 'y': 435, 'type': 'default'}, {'x': 195, 'y': 433, 'type': 'default'}, {'x': 199, 'y': 435, 'type': 'default'}, {'x': 210, 'y': 433, 'type': 'default'}, {'x': 210, 'y': 424, 'type': 'default'}, {'x': 195, 'y': 420, 'type': 'default'}, {'x': 210, 'y': 431, 'type': 'default'}, {'x': 210, 'y': 421, 'type': 'default'}, {'x': 210, 'y': 429, 'type': 'default'}, {'x': 205, 'y': 435, 'type': 'default'}, {'x': 195, 'y': 426, 'type': 'default'}, {'x': 210, 'y': 425, 'type': 'default'}, {'x': 195, 'y': 435, 'type': 'default'}, {'x': 196, 'y': 435, 'type': 'default'}, {'x': 195, 'y': 432, 'type': 'default'}, {'x': 202, 'y': 435, 'type': 'default'}, {'x': 198, 'y': 435, 'type': 'default'}, {'x': 195, 'y': 423, 'type': 'default'}, {'x': 211, 'y': 435, 'type': 'default'}, {'x': 210, 'y': 423, 'type': 'default'}, {'x': 201, 'y': 435, 'type': 'default'}]}
    # draw_map(drawer_input)


if __name__ == "__main__":
    main()