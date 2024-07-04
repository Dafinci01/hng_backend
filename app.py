from flask import Flask, request, jsonify

from waitress import serve

app = Flask(__name__)


@app.route("/api/hello")

def hello():
    visitor_name = request.args.get("visitor_name")
    if not visitor_name:
        visitor_name = input("please enter your name:")
    #to get requester's IP address (consider security)
    client_ip = request.remote_addr

    #retrieve the requesters  location
    reader = geoip2.database.reader('home/user/Downloads/Geolite2-City.mmdb')
    response = reader.city(client_ip)

    location = response.city.name


    greeting = f"Hello,{visitor_name}!. the temp 9is ... celsius in {location}"

    response =  {"client_ip": client_ip, "location": location, "greeting":greeting}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
    serve(app, host="0.0.0.0", port=5000)

    #to access api/hello /api/hello route and see the response, modify the URL in browser to http://127.0.0.1:5000/api/hello?visitor_name=david
