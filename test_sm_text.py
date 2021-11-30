from sm_text import *
input_for_test="Testing @text #this does work #stuff; @things"
checkval = sm_text(input_for_test)


def test_clean_sm_text():
    assert sm_text.clean_sm_text(checkval) == [
        "testing",
        "@text",
        "#this",
        "does",
        "work",
        "#stuff",
        "@things",
    ]


def test_extract_hashtags():
    assert sm_text.extract_hashtags(checkval) == ["#this", "#stuff"]


def test_extract_at_tags():
    assert sm_text.extract_at_tags(checkval) == ["@text", "@things"]
