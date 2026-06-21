
# Flooded Tubular Lead-Acid Life Prediction Dashboard

## Objective
Estimate battery State of Health (SOH) and Remaining Useful Life (RUL) using:
- Capacity measurements
- Electrochemical Impedance Spectroscopy (EIS)
- Water loss measurements

## Experiments Required

### 1. Baseline Characterization (Beginning of Life)
Measure:
- Rated Capacity (C20)
- Rs from EIS
- Rct from EIS
- CPE value from EIS fit
- Initial electrolyte inventory

Conditions:
- 25°C
- Fully charged
- Rest 12–24 h before EIS

### 2. Accelerated Cycle-Life Test
Recommended:
- 80% DoD
- Recharge to 100%
- 45°C or 55°C chamber

Record every 100 cycles:
- Capacity
- EIS spectrum (10 kHz to 10 mHz)
- Water consumption
- Internal resistance

### 3. Positive Grid Corrosion Test
Float:
- 2.45–2.50 V/cell
- 60–75°C

Measure:
- Grid growth
- Weight loss
- Corrosion thickness

### 4. Water Loss Test
Float:
- 2.27–2.30 V/cell
- Elevated temperature

Measure:
- Water replenishment required
- g/Ah loss rate

### 5. EIS Procedure
SOC:
- 100% SOC preferred

Amplitude:
- 5–10 mV AC perturbation

Frequency sweep:
- 10 kHz down to 10 mHz

Fit equivalent circuit:
Rs + (Rct || CPE) + Warburg

Extract:
- Rs
- Rct
- CPE
- CPE exponent n

## Calibration Strategy

Build dataset:

Cycle | Capacity | Rs | Rct | CPE | Water Loss | Failure
------|----------|----|-----|-----|------------|--------

Fit regression or ML model:
SOH = f(Capacity,Rct,Rs,CPE,Water Loss)

End-of-life definition:
- Capacity < 80% rated
or
- Rct exceeds critical threshold
or
- Water inventory below maintenance threshold

## Running Dashboard

Install:
pip install streamlit

Run:
streamlit run battery_life_dashboard.py
