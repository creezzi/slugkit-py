import pytest

from slugkit import slugify, unique_slug


@pytest.mark.parametrize("text,slug", [
    ("Hello, World!", "hello-world"),
    ("Crème Brûlée & Friends!", "creme-brulee-friends"),
    ("  --Already--slugged--  ", "already-slugged"),
    ("Straße Œuvre", "strasse-oeuvre"),
    ("under_score and CamelCase", "under-score-and-camelcase"),
    ("日本語", ""),
    ("", ""),
])
def test_slugify(text, slug):
    assert slugify(text) == slug


def test_custom_separator():
    assert slugify("a b c", separator="_") == "a_b_c"


def test_max_length_cuts_on_word_boundary():
    assert slugify("the quick brown fox", max_length=12) == "the-quick"
    assert slugify("supercalifragilistic", max_length=5) == "super"


def test_unique_slug():
    assert unique_slug("post", set()) == "post"
    assert unique_slug("post", {"post"}) == "post-2"
    assert unique_slug("post", {"post", "post-2", "post-3"}) == "post-4"
