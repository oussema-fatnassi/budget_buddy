import matplotlib.pyplot as plt

class Plotter:

    @staticmethod
    def plot_monthly_summary(selected_month, selected_year, total_income, total_expenses):
        categories = ['Income', 'Expenses']
        values = [total_income, total_expenses]

        plt.figure(figsize=(3.3, 3))
        plt.bar(categories, values, color=["#393E46", "#C7C8CC"])
        plt.xlabel('Type of Transaction')
        plt.ylabel('Amount')
        plt.title(f'Monthly recap for {selected_month}/{selected_year}')
        plt.tight_layout()

        # Save the plot as an image
        plt.savefig('plot.png')

    @staticmethod
    def plot_category_summary(selected_month, selected_year, categories, amounts):
        plt.figure(figsize=(3.3, 3))
        plt.bar(categories, amounts, color="#4CAF50")
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title(f'Category-wise Transactions for {selected_month}/{selected_year}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Save the plot as an image
        plt.savefig('category_plot.png')

