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

filename = 'weights/model.h5'
tar_filename = 'weights/model' + '.tgz'
cmdstring = 'tar -zcvf ' + tar_filename + ' ' + filename
os.system(cmdstring)





model_props = {
    client.repository.ModelMetaNames.NAME: 'Speech - compressed keras model',
    client.repository.ModelMetaNames.FRAMEWORK_NAME: 'tensorflow',
    client.repository.ModelMetaNames.FRAMEWORK_VERSION: '1.15',
    client.repository.ModelMetaNames.RUNTIME_NAME: 'python',
    client.repository.ModelMetaNames.RUNTIME_VERSION: '3.6',
    client.repository.ModelMetaNames.FRAMEWORK_LIBRARIES: [{'name':'keras', 'version': '2.2.5'}]
}

published_model_details = client.repository.store_model(model='model.tgz', meta_props=model_props)       

model_uid = client.repository.get_model_uid(published_model_details)
print(model_uid)



deployment = client.deployments.create(model_uid, 'Keras Speech recognition through compressed file.')

dp = open("variables/deployment.pkl", 'wb')
pickle.dump(dp, deployment)
dp.close()

