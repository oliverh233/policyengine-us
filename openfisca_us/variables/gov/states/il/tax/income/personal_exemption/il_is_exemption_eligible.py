from openfisca_us.model_api import *


class il_is_exemption_eligible(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Whether this tax unit is eligible for any exemptions"
    unit = USD
    definition_period = YEAR
    reference = ""
    defined_for = StateCode.IL

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.il.tax.income.exemption.cap
        filing_status = tax_unit("filing_status", period)

        return tax_unit("adjusted_gross_income", period) < p[filing_status]
