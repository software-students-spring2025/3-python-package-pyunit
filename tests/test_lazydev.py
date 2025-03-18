import pytest
from lazydev.lazydev import lazy_commit_message, lazy_test_excuse

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

#test if the function returns string 
def test_excuse_is_not_empty():
    excuse=lazy_test_excuse()
    assert isinstance(excuse,str),"Excuse should be string"

#checks if the reason input is embedded 
def test_excuse_reason():
    reason="My dog ate my code"
    excuse=lazy_test_excuse(reason)
    assert reason in excuse, f"'{reason} should be in the {excuse}'"
# This is to make sure the reason and excuse is grammatically in checl
def test_structured_sentence():
    excuse=lazy_test_excuse()
    assert excuse,"Excuse should not be empty"
    assert excuse[0].isupper(),f"Excuse should start with a capital letter: {excuse}"
    assert excuse[-1] in {".", "!"}