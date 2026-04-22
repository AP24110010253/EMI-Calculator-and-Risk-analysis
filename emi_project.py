# Loan EMI Calculator & Risk Analyzer (Enhanced Console Version)

# ---------------- EMI CALCULATION ----------------
def calculate_emi(P, rate, years):
    R = rate / (12 * 100)
    N = years * 12

    if R == 0:
        EMI = P / N
    else:
        EMI = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)

    total_payment = EMI * N
    total_interest = total_payment - P

    return EMI, total_interest, total_payment


# ---------------- RISK ----------------
def analyze_risk(emi, income):
    ratio = (emi / income) * 100

    if ratio < 20:
        return "Low Risk"
    elif ratio <= 40:
        return "Medium Risk"
    else:
        return "High Risk"


# ---------------- COMPARISON ----------------
def compare_interest(P, years, r1, r2):
    def emi_calc(rate):
        R = rate / (12 * 100)
        N = years * 12
        if R == 0:
            return P / N
        return (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)

    return emi_calc(r1), emi_calc(r2)


# ---------------- SUGGESTIONS ----------------
def suggestions(rate, years, emi):
    sug = []

    if rate > 10:
        sug.append("Try a lower interest rate loan")

    if years > 10:
        sug.append("Reduce tenure to save interest")

    if emi > 20000:
        sug.append("Consider reducing loan amount")

    if not sug:
        sug.append("Your loan plan looks optimal")

    return sug


# ---------------- BEST LOAN SUGGESTION ----------------
def best_loan_suggestion(income):
    safe_emi = 0.3 * income
    return safe_emi


# ---------------- TENURE CONVERSION ----------------
def convert_tenure():
    print("\n1. Years → Months")
    print("2. Months → Years")

    choice = input("Choose option: ")

    if choice == "1":
        years = float(input("Enter years: "))
        print(f"Months = {years * 12}")
    elif choice == "2":
        months = float(input("Enter months: "))
        print(f"Years = {months / 12:.2f}")
    else:
        print("Invalid choice")


# ---------------- MAIN ----------------
def main():
    print("\n====== LOAN EMI ANALYZER ======\n")

    P = float(input("Enter Loan Amount: "))
    rate = float(input("Enter Interest Rate (%): "))
    years = float(input("Enter Tenure (Years): "))

    emi, total_interest, total_payment = calculate_emi(P, rate, years)

    print("\n--- EMI DETAILS ---")
    print(f"EMI: ₹ {emi:.2f}")
    print(f"Total Interest: ₹ {total_interest:.2f}")
    print(f"Total Payment: ₹ {total_payment:.2f}")

    last_risk = "Not calculated"

    while True:
        print("\n--- MENU ---")
        print("1. Risk Analysis")
        print("2. Interest Comparison")
        print("3. Suggestions")
        print("4. Best Loan Suggestion ")
        print("5. Convert Tenure ")
        print("6. Exit (with Summary)")

        choice = input("Enter choice: ")

        if choice == "1":
            income = float(input("Enter Monthly Income: "))
            last_risk = analyze_risk(emi, income)
            print(f"Risk Level: {last_risk}")

        elif choice == "2":
            r1 = float(input("Enter Rate 1: "))
            r2 = float(input("Enter Rate 2: "))

            emi1, emi2 = compare_interest(P, years, r1, r2)

            print(f"EMI @ {r1}% = ₹ {emi1:.2f}")
            print(f"EMI @ {r2}% = ₹ {emi2:.2f}")

        elif choice == "3":
            sug = suggestions(rate, years, emi)
            print("\nSuggestions:")
            for s in sug:
                print("-", s)

        elif choice == "4":
            income = float(input("Enter your monthly income: "))
            safe_emi = best_loan_suggestion(income)
            print(f"Recommended EMI should be around ₹ {safe_emi:.2f}")

        elif choice == "5":
            convert_tenure()

        elif choice == "6":
            print("\n--- SESSION SUMMARY ---")
            print(f"Loan Amount: ₹ {P}")
            print(f"Interest Rate: {rate}%")
            print(f"Tenure: {years} years")
            print(f"EMI: ₹ {emi:.2f}")
            print(f"Risk: {last_risk}")
            print("\nThank you!")
            break

        else:
            print("Invalid choice")


# Run
main()