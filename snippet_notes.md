# Analytics Tracking 18F Projects
All 18F production sites should contain two analytics traking snippets; a [Digital Analytics Program](http://www.digitalgov.gov/services/dap/) snippet and a custom Google Analytics snippit.

## DAP Tracker


## 18F Tracker
The purpose of the 18F tracker snippet is to simplify/centralize analytics tracking and provide everyone within the organization access to all 18F projects' data. Additionally the snippet contains a few modifications to meet specific privacy and security standards.
Customizations
* [Anonymize IP](https://developers.google.com/analytics/devguides/collection/analyticsjs/field-reference#anonymizeIp)
* [Force SSL](https://developers.google.com/analytics/devguides/collection/analyticsjs/field-reference#forceSSL)

### UA Code
Message us on [g-analytics slack channel](https://18f.slack.com/messages/g-analytics/) and the Analytics Guild will give you a UA code linked to an account, which all 18F members can access.


### JavaScript Code Snippet
```javascript
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', '<<UA-CODE>>', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');
```

## To Process
* https://github.com/FCC/jQuery-and-Google-Analytics-Tools
