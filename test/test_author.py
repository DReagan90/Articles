from lib.models.author import Author
from lib.models.magazine import Magazine
import pytest
def test_author_can_be_found_by_id():
    author = Author.find_by_id(1)
    assert author.name == "John Stein"

def test_author_can_be_found_by_name():
    author = Author.find_by_name("Emily Rhodes")
    assert author is not None
    assert author.name == "Emily Rhodes"

def test_author_articles_returns_correct_titles():
    author = Author.find_by_name("Emily Rhodes")
    titles = [article["title"] for article in author.articles()]
    assert "The Art of Poetry" in titles

def test_author_magazines_returns_unique_magazines():
    author = Author.find_by_name("Emily Rhodes")
    mags = author.magazines()
    names = set(m['name'] for m in mags)
    assert "Wordsmith Weekly" in names
    assert "Tech Trends" in names

def test_author_can_add_article():
    author = Author.find_by_name("David Lin")
    mag = Magazine.find_by_name("Wordsmith Weekly")
    author.add_article(magazine=mag, title="New Horizons in Writing")
    titles = [a['title'] for a in author.articles()]
    assert "New Horizons in Writing" in titles

def test_author_topic_areas():
    author = Author.find_by_name("Emily Rhodes")
    topics = author.topic_areas()
    assert "Literature" in topics
    assert "Technology" in topics
