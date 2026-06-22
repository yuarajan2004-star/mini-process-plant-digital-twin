nano Engineering/Mechanical/Calculations/MEC-CALC-001.md# Mechanical Design Calculations

Document Number:
MEC-CALC-001

Project:
Mini Process Plant Digital Twin with AI-Based Predictive Maintenance

Prepared By:
Yuarajan Senthilkumar

Date:
22 June 2026

Applicable Standards:

- ASME B31.3
- Crane TP-410
- Darcy-Weisbach Equation
- ISA Guidelines

---

# 1. Tank Sizing Calculation

Required Flow Rate = 180 LPH

Convert:
180 LPH = 3 LPM
Desired Operating Duration = 1 minute

Tank Volume Required
V = Q × t

V = 3 × 1
V = 3 Liters

Selected Tank Capacity = 5 Liters

Safety Factor
SF = 5 / 3
SF = 1.67

Result:
Selected tank size is adequate.

---

# 2. Pipe Flow Calculation

Pipe Internal Diameter
D = 12 mm
D = 0.012 m

Flow Rate
Q = 180 LPH
Q = 0.00005 m³/s

V = Q / A
A = πD²/4

A = 3.1416 × (0.012)² /4
A = 0.000113 m²
V = 0.00005 / 0.000113
V = 0.442 m/s

Flow Velocity
V = 0.442 m/s

Result:
Velocity within acceptable range for water service.

Re = ρVD / μ

ρ = 1000 kg/m³
μ = 0.001 Pa.s
Re = (1000 × 0.442 × 0.012)/0.001
Re = 5304

---

# 3. Reynolds Number

Re = 5304

Interpretation:
Re < 2300 → Laminar
2300–4000 → Transition
Re > 4000 → Turbulent

Result:
Flow is Turbulent.
