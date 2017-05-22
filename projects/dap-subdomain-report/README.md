
## Goals

* Assemble a relatively complete list of federal subdomains from open source information.  
* Use it to estimate the extent of Digital analytics Program (DAP) implementation and provide a list of subdomains that agencies can target for further implementation.  

## Background 

A number of my colleagues here at GSA and at DHS have done a tremendous job of [tracking implementation of HTTPS by federal agencies](https://18f.gsa.gov/2017/01/04/tracking-the-us-governments-progress-on-moving-https/), per [OMB Memo 15-13](https://obamawhitehouse.archives.gov/sites/default/files/omb/memoranda/2015/m-15-13.pdf).  As part of this work, they have assembled [a number of open source datasets](https://github.com/GSA/https/tree/master/compliance/data) that can be combined to provide a fairly complete list of subdomains across the federal government.  

While these datasets are being used to assist agencies in implementing HTTPS across their web presence, they have not yet been used to map implementation of the [Digital Analytics Program](https://www.digitalgov.gov/services/dap/).  [OMB Memo 17-06](https://obamawhitehouse.archives.gov/sites/default/files/omb/memoranda/2017/m-17-06.pdf) now requires all Executive Branch websites to fully implement DAP on their public websites.  This project attempts to assist agencies in this effort.  

## Process

Steps:  
1) Download the [2016 end of term export](https://github.com/GSA/https/blob/master/compliance/data/eot-2016.csv) _([direct download](https://raw.githubusercontent.com/GSA/https/master/compliance/data/eot-2016.csv))_, [12-31-16 censys export](https://github.com/GSA/https/blob/master/compliance/data/censys-2016-12-31.csv) _([direct download](https://raw.githubusercontent.com/GSA/https/master/compliance/data/censys-2016-12-31.csv))_, [12-31-16 Digital Analytics Program export](https://github.com/GSA/https/blob/master/compliance/data/dap-2016-12-31.csv) _([direct download](https://raw.githubusercontent.com/GSA/https/master/compliance/data/dap-2016-12-31.csv))_, and [12-31-16 HTTPS report export](https://github.com/GSA/https/blob/master/compliance/data/parents-2016-12-31.csv) _([direct download](https://raw.githubusercontent.com/GSA/https/master/compliance/data/parents-2016-12-31.csv))_.  
2) Combine them all.  _([93430 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/1-initial-combined-subdomain-list.csv))_  _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/1-initial-combined-subdomain-list.csv))_  
3) Remove the inactive domains.  _([39908 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/2-combined-subdomain-list-minus-inactive-URLs.csv))_  _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/2-combined-subdomain-list-minus-inactive-URLs.csv))_  
4) Remove the redirecting domains.  _([34961 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/3-combined-subdomain-list-minus-inactive-or-redirecting-URLs.csv))_  _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/3-combined-subdomain-list-minus-inactive-or-redirecting-URLs.csv))_  
5) Dedup the list.  _([25377 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/4-combined-subdomain-list-minus-inactive-or-redirecting-URLs-dedupped.csv))_  _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/4-combined-subdomain-list-minus-inactive-or-redirecting-URLs-dedupped.csv))_  
6) Add `Agency` and `Branch` columns.  _([25377 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/5-subdomain-list-with-agencies-federal.csv))_ _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/5-subdomain-list-with-agencies-federal.csv))_   
6.1) With the [ignore list](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/assets/ignore-list.md) removed.  _([23,781 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/5.1-subdomain-list-with-agencies-federal-filtered.csv))_  _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/5.1-subdomain-list-with-agencies-federal-filtered.csv))_  
7) Remove other branches.  _([22053 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/6-subdomain-list-with-agencies-executive.csv))_    _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/6-subdomain-list-with-agencies-executive.csv))_  
7.1) With the [ignore list](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/assets/ignore-list.md) removed.  _([20,520 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/6.1-subdomain-list-with-agencies-executive-filtered.csv))_   _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/6.1-subdomain-list-with-agencies-executive-filtered.csv))_  
8) Compare against the DAP participants list.  _([22053 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/7-subdomain-list-with-agencies-executive-DAP.csv))_  _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/7-subdomain-list-with-agencies-executive-DAP.csv))_  
8.1) With the [ignore list](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/assets/ignore-list.md) removed.  _([20,520 results](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/7.1-subdomain-list-with-agencies-executive-DAP-filtered.csv))_    _([raw](https://github.com/18F/g-analytics/raw/18f-pages/projects/dap-subdomain-report/7.1-subdomain-list-with-agencies-executive-DAP-filtered.csv))_  
  
_Caveats:  For practical purposes, the subdomain list is a snapshot from 12-31-16 and their active/inactive and redirecting statuses are also from scans that took place at that time.  Since then, some on this list may have become inactive and new ones may have been registered.  That said, this will hopefully provide a clearer view at agency-, domain-, and branch-wide implementation of the Digital Analytics Program._  

_For step 4, this step relies on automated scans to detect redirects.  Some sites that use client-side redirect methods may not be detected as redirecting.  
  
_For steps 6.1, 7.1, and 8.1 - an '[ignore list](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/assets/ignore-list.md)' was used to filter out subdomains that are not intended for public use, such as login pages, staging sites, and mail servers.  It's not feasible to completely filter out all subdomains that are not intended for public use though we will continue to refine the model.  If you have strings to suggest be added to the ignore list, please share them in the feedback links below._

## Results 

* [List of Active, Non-Redirecting Subdomains for the Federal Government](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/5.1-subdomain-list-with-agencies-federal-filtered.csv)
* [List of Active, Non-Redirecting Subdomains for the Executive Branch with their DAP implementation status](https://github.com/18F/g-analytics/blob/18f-pages/projects/dap-subdomain-report/7.1-subdomain-list-with-agencies-executive-DAP-filtered.csv)

## Feedback

* Feel free to [file an issue](https://github.com/18F/g-analytics/issues) with any thoughts or questions.  
* If you have advice on filtering methods for removing subdomains for non-websites like staging/webmail/etc, please share them [in this issue](https://github.com/18F/g-analytics/issues/30).  
