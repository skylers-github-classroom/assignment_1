from module_1 import Add

def test_add():
    me = Add()
    assert(me.add_correct(1, 2) == 3)
    assert(me.add_incorrect(1, 2) == 3)

if __name__ == "__main__":
    test_add()
    print("Everything passed")