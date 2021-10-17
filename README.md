This is a simple iris flower classification model deployment project as flask app.

## Build an image (Dockerize) and run on Docker container
- Download project
` git clone https://github.com/erkansirin78/flask-iris-classification.git ` 

` cd flask-iris-classification `

- Build image 
` docker image build -t my_flask_iris:1.0 . ` 

- Run container 
` docker run --rm --name flask_iris -p 8082:8080 -d my_flask_iris:1.0 ` 

- Open browser http://localhost:8082/

Enjoy your predictions.

## Directly run on Docker without building
This project is build and pushed to Dockerhub you can directly use the image if you want

`  docker run --rm -d -p 8080:8080 erkansirin78/flask-iris-classification:2021-3 `


## On Kubernetes
- You can deploy the model/app on Kubernetes with deployment object.

- You can deploy this model/app on Openshift just using git project url with OpenShift build menu.

Input web ui:

![Input web ui](images/input_form.png "Input web ui")

Predictions:

![Predictions](images/prediction_result.png "Predictions")
