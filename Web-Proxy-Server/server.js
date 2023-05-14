const express = require('express')
const NodeCache = require( "node-cache" );
const fs = require('fs');
const { exec } = require("child_process");
const cache = new NodeCache();
const app = express();
const port = 9000;
const routes = express.Router()
let blockList = "";
function isBlockedURL(url){
    return blockList.some(blockedUrl => url.includes(blockedUrl));
}
// read the blocked list file
fs.readFile('blockList.txt', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    blockList = data.split("\n").filter(Boolean);;
  });
app.use("/public", express.static("public"));
routes.get('/',(req,res)=>{
    //get site request header
    site=req.query['site']
    console.log(site)
    // check if site is blocked
    if(isBlockedURL(site)){
        console.log("This site is blocked");
        res.sendFile(__dirname + `/public/blockedSite.html`);
    // else check if site is in cache then directly load from there
    }else if(cache.get(site)){
        console.log("in cache")
        res.sendFile(__dirname + `/public/${site}/index.html`);
    // else if not in cache, download the whole site first then open it and add it in cache
    }else{
        console.log(site,"not in cache")
        // -np => Do not ascend to the parent directory when downloading recursive files
        // -N => time-stamping , only download new files
        // -k => convert all links to absoulute URLs  in the downloaded files to allow offline browsing
        // -p => download all necessary files
        // -nd => do not create a heirarchy of directories
        // -nH => do not create a hostname directory, no need to name the directory after the remote server
        // -H => enable spanning accross hosts for recursive retrieving (if site uses other webpages for data download all that too)
        // -E => add an html extension to the downloaded html files
        // --no-check-certificate => Do not verify the SSL/TLS certificate when downloading HTTPS pages
        // -e robots=off => Ignore the robots.txt file that specifies which pages can be downloaded by web crawlers
        // -U 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36' => specify a user agent for searching
        // --directory-prefix=public/${site} => Set the download directory to public/${site}, where ${site} is the name of the website being downloaded
        // --reject js => reject all js files
        // --accept html,css => accept only html and css files
        let wget=exec(`wget -np -N -k -p -nd -nH -H -E --no-check-certificate -e robots=off -U 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36' --directory-prefix=public/${site} --reject js --accept html,css ${site}`, (error, stdout, stderr) => {
            if (error) {
                console.log(error.stack);
                console.log('Error code: ' + error.code);
                console.log('Signal received: ' + error.signal);
              }
              console.log('Child Process STDOUT: ' + stdout);
              console.log('Child Process STDERR: ' + stderr);
        });
        // once wget request is done, load the webpage
        wget.on('exit',function (code) {
            console.log('Child process exited with exit code ' + code);
            success = cache.set( site, true, 10000 );
            res.sendFile(__dirname + `/public/${site}/index.html`);
        });
    }
})
app.use(routes);
app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
  });