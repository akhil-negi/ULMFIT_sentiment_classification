# ULMFIT_Sentiment_classification

## USAGE:
<ul><li>$ git clone https://github.com/akhil-negi/ULMFIT_Sentiment_classification.git</li>
  <li>$ cd ULMFIT_sentiment_classification</li>
  <li>$ sudo docker build -t ubuntu18_fastai .</li>
  <li>$ sudo docker run -it -p 8889:8889 --name sentiment ubuntu18_fastai</li>
  <li>Launch the browser and navigate to http://0.0.0.0:8889/</li></ul>
  
## SUMMARY:
<ul><li>The classifier uses <a href="https://arxiv.org/abs/1801.06146" target="_blank">ULMFIT</a>. Which is an approach to use transfer learning in NLP.</li>
  <li>Dataset used : <a href='https://www.kaggle.com/forums/f/3497/pre-processed-twitter-tweets'>Preprocessed tweets from Kaggle</a></li>
  <li>Use test data (data/test-train-datatest/test.csv) for testing the classifier.</li>
  <li>Classes: 0= Negative, 1=Positive, 2=Neutral</li></ul>
