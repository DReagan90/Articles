from lib.models.article import Article
import pytest
def test_article_can_be_found_by_id():
    article = Article.find_by_id(1)
    assert article.title == "AI in the Modern Age"

def test_article_can_be_found_by_title():
    article = Article.find_by_title("The Art of Poetry")
    assert article is not None

def test_article_has_author_and_magazine():
    article = Article.find_by_title("Cybersecurity Essentials")
    assert article.author_id is not None
    assert article.magazine_id is not None
