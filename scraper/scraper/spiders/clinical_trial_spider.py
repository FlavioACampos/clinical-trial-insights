import traceback
import json

from scrapy import Spider, Request
from datetime import datetime, timedelta
from urllib.parse import urlencode


class ClinicalTrialSpiderSpider(Spider):
    name = "clinical_trial_spider"
    allowed_domains = ["clinicaltrials.gov"]

    def start_requests(self):
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        params = {
            "pageSize": "200",
            "sort": "StudyFirstPostDate",
            "countTotal": "true",
            "filter.advanced": f"AREA[LastUpdatePostDate]{yesterday}",
        }
        url = f"https://clinicaltrials.gov/api/v2/studies?{urlencode(params)}"
        yield Request(
            method="GET",
            url=url,
            headers={},
            callback=self.parse,
            dont_filter=True,
        )

    def set_error_message(self, item, ex):
        """Formats error messages."""
        err = f"Failed: {type(ex).__name__}: {ex} | {traceback.format_exc().strip().splitlines()[-1]}"
        item["Status"] = "Failed"
        item["ScrapeDetails"]["Exception"] = err
        self.logger.error(err)
        return item

    def parse(self, response):
        """Parse API response."""
        item = {"Status": "OK", "Details": {}}
        try:
            data = json.loads(response.text)
            item["totalCount"] = data.get("totalCount")
        except Exception as ex:
            item = self.set_error_message(item, ex)
        finally:
            yield item
