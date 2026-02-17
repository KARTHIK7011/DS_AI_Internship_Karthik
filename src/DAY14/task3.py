# Polynomial Regression Experiment
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score


np.random.seed(42)

X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = X**2 + np.random.normal(0, 2, size=X.shape)   # curved relationship


linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)

r2_linear = r2_score(y, y_pred_linear)


poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)

r2_poly = r2_score(y, y_pred_poly)


print("R² Score (Linear Features):", round(r2_linear, 4))
print("R² Score (Polynomial Features):", round(r2_poly, 4))
