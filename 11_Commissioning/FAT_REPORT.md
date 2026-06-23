# FACTORY ACCEPTANCE TEST (FAT)

Project:
Mini Process Plant Digital Twin with AI-Based Predictive Maintenance

Date:
23 June 2026

Prepared By:
Yuarajan Senthilkumar

--------------------------------------------------

SYSTEM UNDER TEST

✓ MQTT Broker

✓ Data Publisher

✓ Historian Logger

✓ Historian Database

✓ AI Fault Detection Model

✓ Digital Twin Dashboard

✓ Maintenance Recommendation Engine

--------------------------------------------------

TEST RESULTS

1. MQTT Communication

Expected:
Publisher communicates with subscriber.

Result:
PASS

--------------------------------------------------

2. Historian Logging

Expected:
Process values stored in CSV historian.

Result:
PASS

--------------------------------------------------

3. Dashboard Display

Expected:
Live process values visible.

Result:
PASS

--------------------------------------------------

4. AI Normal Detection

Expected:
NORMAL

Result:
PASS

--------------------------------------------------

5. AI Low Pressure Detection

Expected:
LOW PRESSURE

Result:
PASS

--------------------------------------------------

6. AI High Pressure Detection

Expected:
HIGH PRESSURE

Result:
PASS

--------------------------------------------------

7. AI Low Flow Detection

Expected:
LOW FLOW

Result:
PASS

--------------------------------------------------

8. AI High Temperature Detection

Expected:
HIGH TEMPERATURE

Result:
PASS

--------------------------------------------------

9. AI Combined Fault Detection

Expected:
COMBINED FAULT

Result:
PASS

--------------------------------------------------

OVERALL FAT RESULT

PASS

Validation Cases:
6

Passed:
6

Failed:
0

Success Rate:
100%
