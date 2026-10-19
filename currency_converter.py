def converter(usd_val):
    inr_val=86*usd_val
    print(f"{usd_val}$={inr_val} INR")

y=int(input("Enter the number of dollars: "))   
converter(y)

