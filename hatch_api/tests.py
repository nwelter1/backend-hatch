from calls import Call

# example of some unit tests
def checkSortField_test():
    call = Call('health', '20', 'asc')
    assert call.checkSortField() == False, "Should be False"

def checkTagsList():
    call = Call('health,science,food', '20', 'asc')
    assert call.tags == ['health', 'science', 'food'], "Should be ['health', 'science', 'food']"

if __name__ == "__main__":
    checkSortField_test()
    checkTagsList()
    print('all tests passed')