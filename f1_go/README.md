## UDP client and UDP client + websocket

### To Run the UDP Client

Create a new project in your go path and copy the structs folder and udp_client.go. Don't forget to also have the structs.go file inside the structs folder as well.

```
go run udp_client.go
```

### To run the UDP client + websocket

To see images of webpage, see static folder!

Create a new project in your go path and copy the following items like such inside your gopath projects area:

```
[folder] *Project_Name*
    -> [folder] static
        -> [folder] css
            -> telemetry_dashboard.css

        -> [folder] js
            -> telemetry_dashboard.js

        -> telemetry_dashboard.html


    -> [folder] structs
        -> structs.go


    -> go_websocket_server.go
```

Now once the files are now in your go path, we also need gorilla.

To do this, run "go get" pointing to a gorilla package. We only use two gorilla packages, websocket and mux.

For gorilla/websocket:

```
$ go get github.com/gorilla/websocket
```

For gorilla/mux:

```
$ go get github.com/gorilla/mux
```
