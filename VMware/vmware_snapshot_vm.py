# Import the required libraries
from vmware.vapi.vmc.client import create_vmc_client
import vmware.vcenter.vm.snapshot as vm_snapshot

# Connect to VMware Cloud on AWS using the VMC client
client = create_vmc_client(refresh_token=REFRESH_TOKEN,
                           org_id=ORG_ID,
                           sddc_id=SDDC_ID)

# Create a snapshot of the VM
vm_snapshot_service = vm_snapshot.Snapshot(client)
snapshot_task = vm_snapshot_service.create(vm_id=VM_ID, 
                                          name=SNAPSHOT_NAME, 
                                          description=SNAPSHOT_DESCRIPTION, 
                                          memory=True, 
                                          quiesce=True)
client.vcenter.Task.wait_for_completion(snapshot_task)
