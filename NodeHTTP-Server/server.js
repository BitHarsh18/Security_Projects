const http = require("http");

const HOST = "127.0.0.1";
const PORT = 3000;

const server = http.createServer((req, res) => {
    console.log("----- Incoming Request -----");
    console.log("Method:", req.method);
    console.log("URL:", req.url);
    console.log("Headers:", req.headers);

    if (req.method === "GET") {
        if (req.url === "/") {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end("<h1>Welcome to Node HTTP Server</h1>");
        } 
        else if (req.url === "/about") {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end("<h1>About Page</h1><p>Built using Node.js core module.</p>");
        } 
        else {
            res.writeHead(404, { "Content-Type": "text/html" });
            res.end("<h1>404 Not Found</h1>");
        }
    } 
    else {
        res.writeHead(405, { "Content-Type": "text/html" });
        res.end("<h1>Method Not Allowed</h1>");
    }
});

server.listen(PORT, HOST, () => {
    console.log(`🚀 Server running at http://${HOST}:${PORT}`);
});