This is a simple iris flower classification model deployment project as flask app.

You can deploy this model/app on Openshift just using git project url with OpenShift build menu.

You can deploy the model/app as single docker container as well as on Kubernetes. 

This project is build and pushed to Dockerhub you can directly use the image if you want  
`  docker run --rm -d -p 8080:8080 erkansirin78/flask-iris-classification:2021-3 `

Input web ui:

![Input web ui](images/input_form.png "Input web ui")

Predictions:

![Predictions](images/prediction_result.png "Predictions")