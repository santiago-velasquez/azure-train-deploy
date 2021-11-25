from azureml.core import Workspace
ws = Workspace.from_config(path='./.azureml',_file_name='config.json')
datastore = ws.get_default_datastore()
datastore.upload(src_dir='./data',
                 target_path='data',
                 overwrite=True)