from flask import Flask, render_template, url_for, request, session, redirect, g
import blockchain

app = Flask(__name__)



def sample_blockchain_setup():
    blockchain_app = blockchain.Blockchain()
    blockchain_app.new_transaction("Rajiv", "Tanush", '5 BTC')
    blockchain_app.new_transaction("Tanush", "Pradyumna", '1 BTC')
    blockchain_app.new_transaction("Pradyumna", "Rajiv", '7 BTC')
    blockchain_app.new_block()

    blockchain_app.new_transaction("Elon Musk", "Bill Gates", '100 BTC')
    blockchain_app.new_transaction("Bill Gates", "Jeff Bezos", '250 BTC')
    blockchain_app.new_transaction("Jeff Bezos", "Mark Zuckerberg", '720 BTC')
    blockchain_app.new_block()

    return blockchain_app.return_blockchain()

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', blockchain = sample_blockchain_setup())


if __name__ == '__main__':
    app.run(debug=True)