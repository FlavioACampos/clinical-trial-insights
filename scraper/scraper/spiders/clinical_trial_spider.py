import scrapy


class ClinicalTrialSpiderSpider(scrapy.Spider):
    name = "clinical_trial_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        yield {"True?": True}
