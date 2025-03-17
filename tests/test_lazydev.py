import pytest
from lazydev.lazydev import lazy_commit_message

#Tests for lazy_commit_message
#Ensures Keyword is in the commit message when added
def test_commit_keyword():
    keyword = "keyword"
    message = lazy_commit_message(keyword)
    assert keyword in message, f"'{keyword}' not in '{message}'"
    assert isinstance(message, str), "message needs to be a string"

#Ensures output is formatted properly when there is no keyword
def test_commit_no_keyword():
    message = lazy_commit_message()
    assert message, "there should be a message"
    assert not message.startswith(":"), "the colon shouldnt appear if no keyword"
    assert isinstance(message, str), "message needs to be a string"

#Ensures the message is not the same each time
def test_commit_message_random():
    message1 = lazy_commit_message("keyword")
    message2 = lazy_commit_message("keyword")
    assert message1 != message2, "messages should be different each time"