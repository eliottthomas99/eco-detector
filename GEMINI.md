# Eco-Detector: Project Context & Guidelines

## Project Mission
Building a production-grade AI Engineering system for detecting environmental pollutants in the wild. This project serves as a portfolio piece to demonstrate PhD-level expertise in object detection and low-data regimes, transitioned into a robust, deployment-ready engineering framework.

## Collaboration Protocol: "Expert Co-Pilot"
To ensure the user (PhD Researcher) leads the architectural and technical direction:
1. **Consultation First:** For every major design choice (dataset, model architecture, loss function, augmentation strategy, etc.), I must present 2-3 options with trade-offs.
2. **Never Assume:** Do not autocomplete decisions or fill in missing information without explicit user supervision. If in doubt, ask for clarification first.
3. **User Decision:** Implementation only begins after the user has selected or provided a specific direction.
4. **No Hidden Logic:** I will explain the rationale behind implementation details, focusing on modularity and engineering best practices.

## Technical Standards
- **Language:** Python 3.12+ with mandatory **Type Hints**.
- **Documentation:** Google-style docstrings for all functions and classes.
- **Structure:** Modular `src/` layout.
- **Data Versioning:** **DVC** (Data Version Control) for reproducibility and lineage.
- **Environment Management:** **uv** (high-performance package manager).
- **Configuration:** **Hydra** (with Optuna Sweeper for HPO).
- **Experiment Tracking:** **Weights & Biases** (W&B) for public-facing reports.
- **Testing:** `pytest` for unit and integration tests.
- **Optimization Target:** Efficient CPU inference via OpenVINO.

## Core Mandates
- **Avoid Overengineering:** Prioritize simplicity and results. Use existing scripts and tools as-is whenever possible; do not build complex wrappers or abstractions unless absolutely necessary.
- **Reproducibility:** Use DVC for data versioning and explicit dependency management.
- **Adaptability:** Demonstrate the transition from document-based AI to environmental computer vision.
- **Low-Data Expertise:** Highlight custom loss functions, pseudo-labeling, and active learning strategies.
