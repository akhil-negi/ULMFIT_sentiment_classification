from flask import Flask, request,jsonify,render_template #import main Flask class and request object
from ulmfit_classifier import * 


app = Flask(__name__)

@app.route('/')
#def api_root():
#    return 'Welcome'
@app.route('/')
@app.route('/')
def index():
   return render_template('index.html')


@app.route('/api/sentiment_analysis', methods=['POST'])
def translate_query():
#     content = request.get_json()
#     print(type(content))
#     print(content['text'])
    inpt=request.get_json()
    print(inpt['text'])
    clf=ulmfit_classifier()
    sentiment=clf.predict(inpt)
    print(sentiment)
    response={"Sentiment":sentiment}
    return jsonify(response)
    #return translate(content)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=8889)    
