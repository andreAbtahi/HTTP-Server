# HTTP-Server (source: ruslanpivak.com)

## Web Address
    - It is called a URL
        - The basic structure of a URL is this:
            - [http://][localhost:][8888][/hello]
            - 1st: we have the HTTP protocol
            - 2nd: we have the host name
            - 3rd: we have the port
            - 4th: we have the path name
            
        - This is how you tell a browser the address of the web
            server it needs to find and conect to and the page(path)
                on the server to fetch for you.
        
        - Before a browser can send the address/HTTP request, it first
            needs to establish a TCP connection with the Web Server.
            
        - Once TCP connection is established, it then sends an HTTP request over
            the TCP connection to the server and waits for the server to send an
                HTTP request back.
        
        -When browser recieves the response it displays it, in the case of
            webserver1.py it displays a "Hello, Word!"
            
        
# How client and server establish a TCP connection before sending HTTP requests and responses.

    -To do that they both use so-called sockets
    


                
