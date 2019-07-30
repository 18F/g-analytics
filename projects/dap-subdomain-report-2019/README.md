
## Goals

* Assemble a relatively complete list of federal subdomains from open source information.  


## Process

Steps:  
1) Download the [complete HTTPS scan results from pulse.cio.gov](https://pulse.cio.gov/data/hosts/https.json).  
2) Convert it to a CSV.  I used http://www.convertcsv.com/json-to-csv.htm.  
3) Upload the resulting CSV to Google Spreadsheets.  ([link](https://docs.google.com/spreadsheets/d/1MFgrAG-wYfctH_NYdZ71JkVZUQm6Bm5TYCrhurTM4xw/edit#gid=32666482)) _(25,491 results)_
4) Remove unneeded columns
5) Reorient columns for convenience
6) Add Filtering
8) Remove items that match ignore list 
  a) Add a column of numbers to make later resorting easier
  b) Sort domain alphabetically
  c) Remove exact subdomains (label:ignore1; 1659 results); remove close matches (label:ignore2; results)




...
ideas for further to remove: 
local
auth


still lots more of:
dev 
edit
email
extranet
