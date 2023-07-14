from policyengine_us.model_api import *


class dc_self_employment_loss_addition(Variable):
    value_type = float
    entity = Person
    label = "DC excess self-employment loss addition"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/52926_D-40_12.21.21_Final_Rev011122.pdf#page=63"
        "https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2022_D-40_Booklet_Final_blk_01_23_23_Ordc.pdf#page=55"
    )
    defined_for = StateCode.DC

    def formula(person, period, parameters):
        return 0
