import http.server
import socketserver

"""
-A web server is a process that listens to incoming requests on specific TCP address.

-TCP address is identified by an ip address and a port number

-A web server also needs to be told how to handle incoming requests
"""

PORT = 8080

"""
A web server needs to be told how to handle incoming requests.
These incoming requests are handled by special handlers.
You can think of a web server as a dispatcher, a request comes in,
the http server inspects the request and dispatches it to a designated handler.
These handlers can do anything you desire.
But what do you think the most basic handler is?
That would be a handler that just serves a static file.
In other words, when we go to yahoo.com,
the web server at the other end sends back a static html file.

That is what [http.server.SimpleHTTPRequestHandler] is:
a simple HTTP request handler that servers files from the current directory
and any of its subdirectories.
"""
Handler = http.server.SimpleHTTPRequestHandler
"""
An instance of TCPServer describes a server that uses the TCP protocol
to send and receive messages [http is an application layer protocol on top of TCP].

Two Things are needed to instantiate a TCP Server:

1.The TCP address [IP
address and a port number]

2.The handler


Passing an empty string as the IP address means that the server
will be listening on any network interface [all available IP addresses]

Since PORT stores the value 8080,
then the server will be listening on
incoming requests on that port.
"""

with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever() 

