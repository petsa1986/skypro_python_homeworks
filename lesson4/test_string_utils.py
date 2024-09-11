import pytest
from string_utils import StringUtils
util = StringUtils()

"""capitalize"""

def test_capitilize ():
    """POSITIVE"""
    assert util.capitilize ("установка") == "Установка"
    assert util.capitilize ("создание первого теста") == "Создание первого теста"
    assert util.capitilize ("123") == "123"
    """NEGATIVE"""
    assert util.capitilize ("") == ""
    assert util.capitilize (" ") == " "
    assert util.capitilize ("12345тест") == "12345тест"

"""trim"""

def test_trim ():
    """POSITIVE"""
    assert util.trim (" задание") == "задание"
    assert util.trim ("  введите слово ") == "введите слово "
    assert util.trim (" 123") == "123"
    """NEGATIVE"""
    assert util.trim ("") == ""

@pytest.mark.xfail() 
def test_trim_with_numbers_input ():
    assert util.trim (123) =="123"  

"""to_list"""    

@pytest.mark.parametrize ('string, delimeter, result', [
    #POSITIVE:
    ("one,two,three", ",", ["one", "two", "three"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    #NEGATIVE:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ])

def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = util.to_list(string)
    else:
        res = util.to_list(string, delimeter)
    assert res == result

"""contains"""    
@pytest.mark.parametrize ('string, symbol, result', [
    #POSITIVE:
    ("Peter", "e", True),
    (" test", "t", True),
    ("space  ", "e", True),
    ("who-who", "-", True),
    ("123", "1", True),
    ("", "", True),
    #NEGATIVE:
    ("City", "c", False),
    ("parameter", "P", False),
    ("hello", "x", False),  
    ("12345", "!", False),  
    ("", "x", False),  
    # (("hello", "", False))
])

def test_contains(string, symbol, result):
    res = util.contains (string, symbol)
    assert res == result


"""delete_symbol"""    

@pytest.mark.parametrize('string, symbol, result', [
    #POSITIVE:
    ("ctript", "t", "crip"),
    ("Town", "T", "own"),
    ("12345", "1", "2345"),
    ("Peter-Who", "-", "PeterWho"),
    ("itteration", "itter", "ation"),
    #NEGATIVE:
    ("spoon", "k", "spoon"),
    ("", "", ""),
    ("", "g", ""),
    ("молоко", "", "молоко"),
    ("calat  ", "t", "cala  ")
])

def test_delete_symbol(string, symbol, result):
    res = util.delete_symbol(string, symbol)
    assert res == result

"""starts_with"""

@pytest.mark.parametrize('string, symbol, result', [
    #POSITIVE:
    ("test", "t", True),
    ("", "", True),
    (" Учеба", "", True),
    ("Forewer  ", "F", True),
    ("123", "1", True),
    #NEGATIVE:
    ("Summer", "s", False),
    ("fall", "F", False),
    ("", "v", False),
    ("winter", "e", False),
    
])
def test_starts_with(string, symbol, result):
    res = util.starts_with(string, symbol)
    assert res == result

"""end_with"""    

@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки:
    ("coffee", "e", True),
    ("teA", "A", True),
    ("", "", True),
    ("one ", "", True),
    ("123", "3", True),
    ("why-why", "y", True),
    ("test ", "", True),
    #Негативные проверки:
    ("one", "P", False),
    ("two", "e", False),
    ("Three", "E", False),
    ("", "n", False)
])
def test_end_with(string, symbol, result):
    res = util.end_with(string, symbol)
    assert res == result


"""is_empty"""  

@pytest.mark.parametrize('string, result', [
    #POSITIVE:
    ("", True),
    (" ", True),
    ("  ", True),
    #NEGATIVE:
    ("tree", False),
    (" one", False),
    ("123", False),
    ("town ", False)   
])
def test_is_empty(string, result):
    res = util.is_empty(string)
    assert res == result

"""list_to_string"""    

@pytest.mark.parametrize('lst, joiner, result', [
    #POSITIVE:
    (["a", "b", "c"], ",", "a,b,c"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Юго", "Западный"], "-", "Юго-Западный"),
    (["Юго", "ветер"], "Западный", "ЮгоЗападныйветер"),
    #NEGATIVE:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = util.list_to_string(lst)
    else:
        res = util.list_to_string(lst, joiner)
    assert res == result