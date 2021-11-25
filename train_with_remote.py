from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig
from azureml.core import Dataset

if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')
    datastore = ws.get_default_datastore()
    dataset = Dataset.File.from_files(path=(datastore, 'data'))

    experiment = Experiment(workspace=ws, name='remote_training_01')

    config = ScriptRunConfig(
        source_directory='./src',
        script='generate_model.py',
        compute_target='cluster02ml',
        arguments=[
            '--data_path', dataset.as_named_input('input').as_mount()],
    )
    # set up pytorch environment
    env = Environment.from_conda_specification(
        name='sklearn_basic',
        file_path='./.azureml/env-ml-esp.yml'
    )
    config.run_config.environment = env

    run = experiment.submit(config)
    aml_url = run.get_portal_url()
    print("Experimento de entrenamiento corriendo. Siga el link:")
    print("")
    print(aml_url)