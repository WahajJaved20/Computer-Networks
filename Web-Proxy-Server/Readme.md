# Problem Statement

In this assignment, you will implement a web proxy that passes requests and data between
multiple web clients and web servers, concurrently (fork a process for each new client request).
When you&#39;re done with the assignment, you should be able to configure your web browser to
use your personal proxy server as a web proxy that is capable of handling the following tasks.
1. HTTP communications between client and server.
2. HTTPs communications between client and server.
3. Caching of popular content using at least two scheduling algorithms.
4. Content filtering (filtering rules should be configurable via admin console).

# How to Run
write npm in terminal in case you dont have node installed
then run "npm install"
then run "npm run dev"
and goto "localhost:9000/?site='www.example.com'"
you can check the blocked sites and add one of your on a new line then restart the server and query the site to see the blocked html
