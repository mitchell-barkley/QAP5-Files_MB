# Program Description: One Stop Insurance Company
# Written By: Mitchell Barkley
# Written On: July 19th 2023

# Libraries
import FormatValues as FV
import datetime
CurrentDate = datetime.datetime.now()
from calendar import monthrange
from tqdm import tqdm
import time

# Constants

# Functions
def NewPolicyCreator():
    while True:
        print("================================================================================")
        print("                          ONE STOP INSURANCE COMPANY")
        print("================================================================================")
        print("NEW POLICY CREATOR")
        print("Please enter the following information: ")
        print()
        while True:
            CustFirst = input("Customer's First Name: ").title()
            if CustFirst == "":
                print("Error - Customer First Name can not be blank.")
            else:
                break

        while True:
            CustLast = input("Customer's Last Name: ").title()
            if CustLast == "":
                print("Error - Customer Last Name can not be blank.")
            else:
                break
        FullName = CustFirst + " " + CustLast

        while True:
            CustStreet = input("Customer's Street Address: ").title()
            if CustStreet == "":
                print("Error - Customer Street Address can not be blank.")
            else:
                break

        while True:
            CustCity = input("Customer's City: ").title()
            if CustCity == "":
                print("Error - Customer City can not be blank.")
            else:
                break

        while True:
            Prov_Set = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
            CustProv = input("Customer's Province (NL): ").upper()
            if CustProv == "":
                print("Error - Customer Province can not be blank.")
            elif not CustProv.upper() in Prov_Set:
                print("Error - Province entered is not valid.")
            else:
                break

        while True:
            CustPostal = input("Customer's Postal Code (A1A1A1): ").upper()
            if CustPostal == "":
                print("Error - Customer Postal Code can not be blank.")
            elif len(CustPostal) != 6:
                print("Error - Incorrect number of characters - Please use A1A1A1 format.")
            elif CustPostal[0].isdigit():
                print("Error - Invalid character - a number was input where a letter was expected.")
            elif CustPostal[2].isdigit():
                print("Error - Invalid character - a number was input where a letter was expected.")
            elif CustPostal[4].isdigit():
                print("Error - Invalid character - a number was input where a letter was expected.")
            elif CustPostal[1].isalpha():
                print("Error - Invalid character - a letter was input where a number was expected.")
            elif CustPostal[3].isalpha():
                print("Error - Invalid character - a letter was input where a number was expected.")
            elif CustPostal[5].isalpha():
                print("Error - Invalid character - a letter was input where a number was expected.")
            else:
                break

        while True:
            CustPhone = input("Customer's Phone Number (7095551234): ")
            if CustPhone == "":
                print("Error - Customer Phone Number can not be blank.")
            elif len(CustPhone) != 10:
                print("Error - Phone Number must be 10 digits.")
            elif not CustPhone.isdigit():
                print("Error - Phone Number must be 10 digits.")
            else:
                break

        while True:
            NumCars = int(input("Number of Vehicles: "))
            if NumCars == "":
                print("Error - Number of Vehicles can not be blank.")
            elif NumCars < 1:
                print("Error - Number of Vehicles can not be negative")
            else:
                break

        while True:
            RESPONSE = ["Y", "N"]
            ExtraLiability = input("Extra Liability up to $1,000,000.00? (Y/N): ").upper()
            if ExtraLiability == "":
                print("Error - Liability can not be blank.")
            elif not ExtraLiability in RESPONSE:
                print("Error - Input invalid, please use 'Y' or 'N'.")
            else:
                break

        while True:
            RESPONSE = ["Y", "N"]
            GlassCover = input("Glass Coverage? (Y/N): ").upper()
            if GlassCover == "":
                print("Error - Glass Coverage can not be blank.")
            elif not GlassCover in RESPONSE:
                print("Error - Please enter 'Y' or 'N'.")
            else:
                break

        while True:
            RESPONSE = ["Y", "N"]
            Loaner = input("Loaner Vehicle? (Y/N): ").upper()
            if Loaner == "":
                print("Error - Loaner Vehicle can not be blank.")
            elif not Loaner in RESPONSE:
                print("Error - Please enter 'Y' or 'N'.")
            else:
                break

        while True:
            PAY_TYPE = ["Full", "Monthly"]
            Payment = input("Will the Customer be paying in full or monthly? (Full/Monthly): ").title()
            if Payment == "":
                print("Error - Customer Payment can not be blank.")
            elif not Payment in PAY_TYPE:
                print("Error - Please enter 'Full' or 'Monthly'")
            else:
                break

        f = open("OSICDef.dat", "r")
        POLICY_NUMBER = int(f.readline())
        BASIC_RATE = float(f.readline())
        MULTI_CAR_DISCOUNT = float(f.readline())
        EXTRA_LIABILITY_FEE = float(f.readline())
        GLASS_COVERAGE = float(f.readline())
        LOANER_CAR = float(f.readline())
        HST_RATE = float(f.readline())
        PROCESSING_FEE = float(f.readline())
        f.close()

        if NumCars > 1:
            Discount = MULTI_CAR_DISCOUNT * BASIC_RATE * (NumCars - 1)
            Premium = (BASIC_RATE * NumCars) - Discount
        else:
            Premium = BASIC_RATE

        if ExtraLiability == "Y":
            TotalLiability = EXTRA_LIABILITY_FEE * NumCars
        else:
            ExtraLiability = 0

        if GlassCover == "Y":
            TotalGlass = GLASS_COVERAGE * NumCars
        else:
            TotalGlass = 0

        if Loaner == "Y":
            TotalLoaner = LOANER_CAR * NumCars
        else:
            TotalLoaner = 0

        TotalExtra = TotalLiability + TotalGlass + TotalLoaner
        TotalPremium = Premium + TotalExtra
        HST = TotalPremium * HST_RATE
        TotalCost = TotalPremium + HST

        if Payment == "Monthly":
            MonthlyPayment = (TotalCost + PROCESSING_FEE) / 8
        elif Payment == "Full":
            MonthlyPayment = 0

        DaysMonth = lambda dt: monthrange(dt.year, dt.month)[1]
        CurrentDate = datetime.datetime.now()
        NextPaymentDate = CurrentDate.replace(day=1) + datetime.timedelta(DaysMonth(CurrentDate))
        InvoiceDate = FV.FDateS(CurrentDate)

        print()
        print("================================================================================")
        print("                          ONE STOP INSURANCE COMPANY")
        print("                               54 Spruce St.")
        print("                               Deer Lake, NL")
        print("                                  A8A 2C1")
        print("                               (709) 635-5289")
        print("================================================================================")
        print(f"Policy Number: {POLICY_NUMBER}                                     Invoice Date: {InvoiceDate}")
        print()
        print("Customer Information:                  Policy Information:")
        print("--------------------------------------------------------------------------------")
        print(f"Name:    {FullName:<16s}              Number of Vehicles:                     {NumCars:>1d}")
        print(f"Address: {CustStreet:<18s}            Extra Liability:                {FV.FDollar2(TotalLiability):>9s}")
        print(f"         {CustCity:<16s}              Glass Coverage:                 {FV.FDollar2(TotalGlass):>9s}")
        print(f"         {CustProv:<16s}              Loaner Coverage:                {FV.FDollar2(TotalLoaner):>9s}")
        print(f"         {CustPostal:<18s}            -----------------------------------------")
        print(f"Phone #: {CustPhone:<17s}             Total Extra Coverage:           {FV.FDollar2(TotalExtra):>9s}")
        print("--------------------------------------------------------------------------------")
        print(f"                                       Premium for {NumCars:>1d} Vehicles:         {FV.FDollar2(Premium):>9s}")
        print(f"                                       Total Extra Coverage Cost:      {FV.FDollar2(TotalExtra):>9s}")
        print(f"                                       Total Annual Policy Cost:       {FV.FDollar2(TotalPremium):>9s}")
        print(f"                                       HST:                            {FV.FDollar2(HST):>9s}")
        print("                                       -----------------------------------------")
        print(f"                                       Total Due:                      {FV.FDollar2(TotalCost):>9s}")
        print(f"                                       Payment Option:                   {Payment:>7s}")
        if Payment == "Monthly":
            print(f"                                       Monthly Payment:                {FV.FDollar2(MonthlyPayment):>9s}")
            print(f"                                       Payment Due Date:   {FV.FDateL(NextPaymentDate):>10s}")
        print()
        print("================================================================================")
        print("            THANKS FOR CHOOSING ONE STOP FOR YOUR INSURANCE NEEDS!")
        print("================================================================================")
        print()

        f = open("Policies.dat", "a")
        f.write(f"{POLICY_NUMBER}, ")
        f.write(f"{InvoiceDate}, ")
        f.write(f"{CustFirst}, ")
        f.write(f"{CustLast}, ")
        f.write(f"{CustPhone}, ")
        f.write(f"{CustStreet}, ")
        f.write(f"{CustCity}, ")
        f.write(f"{CustProv}, ")
        f.write(f"{CustPostal}, ")
        f.write(f"{NumCars}, ")
        f.write(f"{ExtraLiability}, ")
        f.write(f"{TotalLiability}, ")
        f.write(f"{GlassCover}, ")
        f.write(f"{TotalGlass}, ")
        f.write(f"{Loaner}, ")
        f.write(f"{TotalLoaner}, ")
        f.write(f"{TotalExtra}, ")
        f.write(f"{Payment}, ")
        f.write(f"{MonthlyPayment}, ")
        f.write(f"{TotalCost}\n")
        f.close()

        print("Saving data - Please wait.")
        for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=80, bar_format="{desc}  {bar}"):
            time.sleep(.3)
        print()
        print("Data successfully saved ...")
        time.sleep(1)

        POLICY_NUMBER += 1

        w = open("OSICDef.dat", "w")
        w.write(f"{str(POLICY_NUMBER)}\n")
        w.write(f"{str(BASIC_RATE)}\n")
        w.write(f"{str(MULTI_CAR_DISCOUNT)}\n")
        w.write(f"{str(EXTRA_LIABILITY_FEE)}\n")
        w.write(f"{str(GLASS_COVERAGE)}\n")
        w.write(f"{str(LOANER_CAR)}\n")
        w.write(f"{str(HST_RATE)}\n")
        w.write(f"{str(PROCESSING_FEE)}\n")
        w.close()

        Continue = input("Press enter to create another policy or 'End' to quit program: ").title()
        if Continue == "End":
            break


