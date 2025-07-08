# from src import change_analysis, risk_assessment, deployment_monitor, rollback_decision

# change_log = {'files_changed': 6, 'lines_added': 300, 'lines_removed': 150, 'services': ['auth', 'payment']}
# metrics = {'error_rate': 0.5}

# features = change_analysis.extract_change_features(change_log)
# X_sample = [[features['files_changed'], features['lines_added'], features['lines_removed'], features['services_affected']]]

# predictor = risk_assessment.RiskPredictor()
# predictor.train(X_sample, [1])
# risk_score = predictor.predict(X_sample)[0]

# anomaly = deployment_monitor.detect_anomalies(metrics)
# rollback = rollback_decision.should_rollback(risk_score, anomaly)

# print(f"Risk Score: {risk_score:.2f} | Anomaly: {anomaly} | Rollback Triggered: {rollback}")

import pandas as pd
from src import change_analysis, risk_assessment, deployment_monitor, rollback_decision

df = pd.read_csv('data/deployment_logs.csv')
X = df.drop('rollback', axis=1)
y = df['rollback']

predictor = risk_assessment.RiskPredictor()
predictor.train(X, y)

change_log = {'files_changed': 6, 'lines_added': 300, 'lines_removed': 150, 'services': ['auth', 'payment']}
metrics = {'error_rate': 0.5}

features = change_analysis.extract_change_features(change_log)

X_sample = pd.DataFrame([{
    'files_changed': features['files_changed'],
    'lines_added': features['lines_added'],
    'lines_removed': features['lines_removed'],
    'services_affected': features['services_affected'],
    'error_rate': metrics['error_rate'],
    'duration_sec': 300  
}])

risk_score = predictor.predict(X_sample)[0]
anomaly = deployment_monitor.detect_anomalies(metrics)
rollback = rollback_decision.should_rollback(risk_score, anomaly)

print(f"Risk Score: {risk_score:.2f}")
print(f"Anomaly Detected: {anomaly}")
print(f"Rollback Triggered: {rollback}")
