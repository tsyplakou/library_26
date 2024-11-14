genres_data = [
    {"name": "Science Fiction", "description": "Fiction dealing with futuristic settings, advanced technology, and space exploration."},
    {"name": "Fantasy", "description": "Fiction set in an imaginary universe, often inspired by real-world myth and folklore."},
    {"name": "Mystery", "description": "Fiction revolving around the investigation of a crime or unraveling secrets."},
    {"name": "Historical", "description": "Fiction set in a particular historical period, often based on true events."},
    {"name": "Biography", "description": "A detailed description of a person's life."},
    {"name": "Romance", "description": "Fiction dealing with love and romantic relationships."},
    {"name": "Thriller", "description": "Fiction that creates excitement and suspense."},
    {"name": "Horror", "description": "Fiction intended to scare, unsettle, or horrify the reader."},
    {"name": "Non-Fiction", "description": "Informative and factual works based on real events and people."},
    {"name": "Philosophy", "description": "Works that explore fundamental questions about existence, knowledge, and ethics."},
]

authors_data = [
    {"first_name": "Isaac", "last_name": "Asimov", "birth_year": 1920, "death_year": 1992},
    {"first_name": "J.K.", "last_name": "Rowling", "birth_year": 1965, "death_year": None},
    {"first_name": "Agatha", "last_name": "Christie", "birth_year": 1890, "death_year": 1976},
    {"first_name": "Leo", "last_name": "Tolstoy", "birth_year": 1828, "death_year": 1910},
    {"first_name": "Walter", "last_name": "Isaacson", "birth_year": 1952, "death_year": None},
    {"first_name": "George", "last_name": "Orwell", "birth_year": 1903, "death_year": 1950},
    {"first_name": "Mary", "last_name": "Shelley", "birth_year": 1797, "death_year": 1851},
    {"first_name": "Jane", "last_name": "Austen", "birth_year": 1775, "death_year": 1817},
    {"first_name": "Stephen", "last_name": "King", "birth_year": 1947, "death_year": None},
    {"first_name": "Friedrich", "last_name": "Nietzsche", "birth_year": 1844, "death_year": 1900},
]

books_data = [
    {"title": "Foundation", "release_date": "1951-01-01", "genre": "Science Fiction", "author": "Isaac Asimov"},
    {"title": "Harry Potter and the Philosopher's Stone", "release_date": "1997-06-26", "genre": "Fantasy", "author": "J.K. Rowling"},
    {"title": "Murder on the Orient Express", "release_date": "1934-01-01", "genre": "Mystery", "author": "Agatha Christie"},
    {"title": "War and Peace", "release_date": "1869-01-01", "genre": "Historical", "author": "Leo Tolstoy"},
    {"title": "Steve Jobs", "release_date": "2011-10-24", "genre": "Biography", "author": "Walter Isaacson"},
    {"title": "1984", "release_date": "1949-06-08", "genre": "Science Fiction", "author": "George Orwell"},
    {"title": "Frankenstein", "release_date": "1818-01-01", "genre": "Horror", "author": "Mary Shelley"},
    {"title": "Pride and Prejudice", "release_date": "1813-01-28", "genre": "Romance", "author": "Jane Austen"},
    {"title": "The Shining", "release_date": "1977-01-28", "genre": "Horror", "author": "Stephen King"},
    {"title": "Thus Spoke Zarathustra", "release_date": "1883-01-01", "genre": "Philosophy", "author": "Friedrich Nietzsche"},
    {"title": "The Catcher in the Rye", "release_date": "1951-07-16", "genre": "Fiction", "author": "J.D. Salinger"},
    {"title": "Brave New World", "release_date": "1932-01-01", "genre": "Science Fiction", "author": "Aldous Huxley"},
    {"title": "The Great Gatsby", "release_date": "1925-04-10", "genre": "Historical", "author": "F. Scott Fitzgerald"},
    {"title": "To Kill a Mockingbird", "release_date": "1960-07-11", "genre": "Fiction", "author": "Harper Lee"},
    {"title": "Crime and Punishment", "release_date": "1866-01-01", "genre": "Mystery", "author": "Fyodor Dostoevsky"},
    {"title": "A Brief History of Time", "release_date": "1988-01-01", "genre": "Non-Fiction", "author": "Stephen Hawking"},
    {"title": "The Art of War", "release_date": "500 BC", "genre": "Philosophy", "author": "Sun Tzu"},
    {"title": "The Hobbit", "release_date": "1937-09-21", "genre": "Fantasy", "author": "J.R.R. Tolkien"},
    {"title": "Anna Karenina", "release_date": "1877-01-01", "genre": "Historical", "author": "Leo Tolstoy"},
    {"title": "The Divine Comedy", "release_date": "1320-01-01", "genre": "Philosophy", "author": "Dante Alighieri"},
]

translators_data = [
    {"first_name": "Constance", "last_name": "Garnett", "birth_year": 1861, "death_year": 1946},
    {"first_name": "Pevear", "last_name": "Richard", "birth_year": 1943, "death_year": None},
    {"first_name": "Larissa", "last_name": "Volokhonsky", "birth_year": 1945, "death_year": None},
    {"first_name": "Michael", "last_name": "Glenny", "birth_year": 1927, "death_year": 1990},
    {"first_name": "Louise", "last_name": "Maude", "birth_year": 1855, "death_year": 1939},
    {"first_name": "Aylmer", "last_name": "Maude", "birth_year": 1858, "death_year": 1938},
    {"first_name": "David", "last_name": "McDuff", "birth_year": 1945, "death_year": None},
    {"first_name": "Alan", "last_name": "Myers", "birth_year": 1933, "death_year": 2010},
    {"first_name": "Ann", "last_name": "Dunnigan", "birth_year": 1910, "death_year": 1997},
    {"first_name": "Rosamund", "last_name": "Bartlett", "birth_year": 1961, "death_year": None},
    {"first_name": "Anthony", "last_name": "Briggs", "birth_year": 1932, "death_year": None},
    {"first_name": "Peter", "last_name": "Carson", "birth_year": 1938, "death_year": 2013},
    {"first_name": "Andrew", "last_name": "Bromfield", "birth_year": 1948, "death_year": None},
    {"first_name": "Marian", "last_name": "Schwartz", "birth_year": 1954, "death_year": None},
    {"first_name": "Richard", "last_name": "Freeborn", "birth_year": 1926, "death_year": 2010},
]
