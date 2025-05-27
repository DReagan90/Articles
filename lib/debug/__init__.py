from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Load an author
alice = Author.find_by_id(1)
print(f"Author: {alice.name}")

# Get articles by Alice
print("\nArticles by Alice:")
for a in alice.articles():
    print(f"- {a['title']}")

# Get magazines Alice wrote for
print("\nMagazines Alice contributed to:")
for m in alice.magazines():
    print(f"- {m['name']} ({m['category']})")

# Add a new article
mag = Magazine.find_by_id(1)
alice.add_article(magazine=mag, title="Time Travel and Tech")

# Check topic areas
print("\nAlice's topic areas:")
print(alice.topic_areas())

# Check contributors to a magazine
mag2 = Magazine.find_by_id(2)
print(f"\nContributors to {mag2.name}:")
for author in mag2.contributors():
    print(f"- {author['name']}")

# Contributing authors (more than 2 articles)
print(f"\nFrequent contributors to {mag2.name}:")
for author in mag2.contributing_authors():
    print(f"- {author['name']} (articles: {author['article_count']})")

# Article titles in Science Today
print("\nArticle titles in Science Today:")
science = Magazine.find_by_id(1)
print(science.article_titles())
