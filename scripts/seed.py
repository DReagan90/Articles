import sqlite3

conn = sqlite3.connect('articles.db')
cursor = conn.cursor()

# Clear existing data
cursor.execute("DELETE FROM articles")
cursor.execute("DELETE FROM authors")
cursor.execute("DELETE FROM magazines")

# Insert authors
cursor.execute("INSERT INTO authors (id, name) VALUES (?, ?)", (1, "John Stein"))
cursor.execute("INSERT INTO authors (id, name) VALUES (?, ?)", (2, "Emily Rhodes"))
cursor.execute("INSERT INTO authors (id, name) VALUES (?, ?)", (3, "David Lin"))

# Insert magazines
cursor.execute("INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)", (1, "Tech Trends", "Technology"))
cursor.execute("INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)", (2, "Wordsmith Weekly", "Literature"))

# Insert articles
cursor.execute("INSERT INTO articles (id, title, author_id, magazine_id) VALUES (?, ?, ?, ?)",
               (1, "AI in the Modern Age", 1, 1))
cursor.execute("INSERT INTO articles (id, title, author_id, magazine_id) VALUES (?, ?, ?, ?)",
               (2, "The Art of Poetry", 2, 2))
cursor.execute("INSERT INTO articles (id, title, author_id, magazine_id) VALUES (?, ?, ?, ?)",
               (3, "Cybersecurity Essentials", 3, 1))
cursor.execute("INSERT INTO articles (id, title, author_id, magazine_id) VALUES (?, ?, ?, ?)",
               (4, "Poetry in Tech", 2, 1))

conn.commit()
conn.close()
