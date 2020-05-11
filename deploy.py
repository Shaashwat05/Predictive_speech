from watson_machine_learning_client import WatsonMachineLearningAPIClient
from contextlib import suppress
import os
import pickle

wml_credentials={
  "url": "xxxxxxxxxxxxxxxxxx",
  "apikey": "xxxxxxxxxxxxxxxxxxxxxxx",
  "username": "xxxxxxxxxxxxxxxxxxxx",
  "password": "xxxxxxxxxxxxxxxxxxxxxxx",
  "instance_id": "xxxxxxxxxxxxxxxxxxxxxx"
}


client = WatsonMachineLearningAPIClient(wml_credentials)

#compressing model
filename = 'weights/model.hdf5'
tar_filename = 'weights/model.hdf5' + '.tgz'
cmdstring = 'tar -zcvf ' + tar_filename + ' ' + filename
os.system(cmdstring)



model_props = {
    client.repository.ModelMetaNames.NAME: 'Speech - compressed keras model',
    client.repository.ModelMetaNames.FRAMEWORK_NAME: 'tensorflow',
    client.repository.ModelMetaNames.FRAMEWORK_VERSION: '1.14.0',
    client.repository.ModelMetaNames.RUNTIME_NAME: 'python',
    client.repository.ModelMetaNames.RUNTIME_VERSION: '3.7.5',
    client.repository.ModelMetaNames.FRAMEWORK_LIBRARIES: [{'name':'keras', 'version': '2.3.1'}]
}

published_model_details = client.repository.store_model(model=tar_filename, meta_props=model_props)       

model_uid = client.repository.get_model_uid(published_model_details)
print(model_uid)



deployment = client.deployments.create(model_uid, 'Keras MNIST model deployment through compressed file.')

dp = open("variables/deployment.pkl", 'wb')
pickle.dump(dp, deployment)
dp.close()

