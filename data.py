import sqlite3

conn = sqlite3.connect("websites.db")

c = conn.cursor()

# c.execute("""CREATE TABLE website (
#             name test,
#             website text,
#             priceAsc text,
#             priceDes text
#             )""")

# c.execute("INSERT INTO website VALUES ('New World', 'https://www.ishopnewworld.co.nz/Search?q=', '&s=sortprice&sd=0','&s=sortprice&sd=1')")
c.execute("SELECT * FROM website WHERE name ='New world'")

print(c.fetchone())


conn.commit()

conn.close()
