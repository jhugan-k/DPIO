# DPIO: Dynamic Pricing Intelligence & Optimization

[![Python Version](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deployment](https://img.shields.io/badge/Deployment-AWS%20Elastic%20Beanstalk-orange.svg)](https://aws.amazon.com/elasticbeanstalk/)

A comprehensive web application built with Streamlit that leverages machine learning to forecast product demand and calculate optimal pricing strategies. This project demonstrates an end-to-end MLOps workflow, from data analysis to a containerized cloud deployment.

**[ live demo link will be placed here ]**

## Key Features

-   **Demand Forecasting:** Utilizes the Prophet library to accurately predict future product demand based on historical sales data.
-   **Price Elasticity Modeling:** Implements a linear regression model with Scikit-learn to understand how price changes affect demand.
-   **Price Optimization:** Calculates the optimal price point that maximizes revenue by balancing price and predicted demand.
-   **Interactive Dashboard:** A user-friendly interface built with Streamlit for visualizing data, forecasts, and pricing recommendations.
-   **Containerized & Cloud-Ready:** Fully containerized with Docker for consistent, reproducible deployments on any cloud platform.

## Tech Stack

-   **Language:** Python
-   **Web Framework:** Streamlit
-   **Data Science & ML:** Pandas, NumPy, Scikit-learn, Prophet
-   **Data Visualization:** Plotly, Altair, Seaborn
-   **Deployment:** Docker, AWS Elastic Beanstalk

## Deployment

This application is designed for cloud deployment. The included `Dockerfile` is used by AWS Elastic Beanstalk to build and host the container, creating a scalable and publicly accessible web service.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
