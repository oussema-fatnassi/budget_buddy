import matplotlib.pyplot as plt

class Plotter:                                                                                  # Class to plot the graphics

    @staticmethod
    def plot_monthly_summary(selected_month, selected_year, total_income, total_expenses):      # Method to plot the monthly summary
        categories = ['Income', 'Expenses']
        values = [total_income, total_expenses]

        plt.figure(figsize=(3.3, 3))
        plt.bar(categories, values, color=["#393E46", "#C7C8CC"])                               # Plot the bar graph     
        plt.xlabel('Type of Transaction')
        plt.ylabel('Amount')
        plt.title(f'Monthly recap for {selected_month}/{selected_year}')
        plt.tight_layout()
        plt.savefig('plot.png')                                                                 # Save the plot as an image              

    @staticmethod
    def plot_category_summary(selected_month, selected_year, categories, amounts):              # Method to plot the category summary
        plt.figure(figsize=(3.3, 3))
        plt.bar(categories, amounts, color="#C7C8CC")
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title(f'Category-wise Transactions for {selected_month}/{selected_year}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('category_plot.png')

