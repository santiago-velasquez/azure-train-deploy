from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

ws = Workspace.from_config(path='./.azureml', _file_name='config.json')

experiment = Experiment(workspace=ws, name='test_remote_ws')

config = ScriptRunConfig(source_directory='./src', script='test-remote.py', compute_target='cluster02ml')

run = experiment.submit(config)

aml_url = run.get_portal_url()

print(f'Vínculo al experimento: {aml_url}')