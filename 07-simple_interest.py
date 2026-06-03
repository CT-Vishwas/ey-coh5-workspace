def simple_interest(principal, time_in_months, rate_of_interest):
    return (principal * time_in_months * rate_of_interest)/100


principal = 3_00_000
times_in_months = [36,24,12]
rates_of_interest = [0.07,0.64,0.25,0.56]
for rate in rates_of_interest:
    for months in times_in_months:
        interest = simple_interest(principal, months, rate)
        print(f"The amount: {principal}, at {rate} earns Rs.{interest} for {months} months")