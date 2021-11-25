
from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(tenant_id="99e1e721-7184-498e-8aff-b2ad4e53c1c2")
ws = Workspace.create(name='ml_sv_02',
            subscription_id='fbc9534c-aff1-4cbd-9099-93af17036380',
            resource_group='GR_ESPUDEA_SV_01',
            create_resource_group=False,
            location='eastus2',
            auth=interactive_auth
            )
            
# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')