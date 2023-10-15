import sqlite3

# funkcija za kreiranje tabele Books u SQLite bazi podataka sa parametrom za konekciju
def create_table(conn):
    query = '''
    CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        year INTEGER
    )
    '''
    conn.execute(query)    # izvrsava se SQL upit za kreiranje tabele
    conn.commit()          # promene se potvrdjuju naredbom commit()

# funkcija za dodavanje knjige u bazu
def insert_book(conn, title, year):
    query = 'INSERT INTO Books (title, year) VALUES (?, ?)'
    conn.execute(query, (title, year))
    conn.commit()

# funkcija za dobijanje svih knjiga iz baze
def get_all_books(conn):
    query = 'SELECT * FROM Books'
    cursor = conn.execute(query)
    return cursor.fetchall()

if __name__ == '__main__':
    conn = sqlite3.connect('books.db')  # konektovanje sa bazom ili kreiranje nove ako ne postoji
    create_table(conn)                  # poziv funkcije za kreiranje tabele

    while True:              # beskonacna petlja - kod se izvrsava dok korisnik ne unese podatke
        choice = input('''                            
        Choose an option:
          1 *** Add Book
          2 *** Show Books
          3 *** Exit
        Enter your choice: ''')

        if choice == '1':
            print("\n   Adding a New Book:")
            title = input('   Enter the title: ')
            year = input('   Enter the year: ')
            insert_book(conn, title, year)  # poziv funkcije za dodavanje knjige
        elif choice == '2':
            print("\n   Listing All Books:")
            books = get_all_books(conn)     # Poziv funkcije za dobijanje svih knjiga
            if not books:
                print("   No books found.")
            else:
                for book in books:
                    print(f"   ID: {book[0]}, Title: {book[1]}, Year: {book[2]}")
        elif choice == '3':
            conn.close()  # Zatvaranje veze sa bazom
            break
