from flask import Flask , request , jsonify
import requests
from googlesearch import search 
app = Flask(__name__)

@app.route('/',methods=['GET'])
def API():
	pages={}
	query=str(request.args['Query'])
	pages_count=1
	for page in search(query, tld="co.in", num=10, stop=10, pause=2):
		pages[pages_count]=page;	
		pages_count=pages_count+1

	return jsonify(pages)

if __name__ == '__main__':
    app.run()
