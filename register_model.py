from azureml.core import Workspace
from azureml.core import Model

if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')

    model = Model.register(model_name='model_diabetes',
                           tags={'area': 'udea_training'},
                           model_path='models/rf1.pkl',
                           workspace = ws)
    print(model.name, model.id, model.version, sep='\t')