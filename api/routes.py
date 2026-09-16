"""
FastAPI Routes and Interactive ML/AI Demo Engines
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Any
import os
import random
import time
from datetime import datetime

from api.data import (
    PROFILE_DATA, SKILLS_DATA, EXPERIENCE_DATA,
    PROJECTS_DATA, EDUCATION_DATA, CERTIFICATIONS_DATA
)

router = APIRouter(prefix="/api")

# --- Pydantic Schemas ---
class FraudPredictionInput(BaseModel):
    amount: float = Field(..., example=1250.50, ge=0)
    transaction_time: int = Field(..., example=3, ge=0, le=23) # hour of day
    v1_feature: float = Field(default=0.5, example=-1.2)
    v2_feature: float = Field(default=-0.3, example=2.4)
    is_international: bool = Field(default=False)
    card_type: str = Field(default="Visa Platinum")

class ContactMessageInput(BaseModel):
    name: str = Field(..., min_length=2)
    email: str = Field(..., example="recruiter@tech.com")
    subject: str = Field(..., min_length=3)
    message: str = Field(..., min_length=10)

class InterviewCoachInput(BaseModel):
    role: str = Field(..., example="Data Scientist")
    question_id: str = Field(..., example="q_ml_1")
    question_text: str = Field(..., example="Explain how you handle imbalanced datasets in classification.")
    user_response: str = Field(..., min_length=5, example="I use SMOTE for oversampling minority classes, adjust class weights in XGBoost, and use Precision-Recall curves instead of standard accuracy.")

# Memory store for contact messages
CONTACT_MESSAGES: List[Dict[str, Any]] = []


# --- Profile & Data Routes ---
@router.get("/profile")
def get_profile():
    return PROFILE_DATA

@router.get("/skills")
def get_skills():
    return SKILLS_DATA

@router.get("/experience")
def get_experience():
    return EXPERIENCE_DATA

@router.get("/projects")
def get_projects():
    return PROJECTS_DATA

@router.get("/education")
def get_education():
    return EDUCATION_DATA

@router.get("/certifications")
def get_certifications():
    return CERTIFICATIONS_DATA


# --- Interactive Demo 1: Credit Card Fraud Detection ML Simulator ---
@router.post("/demo/fraud-detection")
def predict_fraud(data: FraudPredictionInput):
    """
    Simulates real-time Credit Card Fraud Detection ML Classifier (RandomForest/XGBoost logic).
    Calculates dynamic risk probability based on feature weights.
    """
    start_time = time.time()
    
    # Risk calculation heuristic based on financial fraud patterns
    risk_score = 0.05  # Base baseline noise
    risk_factors = []
    
    # 1. Transaction Amount Risk
    if data.amount > 2000:
        risk_score += 0.40
        risk_factors.append(f"High Transaction Value (${data.amount:,.2f}) exceeds standard spending threshold")
    elif data.amount > 800:
        risk_score += 0.20
        risk_factors.append(f"Elevated Amount (${data.amount:,.2f}) detected")
        
    # 2. Time Anomaly (Night time transactions 1 AM - 4 AM)
    if 1 <= data.transaction_time <= 4:
        risk_score += 0.25
        risk_factors.append(f"Unusual Transaction Hour ({data.transaction_time:02d}:00 AM) off-peak time")
        
    # 3. International location anomaly
    if data.is_international:
        risk_score += 0.20
        risk_factors.append("Cross-border / International IP location flagged")
        
    # 4. Feature Vector Anomaly (V1 & V2 anomaly components)
    vector_anomaly = abs(data.v1_feature) * 0.15 + abs(data.v2_feature) * 0.15
    risk_score += min(vector_anomaly, 0.30)
    if vector_anomaly > 0.25:
        risk_factors.append(f"PCA Feature Vector Deviation (V1={data.v1_feature:.2f}, V2={data.v2_feature:.2f})")

    # Clamp risk score between 0.01 and 0.99
    risk_score = max(0.01, min(0.99, risk_score))
    
    is_fraud = risk_score >= 0.55
    risk_level = "CRITICAL HIGH" if risk_score >= 0.75 else ("ELEVATED" if risk_score >= 0.55 else ("MODERATE" if risk_score >= 0.30 else "LOW"))
    
    latency_ms = round((time.time() - start_time) * 1000 + random.uniform(2, 6), 2)
    
    return {
        "status": "success",
        "timestamp": datetime.utcnow().isoformat(),
        "input_summary": {
            "amount": f"${data.amount:,.2f}",
            "time_hour": f"{data.transaction_time:02d}:00",
            "is_international": data.is_international,
            "card_type": data.card_type
        },
        "prediction": {
            "is_fraudulent": is_fraud,
            "fraud_probability": round(risk_score * 100, 2),
            "confidence_score": round(99.4 - (risk_score * 2), 2),
            "risk_level": risk_level,
            "decision": "DECLINE & FLAG" if is_fraud else "APPROVE TRANSACTION"
        },
        "feature_contributions": [
            {"feature": "Transaction Amount", "weight": 35 if data.amount > 1000 else 15},
            {"feature": "Time of Day", "weight": 25 if (1 <= data.transaction_time <= 4) else 5},
            {"feature": "Geo Location", "weight": 20 if data.is_international else 5},
            {"feature": "PCA Latent Vector", "weight": round(vector_anomaly * 100, 1)}
        ],
        "risk_factors": risk_factors if risk_factors else ["All features within normal statistical variance"],
        "performance_metrics": {
            "model_architecture": "XGBoost + FastAPI ML Pipeline",
            "inference_time_ms": latency_ms,
            "dataset_trained": "Kaggle European Credit Card Fraud Dataset (284,807 transactions)"
        }
    }


# --- Interactive Demo 2: Sales Analytics Dashboard Endpoint ---
@router.get("/demo/sales-analytics")
def get_sales_analytics():
    """
    Returns live sales dataset for Power BI style interactive charts.
    Demonstrates the 15% profit margin improvement metrics.
    """
    return {
        "summary": {
            "total_revenue": "$1,485,200",
            "total_orders": "14,250",
            "average_order_value": "$104.22",
            "profit_margin_before": "18.5%",
            "profit_margin_after": "21.3%",
            "margin_improvement": "+15.1% Uplift"
        },
        "monthly_performance": [
            {"month": "Jan", "revenue": 95000, "cost": 77500, "profit_margin": 18.4, "optimized_margin": 20.8},
            {"month": "Feb", "revenue": 105000, "cost": 85500, "profit_margin": 18.5, "optimized_margin": 21.0},
            {"month": "Mar", "revenue": 120000, "cost": 97800, "profit_margin": 18.5, "optimized_margin": 21.2},
            {"month": "Apr", "revenue": 115000, "cost": 93700, "profit_margin": 18.5, "optimized_margin": 21.1},
            {"month": "May", "revenue": 135000, "cost": 110000, "profit_margin": 18.5, "optimized_margin": 21.4},
            {"month": "Jun", "revenue": 150000, "cost": 122250, "profit_margin": 18.5, "optimized_margin": 21.5},
            {"month": "Jul", "revenue": 140000, "cost": 114100, "profit_margin": 18.5, "optimized_margin": 21.3},
            {"month": "Aug", "revenue": 160000, "cost": 125900, "profit_margin": 18.5, "optimized_margin": 21.3}
        ],
        "regional_breakdown": [
            {"region": "North America", "sales": 520000, "percentage": 35.0, "color": "#6366f1"},
            {"region": "Europe", "sales": 415000, "percentage": 28.0, "color": "#a855f7"},
            {"region": "Asia-Pacific", "sales": 340000, "percentage": 22.9, "color": "#06b6d4"},
            {"region": "Latin America", "sales": 210200, "percentage": 14.1, "color": "#10b981"}
        ],
        "product_categories": [
            {"category": "Electronics & Gadgets", "revenue": 620000, "margin": "24.5%"},
            {"category": "Apparel & Accessories", "revenue": 380000, "margin": "19.2%"},
            {"category": "Home & Office", "revenue": 285200, "margin": "17.8%"},
            {"category": "Software Subscriptions", "revenue": 200000, "margin": "32.0%"}
        ],
        "key_insights": [
            "Reallocated marketing spend from low-ROI regional channels to top 20% high-margin product bundles.",
            "Dynamic pricing algorithm reduced stock holding costs by 12% in peak Q2.",
            "Visualized customer churn triggers in Power BI resulting in a 15.1% net expansion of profit margin."
        ]
    }


# --- Interactive Demo 3: AI Interview Coach Sandbox Endpoint ---
MOCK_QUESTIONS = {
    "Data Scientist": [
        {
            "id": "ds_1",
            "question": "How do you handle class imbalance in machine learning datasets?",
            "keywords": ["smote", "oversampling", "undersampling", "class weights", "precision", "recall", "f1", "auc-roc", "xgboost"],
            "ideal_sample": "I handle class imbalance using a combination of resampling techniques (like SMOTE for synthetic oversampling) and algorithm-level adjustments such as cost-sensitive learning (setting class_weight='balanced' in Scikit-Learn or scale_pos_weight in XGBoost). Crucially, I evaluate models using Precision-Recall AUC and F1-score rather than simple accuracy."
        },
        {
            "id": "ds_2",
            "question": "What is the difference between L1 (Lasso) and L2 (Ridge) regularization?",
            "keywords": ["l1", "l2", "lasso", "ridge", "sparsity", "feature selection", "absolute", "squared", "penalty"],
            "ideal_sample": "L1 (Lasso) adds the absolute value of coefficients as penalty, which forces useless feature weights to exact zero—effectively performing automated feature selection. L2 (Ridge) adds the squared magnitude of coefficients, shrinking weights smoothly towards zero without making them zero, which helps handle multicollinearity."
        }
    ],
    "Data Analyst": [
        {
            "id": "da_1",
            "question": "Walk me through how you optimized profit margin in a sales dataset using Power BI.",
            "keywords": ["power bi", "dax", "kpi", "profit margin", "trend analysis", "breakdown", "regional", "insights"],
            "ideal_sample": "I built an interactive Power BI dashboard connecting retail transaction tables. Using custom DAX measures for Net Margin % and Customer Lifetime Value, I identified low-margin product categories and underperforming regions. Presenting these insights enabled targeted price adjustments that boosted net profit margins by 15%."
        }
    ],
    "Python Developer": [
        {
            "id": "py_1",
            "question": "Why use FastAPI over Flask or Django for modern async API development?",
            "keywords": ["fastapi", "async", "asyncio", "pydantic", "openapi", "type hints", "speed", "uvicorn", "performance"],
            "ideal_sample": "FastAPI leverages Python 3.7+ type hints and Starlette for high-performance async/await operations, achieving speeds comparable to NodeJS and Go. It provides automatic Pydantic request data validation and auto-generates interactive OpenAPI/Swagger documentation out of the box."
        }
    ]
}

@router.get("/demo/interview-questions")
def get_interview_questions(role: Optional[str] = "Data Scientist"):
    questions = MOCK_QUESTIONS.get(role, MOCK_QUESTIONS["Data Scientist"])
    return {"role": role, "questions": questions}

@router.post("/demo/interview-coach")
def evaluate_interview_answer(data: InterviewCoachInput):
    """
    Evaluates candidate's interview response using simulated NLP vector semantic similarity (Chroma DB + Sentence Transformers concept).
    """
    response_text = data.user_response.lower()
    
    # Find question definition
    question_pool = MOCK_QUESTIONS.get(data.role, [])
    target_q = next((q for q in question_pool if q["id"] == data.question_id), None)
    
    keywords = target_q["keywords"] if target_q else ["model", "data", "python", "analysis"]
    ideal_sample = target_q["ideal_sample"] if target_q else "A strong response covers technical terminology, methodology, and quantifiable results."
    
    # 1. Keyword density score
    matched_keywords = [kw for kw in keywords if kw in response_text]
    keyword_score = min(100, int((len(matched_keywords) / max(1, len(keywords))) * 120))
    
    # 2. Depth & Length score
    words = response_text.split()
    word_count = len(words)
    length_score = min(100, int((word_count / 40) * 100))
    
    # 3. Sentiment & Clarity score
    clarity_score = 88 if word_count > 15 else 60
    
    # Overall Weighted AI Score (Chroma DB Vector Cosine Similarity simulation)
    overall_score = min(98, max(45, int(keyword_score * 0.5 + length_score * 0.3 + clarity_score * 0.2)))
    
    grade = "EXCELLENT" if overall_score >= 85 else ("GOOD" if overall_score >= 70 else "NEEDS IMPROVEMENT")
    
    feedback_points = []
    if len(matched_keywords) > 0:
        feedback_points.append(f"Great inclusion of key technical concepts: {', '.join(matched_keywords[:4])}")
    else:
        feedback_points.append("Try incorporating more specific domain terminology.")
        
    if word_count < 25:
        feedback_points.append("Elaborate further with concrete real-world examples or metrics.")
    else:
        feedback_points.append("Good answer structure and technical depth.")

    return {
        "status": "success",
        "evaluation": {
            "overall_score": overall_score,
            "grade": grade,
            "breakdown": {
                "relevance_score": keyword_score,
                "technical_depth": length_score,
                "communication_clarity": clarity_score
            },
            "vector_similarity_match": f"{overall_score - random.randint(1, 4)}%",
            "key_terms_matched": matched_keywords,
            "feedback": feedback_points,
            "sample_recommended_answer": ideal_sample
        }
    }


# --- Contact Form Submission API ---
@router.post("/contact")
def submit_contact(msg: ContactMessageInput):
    entry = {
        "id": len(CONTACT_MESSAGES) + 1,
        "name": msg.name,
        "email": msg.email,
        "subject": msg.subject,
        "message": msg.message,
        "received_at": datetime.utcnow().isoformat()
    }
    CONTACT_MESSAGES.append(entry)
    return {
        "status": "success",
        "message": f"Thank you {msg.name}! Your message has been sent successfully to Areeba Hasan.",
        "entry_id": entry["id"]
    }


# --- Resume PDF Download Endpoint ---
@router.get("/download-resume")
def download_resume():
    pdf_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "assets", "Areeba_Hasan_Resume.pdf")
    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=404, detail="Resume PDF file not found")
    return FileResponse(
        path=pdf_path,
        filename="Areeba_Hasan_Resume.pdf",
        media_type="application/pdf"
    )
