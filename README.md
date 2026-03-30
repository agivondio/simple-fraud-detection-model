# Simple Fraud Detection Model
A simple machine learning-based fraud detection model built using Python. This project demonstrates how transaction data can be analyzed to identify potentially fraudulent behavior.

## Features
- Fraud detection using anomaly detection
- Built with Isolation Forest (unsupervised learning)
- Works with transaction amount and frequency
- Lightweight and easy to understand
- Suitable for integration with backend systems

## Model Approach
This project uses:
- Isolation Forest Algorithm
- Detects anomalies based on unusual patterns
- No labeled data required (unsupervised learning)

## Tech Stack
- Python 3
- Pandas
- Scikit-learn

## Project Structure
model.py # main model script

## How to Run
1. Install dependencies:
pip install pandas scikit-learn

2. Run the model:
python model.py

## Integration Idea
This model can be integrated into a backend system (e.g., Spring Boot API) to provide real-time fraud detection.

## Future Improvements
- Train with real-world dataset
- Add more features (location, time, device)
- Improve accuracy with supervised learning
- Export model for API integration

## Author
Primusandy Subhan Agivondio
