# Import the required libraries
from vmware.vapi.vmc.client import create_vmc_client
import vmware.vcenter.vm.clone as vm_clone

# Connect to VMware Cloud on AWS using the VMC client
client = create_vmc_client(refresh_token=REFRESH_TOKEN,
                           org_id=ORG_ID,
                           sddc_id=SDDC_ID)

# Clone the VM
vm_clone_service = vm_clone.Clone(client)
clone_spec = vm_clone_service.create_spec(folder=FOLDER_ID, 
                                          host=HOST_ID, 
                                          datastore=DATASTORE_ID, 
                                          name=CLONE_NAME)
clone_task = vm_clone_service.clone(vm_id=VM_ID, spec=clone_spec)
client.vcenter.Task.wait_for_completion(clone_task)
