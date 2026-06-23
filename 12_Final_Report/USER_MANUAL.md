USER MANUAL

1. Start MQTT Broker

sudo systemctl start mosquitto

2. Start Historian Logger

python3 mqtt_logger.py

3. Start Data Publisher

python3 publisher_normal.py

4. Start Dashboard

streamlit run app.py

5. Open Dashboard

http://localhost:8501

6. Review AI Prediction

7. Review Maintenance Recommendation

8. Review Historian Trends
