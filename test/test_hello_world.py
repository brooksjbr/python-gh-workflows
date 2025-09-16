from src.hello_world import msg


def test_hello_world():
    my_msg = "Hello World!"
    result = msg(my_msg)

    assert result == "Your message is Hello World!"
