import matplotlib.pyplot as plt

def create_expenses_piechart():
    # Expense data (customize with your own values)
    categories = ['Rent', 'Food', 'Transport', 'Utilities', 'Entertainment', 'Savings']
    amounts = [1200, 600, 300, 200, 150, 400]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create pie chart
    wedges, texts, autotexts = ax.pie(
        amounts,
        labels=categories,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        explode=(0.05, 0, 0, 0, 0, 0),  # Slightly explode the largest slice
        shadow=True,
        textprops={'fontsize': 12}
    )
    
    # Equal aspect ratio ensures pie is drawn as a circle
    ax.axis('equal')
    
    # Add title
    plt.title('Monthly Expenses Breakdown', fontsize=16, pad=20)
    
    # Adjust layout
    plt.tight_layout()
    
    # Add legend
    plt.legend(
        wedges,
        categories,
        title="Expense Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )
    
    # Save and show the chart
    plt.savefig('monthly_expenses.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    create_expenses_piechart()