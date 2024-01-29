

def test_login_wellworld(py, login):
    assert py.should().contain_title("Well World | Home")
