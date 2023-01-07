# Import the required libraries
from vmware.vapi.vmc.client import create_vmc_client
import vmware.vcenter.vm.template.convert as vm_template_convert

# Connect to VMware Cloud on AWS using the VMC client
client = create_vmc_client(refresh_token=REFRESH_TOKEN,
                           org_id=ORG_ID,
                           sddc_id=SDDC_ID)

# Convert the VM to a template
vm_template_convert_service = vm_template_convert.TemplateConvert(client)
convert_task = vm_template_convert_service.convert(vm_id=VM_ID)
client.vcenter.Task.wait_for_completion(convert_task)
