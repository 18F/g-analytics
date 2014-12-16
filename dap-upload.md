## Hosting the DAP Snippet

Where `dap-1.0.js` is the current, unminified version of the DAP UA snippet.

### Minifying

Generate a minified version of the snippet, and an accompanying [source map](https://developer.chrome.com/devtools/docs/javascript-debugging#source-maps), using [`uglifyjs`](http://lisperator.net/uglifyjs/).

Install `uglifyjs` through `npm` (which comes with [Node](http://nodejs.org)):

```bash
npm install -g uglifyjs
```

Then run it, specifying the source map:

```bash
uglifyjs dap-1.0.js --source-map=dap-1.0.min.js.map > dap-1.0.min.js
```

This gives you three files: `dap-1.0.js`, `dap-1.0.min.js` (minified), and `dap-1.0.min.js.map` (source map).

### Compressing

Most file servers will automatically bake compression (gzip) into the process, automatically compressing them as needed (this is called [compression scheme negotiation](https://en.wikipedia.org/wiki/HTTP_compression#Compression_scheme_negotiation)). Amazon S3 **does not do this**, so we need to compress the files ourselves.

Create a compressed (gzipped) version of all 3 files:

```bash
gzip -c dap-1.0.min.js > dap-1.0.min.js.gz
gzip -c dap-1.0.min.js.map > dap-1.0.min.js.map.gz
gzip -c dap-1.0.js > dap-1.0.js.gz
```

### Uploading

Upload each gzipped file to an Amazon S3 bucket, using [`s3cmd`](https://github.com/s3tools/s3cmd). The below commands instruct Amazon S3 to serve files as JavaScript, and to mark their encoding as `gzip`, so that browsers will know to automatically unzip the files before reading them. 

* Note that **the files are renamed upon upload** to remove the `.gz` suffix.
* Note that the **version number is dropped** so that the file can be upgraded in place.

```
s3cmd put -P --mime-type="application/javascript" --add-header="Content-Encoding: gzip" dap-1.0.js.gz s3://18f-dap/dap.js
s3cmd put -P --mime-type="application/javascript" --add-header="Content-Encoding: gzip" dap-1.0.min.js.gz s3://18f-dap/dap.min.js
s3cmd put -P --mime-type="application/javascript" --add-header="Content-Encoding: gzip" dap-1.0.min.js.map.gz s3://18f-dap/dap.min.js.map
```

This bucket has been published at `https://dvs6mwdoj87wa.cloudfront.net`. (HTTPS only - `http://` links will not redirect.)

Use the following URL to import the DAP into your site:

* https://dvs6mwdoj87wa.cloudfront.net/dap.min.js
