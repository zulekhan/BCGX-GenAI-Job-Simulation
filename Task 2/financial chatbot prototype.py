import pandas as pd

# Reading the Final data report and summary report
final_report = pd.read_csv('final_financial_data_report.csv')
summary_report = pd.read_csv('year_by_year_summary_report.csv')


# Creating a basic Rule-based Logic AI-Driven Chatbot
def financial_chatbot(fiscal_year, company_input):
    print("\nPlease enter your query:")
    user_query = input().strip().lower()

    try:
        if user_query == "what is the total revenue?":
            revenue = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Revenue']
            if revenue.empty:
                return f"No data available for {company_input} in fiscal year {fiscal_year}."
            return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue.values[0]}"

        elif user_query == "what is the net income?":
            net_income = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income']
            if net_income.empty:
                return f"No data available for {company_input} in fiscal year {fiscal_year}."
            return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income.values[0]}"

        elif user_query == "what is the sum of total assets?":
            total_assets = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Assets']
            if total_assets.empty:
                return f"No data available for {company_input} in fiscal year {fiscal_year}."
            return f"The sum of Total Assets for {company_input} for fiscal year {fiscal_year} is $ {total_assets.values[0]}"



        else:
            return (
                "Sorry, I cannot provide information on the requested query. "
                "Available queries include: \n"
                "- What is the total revenue?\n"
                "- What is the net income?\n"
                "- What is the sum of total assets?\n"
                "Please try again!"
            )

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Test the chatbot
while True:
    print("----------------------------------------------------------------------------")
    user_input = input("\nEnter 'Hi' to start the chatbot session; type 'exit' to quit: ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "hi":
        print("\nHello! Welcome to the AI-Driven Financial Chatbot!!!")
        print("\nI can help you with your financial queries.")
        print("\nPlease select the company name from below:")
        print("1. Microsoft\n2. Tesla\n3. Apple")
        company_input = input("Enter company name: ").capitalize()
        if company_input not in ['Apple', 'Microsoft', 'Tesla']:
            print("Invalid Company Name. Please check and enter the correct company name.")
            break
        else:
            print("\nThe data for the fiscal years 2023, 2022, and 2021 is currently available.")
            try:
                fiscal_year = int(input("Enter the fiscal year for the selected company: "))
                if fiscal_year not in [2023, 2022, 2021]:
                    print("Invalid fiscal year. Please restart the chatbot session and try again.")
                    break
            except ValueError:
                print("Invalid input. Fiscal year must be a number. Please restart the chatbot session.")
                break
    else:
        print("Enter 'Hi' properly to start the chatbot session.")
        break

    response = financial_chatbot(fiscal_year, company_input)
    print(response)