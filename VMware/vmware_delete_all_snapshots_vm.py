# Import the required libraries
from vmware.vapi.vmc.client import create_vmc_client
import vmware.vcenter.vm.snapshot as vm_snapshot

# Connect to VMware Cloud on AWS using the VMC client
client = create_vmc_client(refresh_token=REFRESH_TOKEN,
                           org_id=ORG_ID,
                           sddc_id=SDDC_ID)

# Get a list of all the snapshots of the VM
vm_snapshot_service = vm_snapshot.Snapshot(client)
snapshot_list = vm_snapshot_service.list(vm_id=VM_ID)

# Delete all the snapshots
for snapshot in snapshot_list:
    delete_task = vm_snapshot_service.delete(snapshot.id)
    client.vcenter.Task.wait_for_completion(delete_task)
