#!/usr/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/ciscoios/")
def ciscoios():
    try:
        qparms = {}
        # user passes switchname= or default "bootstrapped switch"
        qparms['switchname']  = request.args.get('switchname', 'bootstrapped switch')
        # user passes username= or default "admin"
        qparms['username']  = request.args.get('username', 'admin')
        # user passes gateway= or default "0.0.0.0"
        qparms['defaultgateway'] = request.args.get('gateway', '0.0.0.0')
        # user passes ip= or default "0.0.0.0"
        qparms['switchIP'] = request.args.get('ip', '0.0.0.0')
        # user passes mask= or default "255.255.255.0"
        qparms['netmask'] = request.args.get('mask', '255.255.255.0')
        # user passes mtu= or default '1450'
        qparms['mtusize'] = request.args.get('mtu', '1450')

        # render template and save as baseIOS.conf
        return render_template("baseIOS.conf.j2", **qparms)

    except Exception as err:
        return "Uh-oh! " + err

if __name__ == "__main__":
    app.run(port=5006)
