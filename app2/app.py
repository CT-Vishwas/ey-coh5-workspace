from src.data_loading import load_data
import pandas as pd
import matplotlib.pyplot as plt
from src.report_generation import create_compliance_report, ReportData


if __name__ == "__main__":
    df_app = load_data("./data/cap_app_inventory.csv")
    df_compliance_status = load_data("./data/cap_compliance_status.csv")

    print("Application Inventory Data:")
    print(df_app.head())
    print("\nCompliance Status Data:")
    print(df_compliance_status.head())


    # join the two dataframes on the 'app_id' column
    df_merged = pd.merge(df_app, df_compliance_status, on='App_ID', how='inner')

    print("\nMerged Data:")
    print(df_merged.head())

    # Fix Compliance_Score to be numeric, remove any non-numeric characters
    df_merged['Compliance_Score'] = pd.to_numeric(df_merged['Compliance_Score'].str.replace(r'%', ''), errors='coerce')
    # print(df_merged.head())

        # Generate  insights from the merged data (e.g., count of compliant vs non-compliant applications)
    try:
        compliance_counts = df_merged['Status'].value_counts()
        print("Compliance Status Counts:")
        print(compliance_counts)
    except Exception as e:
        print(f"An error occurred while generating insights: {e}")

    # # Plot compliance score distribution by department
    plt.figure(figsize=(10, 6))
    df_merged.boxplot(column='Compliance_Score', by='Department')
    plt.title('Compliance Score Distribution by Department')
    plt.suptitle('')
    plt.xlabel('Department')
    plt.ylabel('Compliance Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('./output/compliance_score_distribution.png')

    # pie chart of compliance score by department
    plt.figure(figsize=(8, 8))
    df_merged.groupby('Department')['Compliance_Score'].mean().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Average Compliance Score by Department')
    plt.ylabel('')
    plt.savefig('./output/average_compliance_score_by_department.png')

        # Generate a report summarizing the insights (e.g., save to a text file)
    try:
        report_data = ReportData(
            company_title="Company Title",
            status_counts=compliance_counts.to_dict(),
            department_scores=df_merged.groupby('Department')['Compliance_Score'].mean().to_dict(),
            generation_time=pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
            reporter_name="Reporter"
        )
        create_compliance_report(report_data)
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")