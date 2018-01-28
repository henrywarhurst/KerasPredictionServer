# KerasPredictionServer
A simple Flask web server that performs image classification using Keras

# Setup
```
FLASK_APP=server.py
flask run
```

# Making requests to the server
At the moment, the server is only configured to handle POST requests. 

To post an image to the server:
```
curl -X POST -F "image=@./cat.jpeg" http://127.0.0.1:50/predict
```

# Understanding the output

The server returns a number representing the ImageNet class of the image that you POSTed to it.

See https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a to find out the human readable version of the classifaction returned by the POST request.
