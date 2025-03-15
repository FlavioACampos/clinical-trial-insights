import traceback
import json

from scrapy import Spider, Request
from datetime import datetime, timedelta
from urllib.parse import urlencode
from box import Box


class ClinicalTrialSpiderSpider(Spider):
    name = "clinical_trial_spider"
    allowed_domains = ["clinicaltrials.gov"]

    def __init__(self):
        yesterday = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
        self.params = {
            "pageSize": str(200),
            "sort": "StudyFirstPostDate",
            "countTotal": "true",
            "filter.advanced": f"AREA[LastUpdatePostDate]{yesterday}",
        }

    def start_requests(self):
        url = f"https://clinicaltrials.gov/api/v2/studies?{urlencode(self.params)}"
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
        item["scrape_status"] = "Failed"
        item["scrape_details"]["exception"] = err
        self.logger.error(err)
        return item

    def scrape_study(self, study):
        # Study Item
        item = {}
        try:
            study = Box(study, default_box=True, default_value=None)
            # Protocol Section
            id_module = study.protocolSection.identificationModule
            item["nct_number"] = id_module.nctId
            item["study_title"] = id_module.officialTitle
            item["organization"] = id_module.organization.fullName
        except Exception as ex:
            item = self.set_error_message(item, ex)
        finally:
            yield item

    def scrape(self, data, item):
        try:
            if not data.get("studies"):
                self.logger.warning("No studies found!")
            for study in data.get("studies", []):
                yield from self.scrape_study(study)
        except Exception as ex:
            item = self.set_error_message(item, ex)
        finally:
            yield item

    def parse(self, response):
        """Parse API response."""
        # Scraping Page Item
        item = {"scrape_status": "OK", "scrape_details": {}, "scrape_url": response.url}
        try:
            data = json.loads(response.text)
            item["total_count"] = data.get("totalCount")
            # TODO: current page
            # TODO: total pages
            if not item.get("total_count"):
                self.logger.warning("No records found!")
            yield from self.scrape(data, item)
        except Exception as ex:
            item = self.set_error_message(item, ex)
            yield item
