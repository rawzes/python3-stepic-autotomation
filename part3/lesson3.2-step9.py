string = 'My name is Roma'

#  'in' checks substing in string. returns True \ False
if 'name' in string:
    print('string is found')


#  string.find() - returns index of substring in string, or returns -1 if not found
index = string.find('name2')
if index == -1:
    print('required string is not found')


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f'expected \'{substring}\' to be substring of \'{full_string}\''


test_substring('test', 'est')
test_substring('home sweet home', 'test')
