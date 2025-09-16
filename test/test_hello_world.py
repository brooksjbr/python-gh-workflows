from src.hello_world import print_msg


def test_hello_world():
    msg = "Hello World!"
    result = print_msg(msg)

    assert result == "Your message is Hello World!"
