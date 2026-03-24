# Week 4 — Behavioral Feature Expansion (User Logs + Scalable Aggregation)

## Objective

The objective of **Week 4** was to extend the Week 3 baseline by incorporating **fine-grained behavioral data (`user_logs.csv`)**, with the goal of:

- Capturing **early engagement signals** beyond transactions  
- Improving **predictive lift over the Week 3 baseline (ROC ≈ 0.69)**  
- Maintaining strict **temporal causality and leakage control**  

---

## Context from Week 3

Week 3 established a **transaction-only churn prediction baseline** with:

- Carefully selected cutoff timestamp `T` to avoid leakage  
- Interpretable aggregated features  
- Realistic early-warning signal detection  

However, a key limitation was identified:

> Transactional data alone lacks sufficient behavioral depth to capture early churn signals.

---

## Dataset Expansion

**New dataset introduced:**
- `user_logs.csv` — high-frequency behavioral logs capturing user engagement patterns

This dataset includes:
- Session counts  
- Listening time  
- Interaction activity  
- Daily engagement signals  

---

## Core Challenge: Feature Engineering at Scale

Unlike transactional data, `user_logs` is:

- Extremely large (millions of records)  
- Time-series at daily granularity  
- Requires heavy aggregation across time windows  

---

## Initial Approach (Pandas-Based)

Initial attempts used Pandas to:
- Create rolling time windows (recent / mid / long-term)
- Aggregate per-user behavioral metrics

### Issues Encountered:
- Memory exhaustion  
- Slow execution times  
- Frequent crashes during groupby operations  

---

## Solution: Migration to DuckDB

To overcome scalability constraints, the pipeline was redesigned using **DuckDB**.

### Why DuckDB:
- Efficient SQL-based aggregations  
- Handles large datasets without full in-memory load  
- Seamless integration with Python workflows  

This transition was a **key architectural improvement**.

---

## Feature Engineering (Behavioral Signals)

All features were constructed within the same leakage-safe window:

- Feature window: `[T − 60 days, T)`

### Feature Categories

#### 1. Engagement Intensity
- Total sessions  
- Total listening time  
- Average session duration  

#### 2. Activity Frequency
- Active days  
- Sessions per active day  

#### 3. Behavioral Consistency
- Variance in engagement  
- Stability of activity patterns  

#### 4. Temporal Segmentation
- Recent vs mid vs long-term engagement comparisons (where feasible)

---

## Modeling Approach

To maintain comparability:

- Continued use of **interpretable models (Logistic Regression / Tree-based models)**  
- No aggressive hyperparameter tuning  

Focus remained on:
> Measuring **incremental signal gain**, not maximizing complexity.

---

## Evaluation Philosophy

Consistent with Week 3:

- ROC-AUC used as directional metric  
- Emphasis on:
  - Early signal detection  
  - Avoiding inactivity-driven shortcuts  

### Observations

- Improved separation for mid-risk users  
- Behavioral features added predictive value beyond transactions  
- Model retained realistic decision boundaries  

---

## Key Learnings

### 1. Scalability is Critical
> Feature engineering pipelines must be designed for large-scale data from the start.

### 2. Behavioral Data Adds Early Signal
> Engagement patterns act as leading indicators of churn.

### 3. Tooling Drives Feasibility
> DuckDB enabled workflows that were impractical in Pandas.

### 4. Feature Design Trade-offs
> More granular features improve signal but increase system complexity.

---

## Limitations

- No sequence modeling (temporal ordering not fully leveraged)  
- Limited feature selection optimization  
- Some windowing strategies constrained by computational limits  

---

## What This Phase Achieved

By the end of Week 4:

- Successfully integrated **behavioral data into churn modeling**  
- Built a **scalable feature engineering pipeline using DuckDB**  
- Demonstrated **incremental improvement over baseline**  
- Strengthened the foundation for **user-level analysis and interpretation**  

---

## Next Phase

**Week 5 focuses on:**
- Model explainability (SHAP)  
- Identifying key churn drivers  
- Translating predictions into actionable retention strategies  

---

## Summary

> **Week 4 transformed the baseline into a behavior-aware system by overcoming scalability challenges and introducing meaningful early engagement signals into churn prediction.**
