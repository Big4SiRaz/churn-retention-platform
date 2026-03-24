# Churn Prediction & Retention Platform

## Overview

This project is an **API-first churn prediction and marketing retention platform** designed to help product, marketing, and CRM systems:

- Identify at-risk users early  
- Understand *why* users are likely to churn  
- Trigger targeted, actionable retention strategies  

The goal is not just to build a model, but to design a **production-style decision system** that bridges:

> **Data → Prediction → Explanation → Action → Integration**

---

## Problem Statement

Marketing teams often operate with:

- Limited visibility into churn risk  
- No clear understanding of *why* users churn  
- Inefficient, blanket retention campaigns  

This results in:
- Poor targeting  
- Wasted spend  
- Missed retention opportunities  

---

## Solution

This project builds a **churn intelligence platform** that:

- Predicts churn risk using historical behavior  
- Explains key drivers of churn (model explainability)  
- Maps predictions to **actionable retention strategies**  
- Exposes functionality via **APIs for integration with CRM and marketing systems**  
- Provides a **Streamlit UI** as a thin visualization layer  

---

## Target Users

- Marketing & Growth Teams  
- CRM / Campaign Systems  
- Product Managers  
- Data & Analytics Teams  

---

## Dataset

Primary dataset:
- **KKBox Churn Dataset**

Includes:
- transactions.csv — subscription activity  
- user_logs.csv — engagement behavior  
- members.csv — user metadata  

---

## Tools & Technologies

- Python (pandas, numpy, scikit-learn, SHAP)  
- DuckDB (large-scale feature aggregation)  
- Jupyter Notebook  
- FastAPI (planned)  
- Streamlit (planned)  

---

## Project Evolution

### Week 1–2: Data Understanding
- EDA, cleaning, anomaly detection  
- Churn label isolation  
- Identified skew, missing values, inconsistencies  

### Week 3: Baseline Modeling
- Leakage-aware setup  
- Logistic regression baseline  
- ROC ≈ 0.69  

### Week 4: Behavioral Integration
- Introduced user_logs  
- Faced scaling issues with pandas  
- Migrated to DuckDB  
- Built behavioral features  

### Week 5: Explainability
- Implemented SHAP  
- Identified churn drivers  
- Translated predictions to actions  

---

## Evolution Summary

| Stage | Capability |
|------|----------|
| Week 1–2 | Data understanding |
| Week 3 | Baseline prediction |
| Week 4 | Behavioral modeling |
| Week 5 | Actionable insights |

---

## Current Capabilities

- Predict churn  
- Explain drivers  
- Suggest retention actions  

---

## Limitations

- No real-time API yet  
- No A/B testing  
- Rule-based strategies  

---

## Phase 2 Roadmap

### API System
- FastAPI endpoints  
- Real-time + batch scoring  

### Experimentation
- A/B testing  
- Measure uplift  

### Synthetic Data
- Simulate interventions  

### Model Improvements
- Advanced models  
- Feature optimization  

### MLOps
- Monitoring  
- Drift detection  

---

## Key Learnings

- Correctness > accuracy  
- Data engineering is critical  
- Explainability enables action  
- Systems thinking is essential  

---

## Status

Week 1–5 complete  
Moving toward production system  

---

## Summary

This project evolved into a **churn intelligence platform** combining modeling, explainability, and product thinking with a clear roadmap toward production deployment.
