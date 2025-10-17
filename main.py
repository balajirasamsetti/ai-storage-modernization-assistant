"""
main.py

Entry point for the AI Storage Modernization Assistant.
"""

from utils.data_preprocessor import load_and_clean_data
from model.anomaly_detector import AnomalyDetector
from rca.rca_engine import RCAEngine
from automation.self_heal import SelfHealAutomation
from ui.dashboard import launch_dashboard

def main():
    # Specify your data file path
    data_filepath = "data/mock_syslog.csv"
    
    # Load and preprocess data
    data = load_and_clean_data(data_filepath)
    
    # Detect anomalies
    detector = AnomalyDetector()
    detector.fit(data)
    anomalies = detector.predict(data)
    
    # Root Cause Analysis
    rca = RCAEngine()
    rca_results = rca.analyze(data)
    
    # Trigger self-healing if necessary
    automation = SelfHealAutomation()
    automation.trigger(rca_results)
    
    # Launch dashboard
    launch_dashboard()

if __name__ == "__main__":
    main()