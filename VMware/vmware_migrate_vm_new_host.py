# Import the required libraries
from vmware.vapi.vmc.client import create_vmc_client
import vmware.vcenter.vm.relocate as vm_relocate

# Connect to VMware Cloud on AWS using the VMC client
client = create_vmc_client(refresh_token=REFRESH_TOKEN,
                           org_id=ORG_ID,
                           sddc_id=SDDC_ID)

# Check if the VM is powered off
vm_service = client.vcenter.VM
vm_info = vm_service.get(vm_id=VM_ID)
if vm_info.power_state != "POWERED_OFF":
    raise Exception("Cannot migrate powered on VM")

# Migrate the VM to the new host
vm_relocate_service = vm_relocate.Relocate(client)
relocate_spec = vm_relocate_service.create_spec(host=NEW_HOST_ID, 
                                                 datastore=NEW_DATASTORE_ID)
relocate_task = vm_relocate_service.relocate(vm_id=VM_ID, spec=relocate_spec)
client.vcenter.Task.wait_for_completion(relocate_task)
