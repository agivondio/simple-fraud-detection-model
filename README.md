# AI-Powered Fraud Detection API

This project is a simple backend system that detects potentially fraudulent transactions using rule-based scoring combined with AI-inspired logic. It is designed as a foundational prototype for fraud detection systems in financial platforms.

---

## 🚀 Features

- Fraud detection based on transaction patterns
- Risk scoring system (0.0 – 1.0)
- Explainable AI output (reason for classification)
- REST API built with Spring Boot
- In-memory database using H2
- Transaction logging for audit and analysis
- Endpoints to retrieve all and fraudulent transactions

---

## 🛠 Tech Stack

- Java 17
- Spring Boot
- Spring Data JPA
- H2 Database
- REST API

---

## 📡 API Endpoints

### 1. Check Transaction
`POST /api/check-transaction`

Request:
```json
{
  "amount": 7000,
  "frequency": 10
}
