import pytest
from lazydev.lazydev import lazy_commit_message, lazy_pull_request

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

#Tests for lazy_pull_request
#Ensures words are in pr title when given
def test_pr_words_given():
    verb = "test verb"
    noun = "test noun"
    message = lazy_pull_request(verb,noun)
    assert verb in message, f"'{verb}' not in '{message}'"
    assert noun in message, f"'{verb}' not in '{message}'"
    assert isinstance(message, str), "message needs to be a string"

#Ensures output is formatted properly with only given verb input 
def test_pr_verb_given():
    verb = "test verb"
    message = lazy_pull_request(verb)
    assert verb in message, f"'{verb}' not in '{message}'"
    assert message, "there should be a message"
    assert isinstance(message, str), "message needs to be a string"

#Ensures output is formatted properly with only given verb input 
def test_pr_noun_given():
    noun = "test noun"
    message = lazy_pull_request(inputNoun=noun)
    assert noun in message, f"'{noun}' not in '{message}'"
    assert message, "there should be a message"
    assert isinstance(message, str), "message needs to be a string"

#Ensures the message is not the same each time without given arguments
def test_pr_random():
    message1 = lazy_pull_request()
    message2 = lazy_pull_request()
    assert message1 != message2, "messages should be different each time"