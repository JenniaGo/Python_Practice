# Deploy a VM from a template
# Import the required libraries
from vmware.vapi.vmc.client import create_vmc_client
import vmware.vcenter.vm.template.deploy as vm_template_deploy
import vmware.vcenter.vm.hardware.disk as vm_disk
import vmware.vcenter.vm.hardware.nic as vm_nic

# Connect to VMware Cloud on AWS using the VMC client
client = create_vmc_client(refresh_token=REFRESH_TOKEN,
                           org_id=ORG_ID,
                           sddc_id=SDDC_ID)

# Create the VM disk specification
vm_disk_service = vm_disk.Disk(client)
vm_disk_spec = vm_disk_service.create_spec(new_vmdk(size=10))

# Create the VM NIC specification
vm_nic_service = vm_nic.Nic(client)
vm_nic_spec = vm_nic_service.create_spec(network=NETWORK_ID)

# Deploy the VM from the template
vm_template_deploy_service = vm_template_deploy.TemplateDeploy(client)
deploy_spec = vm_template_deploy_service.create_spec(name=VM_NAME,
                                          folder=FOLDER_ID, 
                                          resource_pool=RESOURCE_POOL_ID, 
                                          datastore=DATASTORE_ID,
                                          disks=[vm_disk_spec],
                                          nics=[vm_nic_spec])
deploy_task = vm_template_deploy_service.deploy(template_id=TEMPLATE_ID,
                                          spec=deploy_spec)
client.vcenter.Task.wait_for_completion(deploy_task)
