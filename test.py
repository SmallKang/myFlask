from collections import namedtuple

def load_user(id):
    user = namedtuple('user', 'id name age')
    a = user(1, 'A', 18)
    b = user(2, 'B', 20)
    l = [a, b]
    for i in l:
        if i.id == id:
            return i

if __name__ == '__main__':
    print(load_user(1))