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

# 4. Pressure Drop Calculation (DARCY-WEISBACH PRESSURE DROP CALCULATION)

Objective
Calculate frictional pressure loss in the recirculation line.

Given Data
Pipe Length = 2 m
Pipe Diameter = 0.012 m
Flow Velocity = 0.442 m/s
Density = 1000 kg/m³
Friction Factor = 0.037

Formula
hf = f × (L/D) × (V² / 2g)

Calculation
hf = 0.037 × (2 / 0.012) × (0.442² / (2 × 9.81))
hf = 0.061 m

Pressure Loss
ΔP = ρgh

ΔP = 1000 × 9.81 × 0.061
ΔP = 598 Pa
ΔP = 0.006 bar

Result
Pressure drop is negligible.

Engineering Comment
The selected pump can easily overcome this pressure loss.

---

# 5. Pump Total Dynamic Head Calculation

Objective
Determine the Total Dynamic Head (TDH) required for the circulation pump.

Given Data
Static Head = 0.30 m
Friction Head = 0.061 m
Safety Margin = 20%

Formula
TDH = Static Head + Friction Head

Calculation
TDH = 0.30 + 0.061
TDH = 0.361 m

Safety Margin
TDHdesign = TDH × 1.20
TDHdesign = 0.361 × 1.20
TDHdesign = 0.433 m

Result
Required Pump Head = 0.433 m

Engineering Comment
Any pump capable of delivering more than 0.433 m head at the design flow rate is acceptable.

---

# 6. Pump Suitability Verification

Objective
Verify that the selected pump can meet the required Total Dynamic Head.

Given Data
Required Head = 0.433 m
Pump Maximum Head = 1.50 m

Formula
Head Margin = Pump Head / Required Head

Calculation
Head Margin = 1.50 / 0.433
Head Margin = 3.46

Result
Pump head exceeds design requirement.

Engineering Comment
The selected pump provides approximately 3.5 times the required head and is suitable for operation.

---

# 7. Valve Cv Calculation

Objective
Determine the minimum valve flow coefficient required for the design flow.

Given Data
Flow Rate = 180 LPH
Flow Rate = 3 LPM
Flow Rate = 0.79 GPM
Pressure Drop Across Valve = 0.10 psi
Specific Gravity of Water = 1.0

Formula
Cv = Q × √(SG / ΔP)

Where
Cv = Valve Flow Coefficient
Q = Flow Rate (GPM)
SG = Specific Gravity
ΔP = Pressure Drop (psi)

Calculation
Cv = 0.79 × √(1.0 / 0.10)
Cv = 0.79 × 3.162
Cv = 2.50

Result
Required Valve Cv = 2.50

Engineering Comment
Any valve with Cv greater than 2.50 can satisfy the design flow requirement.

---

# 8. Valve Suitability Verification

Objective
Verify the selected valve can meet the required Cv.

Given Data
Required Cv = 2.50
Typical 1/2 inch PVC Ball Valve Cv = 15

Formula
Cv Margin = Valve Cv / Required Cv

Calculation
Cv Margin = 15 / 2.50
Cv Margin = 6.0

Result
Selected valve exceeds the required flow capacity.

Engineering Comment
The selected 1/2 inch PVC ball valve is adequately sized for this application.

