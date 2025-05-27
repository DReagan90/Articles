from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Example queries for demonstration

def authors_with_article_counts():
    conn = get_connection()
    with conn:
        rows = conn.execute('''
            SELECT authors.name, COUNT(articles.id) as article_count
            FROM authors
            LEFT JOIN articles ON authors.id = articles.author_id
            GROUP BY authors.id
        ''').fetchall()
    for row in rows:
        print(f"Author: {row['name']}, Articles: {row['article_count']}")

def magazines_with_multiple_authors():
    conn = get_connection()
    with conn:
        rows = conn.execute('''
            SELECT magazines.name, COUNT(DISTINCT articles.author_id) as author_count
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            GROUP BY magazines.id
            HAVING author_count >= 2
        ''').fetchall()
    for row in rows:
        print(f"Magazine: {row['name']}, Unique Authors: {row['author_count']}")

def main():
    print("Authors with article counts:")
    authors_with_article_counts()
    print("\nMagazines with articles by at least 2 authors:")
    magazines_with_multiple_authors()

if __name__ == "__main__":
    main()