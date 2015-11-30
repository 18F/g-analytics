import os
from CloudFoundry import CloudFoundry

"""
A script for collecting CF URLs
### Quick Start
1. Set the following env variables
* CF_URL
* CF_USERNAME
* CF_PASSWORD
2. `python CFURLCollector.py`
"""


class CFURLCollector:
    def __init__(self):
        self.cf_api = CloudFoundry(
            url=os.getenv('CF_URL'),
            username=os.getenv('CF_USERNAME'),
            password=os.getenv('CF_PASSWORD'))
        self.domain_dict = {}

    def add_domain_to_list(self, domain, domain_url):
        """ Add new domains to dict so they don't have to be looked
        up again """
        self.domain_dict[domain_url] = domain

    def get_domain(self, domain_url):
        """ Get domain from Cloud Foundry """
        domain = self.domain_dict.get('domain_url')
        if not domain:
            response = self.cf_api.make_request(endpoint=domain_url).json()
            domain = response['entity']['name']
            self.add_domain_to_list(domain=domain, domain_url=domain_url)
        return domain

    def get_urls(self):
        """ Collect hosts and domains and combine them to make url """
        route_pager = self.cf_api.yield_request(endpoint='/v2/routes')
        for page in route_pager:
            for route in page['resources']:
                domain = self.get_domain(
                    domain_url=route['entity']['domain_url'])
                host = route['entity']['host']
                if host:
                    domain = host + "." + domain
                yield domain

if __name__ == "__main__":
    api = CFURLCollector()
    for url in api.get_urls():
        print(url)
