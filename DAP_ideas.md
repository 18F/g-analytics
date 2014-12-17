Three main areas need further fleshing out: tracking the implementation of the DAP program across the .gov web presence, sharing the data more broadly across government, and beginning to carefully publish the data publicly.  Some next steps include:


## Tracking Implementation
* modify the .gov domain tracker to include whether the DAP code is present 
* Pull from the DAP data what subdomains and domains are registering.  
  * Also pull number of URLs showing up for each of those subdomains/domains.  
* Engage with OGP to try and find some number of subdomains that we could integrate into a variant of the .gov domain tracker that is focused on tracking implementation. 
* Consider a crowdsourced gathering of subdomains, complemented with potential google dives.  (a la [this query](https://www.google.com/search?q=site%3A*.*.gov+-inurl%3Awww&oq=site%3A*.*.gov+-inurl%3Awww&gs_l=serp.3...5617.5689.0.5863.2.2.0.0.0.1.118.201.1j1.2.0....0...1c.1.52.serp..2.0.0.h24hcvZzS0k))
* Use the site crawler app to spider every .gov homepage, save the source code, and derive a list of all urls to assemble a list of subdomains.  

## Sharing
* Create a series of optional mailing lists, such as: 
  * general gov't wide report, weekly and monthly - automated
  * a monthly report, custom-built that highlights particularly interesting occurances 
  * Other custom reports (what?)

## Publishing
* Decide on a hub to begin sharing general data with the public (perhaps usa.gov/analytics), host it in GSA's GitHub, and begin building out material there.  Candidates for initial material would be:  
  * Status numbers of agencies using DAP, domains participating, pages harvested, gov't users, etc.  
  * Publish the gov't wide aggregate numbers (site visitors, locations, browser/os).  Could be static at first then change to automated widget.  
* Create embeddable widgets for some of the above charts.  

## Material
* https://www.youtube.com/watch?v=90mhs1ENdCo&feature=youtu.be
* 

## Other To Do 
* Enable GSA users to access the Google Developer Console so as to be able to hit the api. 
* Integrate collaborators: charles w., eric m., leah b., gabriel r.
