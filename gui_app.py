import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib

# Load the saved model
best_model = joblib.load('house_price_predictor_model.pkl')

# Define the actual distinct values from the dataset
location_values = ['Downtown', 'Suburban', 'Urban', 'Rural']
condition_values = ['Excellent', 'Good', 'Fair', 'Poor']
garage_values = ['No', 'Yes']

# Function to predict the price
def predict_price():
    try:
        # Gather input values from the user (get selected values from dropdowns)
        location = location_values.index(dropdown_location.get())
        condition = condition_values.index(dropdown_condition.get())
        garage = garage_values.index(dropdown_garage.get())
        area = slider_area.get()
        bedrooms = slider_bedrooms.get()
        bathrooms = slider_bathrooms.get()
        floors = slider_floors.get()
        year_built = slider_year_built.get()

        # Create input data in the correct feature order for the model
        input_data = pd.DataFrame({
            'Area': [area],
            'Bedrooms': [bedrooms],
            'Bathrooms': [bathrooms],
            'Floors': [floors],
            'YearBuilt': [year_built],
            'Location': [location],
            'Condition': [condition],
            'Garage': [garage]
        })

        # Predict the price using the loaded model
        predicted_price = best_model.predict(input_data)[0]

        # Display the predicted price
        messagebox.showinfo('Predicted Price', f'Predicted House Price: ${predicted_price:,.2f}')

    except Exception as e:
        messagebox.showerror('Input Error', f'Error: {str(e)}')

# Create and configure the main window
root = tk.Tk()
root.title("House Price Predictor")

# Labels and dropdowns for Location, Condition, and Garage
tk.Label(root, text="Location:").grid(row=0, column=0, padx=10, pady=10)
dropdown_location = ttk.Combobox(root, values=location_values)
dropdown_location.grid(row=0, column=1)
dropdown_location.current(0)  # Set default value

tk.Label(root, text="Condition:").grid(row=1, column=0, padx=10, pady=10)
dropdown_condition = ttk.Combobox(root, values=condition_values)
dropdown_condition.grid(row=1, column=1)
dropdown_condition.current(0)  # Set default value

tk.Label(root, text="Garage:").grid(row=2, column=0, padx=10, pady=10)
dropdown_garage = ttk.Combobox(root, values=garage_values)
dropdown_garage.grid(row=2, column=1)
dropdown_garage.current(0)  # Set default value

# Label for Area Slider
tk.Label(root, text="Area (in sq. ft.):").grid(row=3, column=0, padx=10, pady=10)

# Slider for Area
slider_area = tk.Scale(root, from_=100, to=5000, orient='horizontal', length=300)
slider_area.grid(row=3, column=1, padx=10, pady=10)

# Slider for Bedrooms
tk.Label(root, text="Bedrooms:").grid(row=4, column=0, padx=10, pady=10)
slider_bedrooms = tk.Scale(root, from_=1, to=5, orient='horizontal', length=300)
slider_bedrooms.grid(row=4, column=1, padx=10, pady=10)

# Slider for Bathrooms
tk.Label(root, text="Bathrooms:").grid(row=5, column=0, padx=10, pady=10)
slider_bathrooms = tk.Scale(root, from_=1, to=4, orient='horizontal', length=300)
slider_bathrooms.grid(row=5, column=1, padx=10, pady=10)

# Slider for Floors
tk.Label(root, text="Floors:").grid(row=6, column=0, padx=10, pady=10)
slider_floors = tk.Scale(root, from_=1, to=3, orient='horizontal', length=300)
slider_floors.grid(row=6, column=1, padx=10, pady=10)

# Slider for Year Built
tk.Label(root, text="Year Built:").grid(row=7, column=0, padx=10, pady=10)
slider_year_built = tk.Scale(root, from_=1900, to=2023, orient='horizontal', length=300)
slider_year_built.grid(row=7, column=1, padx=10, pady=10)

# Button to predict the price
predict_button = tk.Button(root, text="Predict Price", command=predict_price)
predict_button.grid(row=8, column=0, columnspan=2, pady=20)

# Run the GUI
root.mainloop()
