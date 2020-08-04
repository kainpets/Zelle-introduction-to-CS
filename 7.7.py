# Program to compute the babysitter's wage expenses

def main():
    sh = int(input("Enter the hour babysitting begun: "))
    sm = int(input("Enter the minute babysitting begun: "))
    eh = int(input("Enter the hour babysitting ended: "))
    em = int(input("Enter the minute babysitting ended: "))

    # in case the work goes on after midnight
    if eh < sh:
        eh = eh + 24
    
    work_time = (eh * 60 + em) - (sh * 60 + sm)
    
    if eh >= 21:
        work_time_over_21 = (eh - 21) * 60 + em
        payment = (work_time - work_time_over_21) * 2.5 / 60 +\
        (work_time_over_21 / 60 * 1.75)
    else: 
        payment = work_time / 60 * 2,5

    print("You will be payed (amount rounded) ", round(payment, 2))
    
main()
