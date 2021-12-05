from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act 
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected_value = 0 
    # Assert 
    assert starting_value == expected_value

def test_update_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act 
    expected_value = 15 
    simple_storage.store(expected_value, {"from": account})
    # Assert
    assert expected_value == simple_storage.retrieve()
