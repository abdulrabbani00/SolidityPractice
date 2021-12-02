// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage { // similar to a class
    
    // this will get initialized to 0!
    uint256 public favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    //People public person = People({favoriteNumber: 2, name: "Abdul"});
    // Array
    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // view, pure - Do not change state.
    // view - does not lead to transcations.
    // pure - does computation but doesnt store the state
    function retrieve() public view returns(uint256) {
        return favoriteNumber;
    }

    // memory, storage
    // memory - stores only during exection
    // storage - stored even after execution
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        //people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
    
}