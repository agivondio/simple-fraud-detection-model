# AI-Powered Fraud Detection API
This project is a simple backend system that detects potentially fraudulent transactions using rule-based scoring combined with AI-inspired logic. It is designed as a foundational prototype for fraud detection systems in financial platforms.

## Features
- Fraud detection based on transaction patterns
- Risk scoring system (0.0 – 1.0)
- Explainable AI output (reason for classification)
- REST API built with Spring Boot
- In-memory database using H2
- Transaction logging for audit and analysis
- Endpoints to retrieve all and fraudulent transactions

## Tech Stack
- Java 17
- Spring Boot
- Spring Data JPA
- H2 Database
- REST API

## API Endpoints
### 1. Check Transaction
POST /api/check-transaction
Request:
{
  "amount": 7000,
  "frequency": 10
}

Response:
{
  "fraud": true,
  "riskScore": 0.9,
  "reason": "High transaction amount & unusual frequency"
}

### 2. Get All Transactions
GET /api/transactions

### 3. Get Fraud Transactions
GET /api/transactions/fraud

## How to Run
1. Clone repository
2. Open project in IntelliJ IDEA
3. Run TransactionRiskApiApplication
4. Access API at: http://localhost:8081/api

## H2 Database Access
Open : http://localhost:8081/h2-console
Use >
JDBC URL: jdbc:h2:mem:testdb
User: sa
Password: (empty)

## Example Use Case
A transaction with high amount and unusual frequency will be flagged:
Amount: 9000
Frequency: 12
Result: Fraud (Risk Score: 0.9)

## Future Improvements
1. Integrate real machine learning model (Python)
2. Add authentication & security
3. Deploy to cloud (AWS / GCP)
4. Add dashboard for monitoring transactions
5. Improve fraud detection using historical data

## Author
Primusandy Subhan Agivondio
agivondio
