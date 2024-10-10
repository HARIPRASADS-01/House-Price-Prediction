# House Price Prediction Project

This project predicts house prices based on various features such as area, bedrooms, location, condition, etc. It uses machine learning algorithms like Random Forest and Gradient Boosting to train models for price prediction.

## Dataset

The dataset contains 2000 rows and 9 columns of housing data. It includes features like:
- **Area**: House size in sq. ft.
- **Bedrooms, Bathrooms**: Number of rooms.
- **Location, Condition**: Various categorical features.
- **Price**: Target variable (house price).

## Steps

1. **Data Preprocessing**: Categorical encoding and train-test split.
2. **Modeling**: Using Random Forest and Gradient Boosting to compare performance.
3. **Evaluation**: Mean Squared Error (MSE) and R2 score for model performance.
4. **GUI Application**: A Tkinter-based GUI allows for real-time price predictions.

## Model Results

The best model was the Random Forest Regressor, which achieved the lowest Mean Squared Error (MSE).

 images\performance_plot.png

## Installation and Usage

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/House-Price-Prediction.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. To run the Jupyter notebook:

    ```
    jupyter notebook house_price_prediction.ipynb
    ```

4. Run the GUI:

    ```
    python gui_app.py
    ```

## Visual Outputs



**KDE Plot**
images\kde_plot.png

**Scatter Plot**  
images\scatter_plot.png

## Future Improvements

- Adding external factors like proximity to amenities.
- Time-series modeling for economic trends.

