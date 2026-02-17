## Key Features
* **Real-time Gas Monitoring:** Simulates industrial sensors for Methane (%) and Ammonia (ppm).
* **Predictive Analysis:** Implements Linear Regression to predict gas levels 1 second in advance.
* **Cross-Language Integration:** A hybrid architecture combining **Python** (for ML & Data Processing) and **C++** (for Actuator Control & Execution).
* **Autonomous Decision Making:** Automatically triggers exhaust fans via digital signals based on AI-predicted threshold breaches.

## Project Architecture
1.  **Data Producer (Python):** Generates synthetic sensor data mimicking real-world gas fluctuations.
2.  **ML Brain (Python):** * Processes the rolling window of the last 10 seconds.
    * Calculates Confidence Scores ($R^2$) for model reliability.
    * Outputs control signals to `sinyal.txt`.
3.  **Actuator Controller (C++):** * Continuously polls the signal file.
    * Executes safety protocols (Fan ON/OFF) with low-latency performance.

## Tech Stack
* **Python:** Pandas, NumPy, Scikit-learn.
* **C++:** Standard Template Library (STL), File I/O.
* **Architecture:** Inter-process Communication (IPC) via File I/O.
