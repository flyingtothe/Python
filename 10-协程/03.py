# yield from
def gen():
    for c in 'AB':
        yield c
# list 直接用生成器做参数
print(list(gen()))
def gen_new():
    yield  from 'AB'
print(list(gen_new()))