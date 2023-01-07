# Import the required libraries
from vmware.vapi.vmc.client import create_vmc_client
import vmware.vcenter.vm.power as vm_power
import vmware.vcenter.vm.hardware.boot as vm_boot

# Connect to VMware Cloud on AWS using the VMC client
client = create_vmc_client(refresh_token=REFRESH_TOKEN,
                           org_id=ORG_ID,
                           sddc_id=SDDC_ID)

# Get a list of all the VM IDs in the SDDC
vm_service = client.vcenter.VM
vm_list = vm_service.list()

# Power on the first VM in the list
vm_id = vm_list[0].vm
vm_power_service = vm_power.Power(client)
vm_power_service.start(vm_id)

# Change the boot order for the first VM so that it boots from the CD-ROM
vm_boot_service = vm_boot.Boot(client)
vm_boot_order = vm_boot_service.get(vm_id)
vm_boot_order.cd = vm_boot_order.disk
vm_boot_service.update(vm_id, vm_boot_order)
