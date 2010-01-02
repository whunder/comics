from comics.aggregator.crawler import CrawlerBase, CrawlerResult
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Deep Fried'
    language = 'en'
    url = 'http://www.whatisdeepfried.com/'
    start_date = '2001-09-16'
    rights = 'Jason Yungbluth'

class Crawler(CrawlerBase):
    history_capable_days = 14
    schedule = 'Mo,Tu,We,Th,Fr,Sa'
    time_zone = -5

    def crawl(self, pub_date):
        feed = self.parse_feed('http://www.whatisdeepfried.com/feed/')
        for entry in feed.for_date(pub_date):
            url = entry.summary.src('img')
            title = entry.title
            return CrawlerResult(url, title)