from pytest import mark

ddt = {
    'argnames': 'name, description',
    'argvalues': [('hello', 'world'),
        ('hello', ''),
        ('123', 'world')],
    'ids': ['general', 'test with no description', 'test with digits in name']
}

@mark.parametrize(**ddt)
def test_new_testcase(desktop_app_auth, name, description):
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test case')
    assert desktop_app_auth.test_cases.check_test_exists(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)

def test_testcases_does_not_exist(desktop_app_auth):
    desktop_app_auth.navigate_to('Test Cases')
    assert not desktop_app_auth.test_cases.check_test_exists('sdasdfhsfdhjksldfkfs')



#def test_new_testcase_no_descr(desktop_app_auth):
#   test_name = 'hello'
#    desktop_app_auth.navigate_to('Create new test')
#    desktop_app_auth.create_test(test_name='world')
#    desktop_app_auth.navigate_to('Test case')
#    assert desktop_app_auth.test_cases.check_test_exists(test_name)
#    desktop_app_auth.test_cases.delete_test_by_name(test_name)


#def test_new_testcase_digits_name(desktop_app_auth):
#    test_name = '123'
#    desktop_app_auth.navigate_to('Create new test')
#    desktop_app_auth.create_test(test_name='world')
#    desktop_app_auth.navigate_to('Test case')
#    assert desktop_app_auth.test_cases.check_test_exists(test_name)
#    desktop_app_auth.test_cases.delete_test_by_name(test_name)