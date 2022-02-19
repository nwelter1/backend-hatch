from calls import Call

# example of some unit tests
def checkSortField_test():
    call = Call('health', '20', 'asc')
    assert call.checkSortField() == False, "Should be False"

def TagsList_test():
    call = Call('health,science,food', '20', 'asc')
    assert call.tags == ['health', 'science', 'food'], "Should be ['health', 'science', 'food']"

if __name__ == "__main__":
    checkSortField_test()
    TagsList_test()
    print('all tests passed')