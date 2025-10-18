from ._anvil_designer import OOB_MgmtTemplate
from anvil import *
import anvil.js  # Import the anvil.js module

class OOB_Mgmt(OOB_MgmtTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.output_card.visible = True

    oob_ip = self.ip_address.text
    oob_subnet = self.subnet_mask.text
    oob_gateway = self.default_gateway.text

    self.output_text.text = f"""
    dhcp-client client mgmtbr0 admin-enable false
    oc-if:interfaces interface mgmtbr0 ipv4 addresses address { oob_ip } config ip { oob_ip } prefix-length {oob_subnet}
    rib vrf default ipv4 0.0.0.0/0 next-hop { oob_gateway }
    """

  def copy_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Use anvil.js to call the browser's Clipboard API.
    #    This is a JavaScript function being called directly from Python.
    anvil.js.window.navigator.clipboard.writeText(self.output_text.text)

    # (Optional) Provide feedback to the user.
    self.copy_button.text = "Copied! 👍"
