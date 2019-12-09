from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello world'

#TODO: handle the post request.
@app.route('/post/endpoint', methods=['POST'])
def test_endpoint():
	input_json = request.get_json(force=True)
	print ('data from client: ',input_json)
	dictToReturn = {'answer: ': 42}
	return jsonify(dictToReturn)

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1')