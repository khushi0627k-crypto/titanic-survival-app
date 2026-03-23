# 🚢 Titanic Survival Prediction App

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, interactive web application built with Streamlit to predict the survival of passengers on the Titanic based on key attributes.

## 🌟 Overview

The Titanic Survival Prediction App provides an intuitive interface for users to input passenger details and receive an instant prediction on whether that passenger would have survived the tragic sinking of the RMS Titanic. This project serves as a practical demonstration of deploying a pre-trained machine learning model using Streamlit, making it accessible to a wider audience without requiring any coding knowledge.

**Key Value Proposition:**
*   **Ease of Use:** A straightforward web interface makes predictions simple and fast.
*   **Educational:** Illustrates the application of machine learning in a historical context.
*   **Interactive:** Users can experiment with different passenger profiles to see how various factors influence survival.

**Target Audience:**
*   Students and developers learning about Streamlit or ML model deployment.
*   Anyone interested in the Titanic story and data science applications.
*   Educators looking for a simple ML demo.

**Current Status:**
This is an initial release, providing core prediction functionality.

## ✨ Features

*   **Interactive Input Fields:** Easily adjust passenger class, sex, age, and fare using dropdowns, sliders, and number inputs.
*   **Real-time Predictions:** Get immediate survival predictions upon clicking the "Predict" button.
*   **Clear Visual Feedback:** Displays "✅ Passenger Survived" or "❌ Passenger Did Not Survive" for easy interpretation.
*   **Pre-trained ML Model:** Utilizes a pre-trained Scikit-learn model (`model.pkl`) for predictions.

## 🛠️ Tech Stack

*   **Python**: The core programming language.
*   **Streamlit**: For building the interactive web application user interface.
*   **Pandas**: (Implicitly used in model training, though not directly in `app.py`) For data manipulation.
*   **NumPy**: For numerical operations, especially handling feature arrays for the model.
*   **Scikit-learn**: The machine learning library used to train and deploy the prediction model.
*   **Pickle**: For serializing and deserializing the machine learning model (`model.pkl`).

## 🏗️ Architecture

The application follows a simple architecture:

*   **`app.py`**: This is the main Streamlit application file. It handles the user interface, collects input, loads the pre-trained machine learning model, and makes predictions.
*   **`model.pkl`**: A binary file containing the pre-trained Scikit-learn machine learning model. This model is loaded into `app.py` at runtime.
*   **`requirements.txt`**: Lists all the necessary Python dependencies for the project.

The Streamlit framework manages the web server and UI rendering, allowing `app.py` to focus solely on application logic.

```
.
├── ML_Web_App/
│   └── model.pkl           # (Potentially an older model, ensure root model.pkl is used)
├── app.py                  # Main Streamlit application
├── model.pkl               # Pre-trained Scikit-learn model for app.py
├── requirements.txt        # Python dependencies
└── ... (other files like analysis.ipynb, titanic.csv)
```

## 🚀 Getting Started

Follow these instructions to set up and run the Titanic Survival Prediction App on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
*   **pip**: Python's package installer (usually comes with Python).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/khushi0627k-crypto/titanic-survival-app.git
    cd titanic-survival-app
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

### Configuration

No special configuration is required. The `model.pkl` file should be present in the root directory alongside `app.py`.

## 🏃 Usage

To run the application, navigate to the project's root directory in your terminal (where `app.py` is located) and execute the following command:

```bash
streamlit run app.py
```

This will open the application in your default web browser (usually at `http://localhost:8501`).

**How to Use:**
1.  **Select Passenger Class:** Choose 1st, 2nd, or 3rd class.
2.  **Select Sex:** Choose Male or Female.
3.  **Adjust Age:** Use the slider to set the passenger's age.
4.  **Enter Fare:** Input the fare paid by the passenger.
5.  **Click "Predict":** The application will display whether the passenger survived or not.

![Titanic Survival App Screenshot](https://via.placeholder.com/800x450?text=Titanic+Survival+App+Screenshot)
*(Placeholder for a screenshot of the running Streamlit app)*

## ⚙️ Development

### Setting up Development Environment

1.  Follow the [Installation](#installation) steps to set up the project.
2.  The `.devcontainer` directory suggests that this project is set up for development in a containerized environment (e.g., VS Code Dev Containers). If you use VS Code, you can open the project in a Dev Container for a pre-configured development environment.

### Running Tests

This project currently does not include automated tests. For development, you can manually test the application by running `streamlit run app.py` and interacting with the UI.

### Code Style Guidelines

*   Follow PEP 8 for Python code style.
*   Keep the Streamlit UI code clean and well-commented.

## 🚀 Deployment

The Streamlit application can be easily deployed to various platforms.

### Streamlit Cloud

The simplest way to deploy this app is using Streamlit Cloud:

1.  Push your repository to GitHub.
2.  Go to [Streamlit Cloud](https://share.streamlit.io/) and connect your GitHub account.
3.  Select your repository and the `app.py` file as the main application file.
4.  Streamlit Cloud will automatically build and deploy your application.

### Docker/Containerization

For more controlled deployments, you can containerize the application using Docker. A `Dockerfile` would typically look like this (you might need to create one):

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run with Docker:

```bash
docker build -t titanic-survival-app .
docker run -p 8501:8501 titanic-survival-app
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  **Fork** the repository.
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name` or `bugfix/issue-description`.
3.  **Make your changes** and ensure they adhere to the project's code style.
4.  **Commit your changes** with a clear and descriptive message.
5.  **Push your branch** to your forked repository.
6.  **Open a Pull Request** to the `main` branch of this repository, describing your changes in detail.

## ❓ Troubleshooting

*   **`ModuleNotFoundError`**: Ensure all dependencies are installed from `requirements.txt`. Activate your virtual environment before running `pip install -r requirements.txt`.
*   **`model.pkl` not found**: Make sure `model.pkl` is in the same directory as `app.py`. If you moved `app.py`, update the path in `app.py` or move `model.pkl` accordingly.
*   **Streamlit not opening in browser**: Check your terminal for error messages. Ensure port 8501 is not blocked by a firewall or another application.

## 🗺️ Roadmap

*   Implement more advanced feature engineering for the model.
*   Add a section to display model performance metrics (e.g., accuracy, confusion matrix).
*   Allow users to upload their own CSV data for prediction.
*   Improve UI/UX with more visual elements and explanations.

## 📄 License & Credits

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Author:**
*   [khushi0627k](https://github.com/khushi0627k)

**Acknowledgments:**
*   The Titanic dataset is a classic for machine learning and can be found on platforms like Kaggle.
*   Thanks to the Streamlit community for providing an excellent framework for building web applications.