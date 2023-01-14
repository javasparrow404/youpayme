#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, send_file, render_template, request

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, template_folder='views')

# Set the app secret key from the secret environment variables.
# app.secret = os.environ.get('SECRET')


# @app.route('/qr/<id>/<amount>/<name>/<note>')
# def serve_qr(id, amount, name, note):
#     return send_file(create_qr(id, amount, name, note), mimetype='image/png')


# def create_qr(id, amount=None, name=None, note=None):
#     upi_id = id
#     # for production
#     save_dir = tempfile.gettempdir()
#     # for local testing
#     # save_dir = 'save'
#     if amount:
#         try:
#             amount = round(float(amount), 2)
#             url = f"upi://pay?pn={name}&pa={upi_id}&cu=INR&am={amount}&tn={note}"
#         except Exception:
#             amount = None
#             url = f"upi://pay?pn={name}&pa={upi_id}&cu=INR&tn={note}"
#     else:
#         url = f"upi://pay?pn={name}&pa={upi_id}&cu=INR&tn={note}"

#     version, level, qr_name = myqr.run(
#         url,
#         version=1,
#         level='H',
#         picture="logo.jpg",
#         colorized=False,
#         contrast=1.0,
#         brightness=1.0,
#         save_name=id+"_qr.png",
#         save_dir=save_dir
#     )
#     return save_dir + "/" + id+"_qr.png"


@app.route('/pay')
def payment():
    name = request.args.get('pn')
    upi_id = request.args.get('pa')
    amount = request.args.get('am')
    amount = round(float(amount), 2)
    note = "youpayme" if request.args.get(
        'tn') is None else request.args.get('tn')
    return render_template('home.html', name=name, id=upi_id, amount=amount, note=note)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/logo')
def logo():
    # serve the logo file
    return send_file('logo.jpg', mimetype='image/png')

# @app.route('/<id>/<amount>')
# def amount_payment(id, amount):
#     if '@' in id:
#         """Displays the QR and Payment Info."""
#         try:
#             amount = round(float(amount), 2)
#         except Exception:
#             amount = None
#         return render_template('home.html', id=id, amount=amount)
#     else:
#         return render_template("create.html", id=id, amount=amount)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
