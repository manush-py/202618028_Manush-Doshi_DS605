import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        # FIX: Force the correct encoding to bypass the Windows lxml bug
        response = response.replace(encoding='utf-8')
        
        books = response.css('article.product_pod')
        
        for book in books:
            relative_url = book.css('h3 a::attr(href)').get()
            book_url = response.urljoin(relative_url)
            yield scrapy.Request(url=book_url, callback=self.parse_book)

        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page:
            next_page_url = response.urljoin(next_page)
            page_num = int(next_page_url.split('page-')[1].split('.html')[0])
            if page_num <= 5:
                yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_book(self, response):
        # FIX: Force the correct encoding here as well
        response = response.replace(encoding='utf-8')
        
        title = response.css('div.product_main h1::text').get()
        category = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
        price = response.css('p.price_color::text').get()
        
        rating_class = response.css('p.star-rating::attr(class)').get()
        rating = rating_class.split(' ')[1] if rating_class else None
        
        availability = response.css('p.availability').xpath('normalize-space()').get()
        description = response.xpath('//div[@id="product_description"]/following-sibling::p/text()').get()
        upc = response.xpath('//th[text()="UPC"]/following-sibling::td/text()').get()
        reviews = response.xpath('//th[text()="Number of reviews"]/following-sibling::td/text()').get()

        yield {
            'title': title,
            'category': category,
            'price': price,
            'rating': rating,
            'availability': availability,
            'description': description,
            'upc': upc,
            'reviews': reviews,
            'url': response.url
        }