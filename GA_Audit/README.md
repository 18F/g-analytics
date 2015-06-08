A scripts that collects urls from Cloud Foundry and extracts the version of GA running along with the UA code.

## Installation
##### Install Python requirements
```bash
pip install -r requirements.txt
```
##### Install PhantomJS Headless Browser
Mac with brew
```bash
brew install phantomjs
```

## Usage
Set the following env variables
```bash
export CF_URL="18f.gov"
export CF_USERNAME="CF username"
export CF_PASSWORD="CF password"
```
#### Example script

```
import logging

from CFURLCollector import CFURLCollector
from GAChecker import GAChecker

def audit():
    """ Check with sites have GA  """
    collector = CFURLCollector()
    url_iterator = collector.get_urls()
    auditor = GAChecker()
    audit_dict = {}
    for url in url_iterator:
        status = auditor.check_for_ga("http://" + url)
        audit_dict[url] = status
        logging.info("%s--%s", url, status)
    auditor.quit_browser()
    return audit_dict


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(audit())
```


