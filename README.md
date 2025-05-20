📚 Book Scraper Project

This is a web scraping project built with Scrapy that extracts book data (like title, price, availability, and rating) from the website books.toscrape.com. The extracted data can be stored in a JSON file or saved directly into a SQLite database.
🚀 Project Structure

book_scraper_project/
│
├── bookscraper/
│   ├── spiders/
│   │   └── book_spider.py      # Main spider for scraping
│   ├── __init__.py
│   ├── items.py                # Defines the data structure
│   ├── middlewares.py
│   ├── pipelines.py            # Optional: For saving to SQLite
│   ├── settings.py             # Project settings
│
├── scrapy.cfg                  # Scrapy project configuration
├── books.json                  # Output (if saving as JSON)
├── books.db                    # Output (if saving to SQLite)
└── README.md                   # Project documentation

🛠 Features

    Scrapes book title, price, availability, and rating

    Saves data to:

        books.json (JSON file)

        or books.db (SQLite database)

    Easily extendable to scrape more fields

⚙️ How to Run
1. Clone the Project

git clone https://github.com/your-username/book_scraper_project.git
cd book_scraper_project

2. Install Dependencies

pip install scrapy

3. Run the Spider and Save to JSON

scrapy crawl bookspider -o books.json

4. (Optional) Run the Spider and Save to SQLite

Make sure pipelines.py is configured and enabled in settings.py, then run:

scrapy crawl bookspider

💾 Sample Output (JSON)

[
  {
    "title": "A Light in the Attic",
    "price": "£51.77",
    "availability": "In stock",
    "rating": "Three"
  },
  ...
]

🧱 Technologies Used

    Python 3

    Scrapy

    SQLite 

    JSON

✍️ Author

Abubakar Salimon
Data Scientist & Web Scraper