def PolicyListing():
    print()
    print("================================================================================")
    print("                          ONE STOP INSURANCE COMPANY")
    print("================================================================================")
    print(f"POLICY LISTING AS OF {FV.FDateM(CurrentDate)}")
    print()
    print("POLICY   CUSTOMER                POLICY       INSURANCE      EXTRA       TOTAL")
    print("NUMBER   NAME                     DATE         PREMIUM       COSTS      PREMIUM")
    print("================================================================================")

    f = open("Policies.dat", "r")

    Total_Policies = 0
    Total_Premiums = 0
    Total_Extra_Costs = 0
    Total_Total_Premiums = 0

    for CustomerInfoLine in f:
        CustomerInfo = CustomerInfoLine.split(",")
        POLICY_NUMBER = int(CustomerInfo[0])
        CUSTOMER_FIRST = CustomerInfo[2]
        CUSTOMER_LAST = CustomerInfo[3]
        CUSTOMERNAME = CUSTOMER_LAST + ", " + CUSTOMER_FIRST
        POLICY_DATE = CustomerInfo[1]
        INSURANCE_PREMIUM = float(CustomerInfo[19])
        TOTAL_EXTRAS = float(CustomerInfo[16])
        TOTAL_PREMIUM = INSURANCE_PREMIUM + TOTAL_EXTRAS

        print(f" {POLICY_NUMBER:<4d}  {CUSTOMERNAME:<20s}   {POLICY_DATE}     {FV.FDollar2(INSURANCE_PREMIUM)}     {FV.FDollar2(TOTAL_EXTRAS)}    {FV.FDollar2(TOTAL_PREMIUM)}")

        Total_Policies += 1
        Total_Premiums += INSURANCE_PREMIUM
        Total_Extra_Costs += TOTAL_EXTRAS
        Total_Total_Premiums += TOTAL_PREMIUM

    f.close()
    print("================================================================================")
    print(f"Total Policies: {Total_Policies:<3d}                          {FV.FDollar2(Total_Premiums)}"
          f"   {FV.FDollar2(Total_Extra_Costs)}   {FV.FDollar2(Total_Total_Premiums)}")


