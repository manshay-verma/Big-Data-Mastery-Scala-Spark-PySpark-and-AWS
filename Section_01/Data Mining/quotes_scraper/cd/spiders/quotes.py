import scrapy
## We do this already but that time 
# we use it on scrapy and 
# it help to more multiple functionality and do many more things 
# 31.07.2025

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield{
                "text":quote.css("span.text::text").get(),
                "author":quote.css("small.author::text").get(),
                "tag":quote.css("div.tags a.tag::text").getall()
            }
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page,self.parse)