# Import the required libraries
from vmware.vapi.vmc.client import create_vmc_client
import vmware.vcenter.vm.power as vm_power

# Connect to VMware Cloud on AWS using the VMC client
client = create_vmc_client(refresh_token=REFRESH_TOKEN,
                           org_id=ORG_ID,
                           sddc_id=SDDC_ID)

# Monitor the power state of the VM
vm_power_service = vm_power.Power(client)
while True:
    power_state = vm_power_service.get(vm_id=VM_ID).state
    print(f"Current power state: {power_state}")
    time.sleep(30)
