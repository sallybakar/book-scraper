import scrapy
import sqlite3  # <-- Import sqlite3

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['https://books.toscrape.com/']

    def open_spider(self, spider):
        # Runs once when spider starts
        self.conn = sqlite3.connect('books.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                price TEXT,
                availability TEXT,
                url TEXT
            )
        ''')
        self.conn.commit()

    def close_spider(self, spider):
        # Runs once when spider closes
        self.conn.close()

    def parse(self, response):
        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            availability = book.css('p.in_stock.availability::text').get().strip()
            url = response.urljoin(book.css('h3 a::attr(href)').get())

            # Insert into database
            self.c.execute(
                "INSERT INTO books (title, price, availability, url) VALUES (?, ?, ?, ?)",
                (title, price, availability, url)
            )
            self.conn.commit()

            yield {
                'title': title,
                'price': price,
                'availability': availability,
                'url': url
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)