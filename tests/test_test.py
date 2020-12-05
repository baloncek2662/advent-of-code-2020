def pytest_test():
	assert 1 == 1

def test_list():
	assert 1 in [1,2,34]
	assert 1 not in ['1',2,3]
