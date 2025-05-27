from lib.models.magazine import Magazine
import pytest
def test_magazine_can_be_found_by_id():
    mag = Magazine.find_by_id(1)
    assert mag.name == "Tech Trends"

def test_magazine_can_be_found_by_name():
    mag = Magazine.find_by_name("Wordsmith Weekly")
    assert mag is not None
    assert mag.category == "Literature"

def test_magazine_articles_returns_list():
    mag = Magazine.find_by_name("Tech Trends")
    articles = mag.articles()
    titles = [a["title"] for a in articles]
    assert "AI in the Modern Age" in titles

def test_magazine_contributors_returns_unique_authors():
    mag = Magazine.find_by_name("Tech Trends")
    names = [a["name"] for a in mag.contributors()]
    assert "John Stein" in names
    assert "Emily Rhodes" in names

def test_magazine_article_titles_returns_titles():
    mag = Magazine.find_by_name("Tech Trends")
    titles = mag.article_titles()
    assert "AI in the Modern Age" in titles

def test_contributing_authors_more_than_2_articles():
    mag = Magazine.find_by_name("Tech Trends")
    authors = mag.contributing_authors()
    for a in authors:
        assert a["article_count"] > 2
