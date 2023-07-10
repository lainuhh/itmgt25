
def savings(gross_pay, tax_rate, expenses):
    # Deduct tax rate
    gross_pay = (gross_pay * (1 - tax_rate)) // 1
    # Subtract expenses
    gross_pay -= expenses
    return int(gross_pay)


def material_waste(total_material, material_units, num_jobs, job_consumption):
    material_consumed = num_jobs * job_consumption
    waste = total_material - material_consumed
    return f"{waste}{material_units}"


def interest(principal, rate, periods):
    simple_interest = principal * rate * periods
    return int(principal + simple_interest)


def body_mass_index(weight, height):
    kg = weight * 0.453592
    m = ((height[0] * 12) + height[1]) * 0.0254
    return kg / (m * m)