def MonthlyPaymentListing():
    print()
    print("================================================================================")
    print("                          ONE STOP INSURANCE COMPANY")
    print("================================================================================")
    print(f"MONTHLY PAYMENT LISTING AS OF {FV.FDateM(CurrentDate)}")
    print()
    print("POLICY  CUSTOMER                 TOTAL                      TOTAL        MONTHLY")
    print("NUMBER  NAME                    PREMIUM         HST         COST         PAYMENT")
    print("================================================================================")

    x = open("OSICDef.dat", "r")

    POLICY_NUMBER = int(x.readline())
    BASIC_RATE = float(x.readline())
    MULTI_CAR_DISCOUNT = float(x.readline())
    EXTRA_LIABILITY_FEE = float(x.readline())
    GLASS_COVERAGE = float(x.readline())
    LOANER_CAR = float(x.readline())
    HST_RATE = float(x.readline())
    PROCESSING_FEE = float(x.readline())
    x.close()

    f = open("Policies.dat", "r")

    Total_Policies = 0
    Total_Premiums = 0
    Total_HST = 0
    Total_Cost = 0
    Total_Monthly_Payment = 0

    for CustomerInfoLine in f:
        CustomerInfo = CustomerInfoLine.split(",")
        POLICY_NUMBER = int(CustomerInfo[0])
        CUSTOMER_FIRST = CustomerInfo[2]
        CUSTOMER_LAST = CustomerInfo[3]
        CUSTOMERNAME = CUSTOMER_LAST + ", " + CUSTOMER_FIRST
        INSURANCE_PREMIUM = float(CustomerInfo[19])
        TOTAL_EXTRAS = float(CustomerInfo[16])
        TOTAL_PREMIUM = INSURANCE_PREMIUM + TOTAL_EXTRAS
        HST = HST_RATE * TOTAL_PREMIUM
        TOTAL_COST = TOTAL_PREMIUM + HST
        PAYMENT = CustomerInfo[17].strip()
        MONTHLY_PAYMENT = (TOTAL_COST + PROCESSING_FEE) / 12

        if PAYMENT == "Monthly":
            print(f"{POLICY_NUMBER:<4d}   {CUSTOMERNAME:<20s}    {FV.FDollar2(TOTAL_PREMIUM)}       {FV.FDollar2(HST)}"
                  f"     {FV.FDollar2(TOTAL_COST)}     {FV.FDollar2(MONTHLY_PAYMENT)}")

            Total_Policies += 1
            Total_Premiums += TOTAL_PREMIUM
            Total_HST += HST
            Total_Cost += TOTAL_COST
            Total_Monthly_Payment += MONTHLY_PAYMENT

    f.close()
    print("================================================================================")
    print(f"Total Policies: {Total_Policies:<3d}           {FV.FDollar2(Total_Premiums)}     {FV.FDollar2(Total_HST)}"
          f"    {FV.FDollar2(Total_Cost)}   {FV.FDollar2(Total_Monthly_Payment)}")

# Main Program
print()
while True:
    print()
    print("================================================================================")
    print("                          ONE STOP INSURANCE COMPANY")
    print("================================================================================")
    print("     OPTIONS MENU")
    print()
    print("1 - NEW POLICY CREATOR")
    print("2 - POLICY LISTING")
    print("3 - MONTHLY PAYMENT LISTING")
    print("4 - QUIT PROGRAM")
    print()
    menu = input("Please select an option: ")
    print()

    if menu == "1":
        option = NewPolicyCreator()
    elif menu == "2":
        option = PolicyListing()
    elif menu == "3":
        option = MonthlyPaymentListing()
    elif menu == "4":
        break