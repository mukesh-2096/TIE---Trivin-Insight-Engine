# TIE - Trivin Insight Engine

**Employee Engagement Survey Analysis Platform**

A comprehensive Python-based analytics platform for uncovering dissatisfaction themes, department-wise trends, and time-based changes in employee engagement survey data.

---

## 📋 Table of Contents

- [Problem Statement](#problem-statement)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Module Documentation](#module-documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Problem Statement

A company conducting employee engagement surveys wants to understand what drives dissatisfaction but only has raw survey responses. **TIE** solves this by:

1. **Identifying Common Dissatisfaction Themes** via NLP and topic modeling
2. **Analyzing Department-wise Trends** to pinpoint problem areas
3. **Tracking Changes Over Time** to monitor sentiment evolution

---

## ✨ Features

- 📊 **Automated Theme Extraction** - LDA topic modeling on dissatisfied responses
- 🎭 **Sentiment Analysis** - VADER-based sentiment scoring with cross-validation
- 📈 **Department Analytics** - Dissatisfaction rates and theme breakdown by department
- ⏰ **Time-series Analysis** - Trend detection and spike identification
- 🎨 **Rich Visualizations** - Interactive Plotly charts, word clouds, heatmaps
- 🚀 **Streamlit Dashboard** - Multi-page interactive dashboard with filters
- 🧪 **Full Test Coverage** - Pytest unit tests for all core modules
- 📝 **Synthetic Data Generator** - Realistic sample data for testing

---

## 📁 Project Structure

```
TIE/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── data/
│   ├── raw/              # Raw survey data files
│   ├── processed/        # Cleaned and preprocessed data
│   └── sample/           # Synthetic data generation scripts
├── notebooks/
│   ├── 01_eda.ipynb              # Exploratory Data Analysis
│   ├── 02_theme_analysis.ipynb   # Theme extraction experiments
│   ├── 03_dept_trends.ipynb      # Department analysis
│   └── 04_time_analysis.ipynb    # Time-series analysis
├── src/
│   ├── __init__.py
│   ├── config.py         # Centralized configuration
│   ├── data/
│   │   ├── loader.py     # Data loading utilities
│   │   ├── cleaner.py    # Data cleaning functions
│   │   └── preprocessor.py  # Text preprocessing
│   ├── analysis/
│   │   ├── theme_extractor.py   # LDA topic modeling
│   │   ├── sentiment.py         # Sentiment analysis
│   │   ├── dept_analyzer.py     # Department analytics
│   │   └── time_analyzer.py     # Time-series analysis
│   ├── visualization/
│   │   ├── charts.py            # Plotly chart generators
│   │   ├── wordcloud_gen.py     # WordCloud generation
│   │   └── dashboard.py         # Dashboard utilities
│   └── utils/
│       ├── logger.py     # Logging configuration
│       └── helpers.py    # Helper functions
├── dashboard/
│   └── app.py           # Streamlit dashboard application
├── outputs/
│   ├── figures/         # Generated visualizations
│   ├── reports/         # Analysis reports
│   └── exports/         # Exported data files
└── tests/
    ├── test_loader.py
    ├── test_cleaner.py
    ├── test_sentiment.py
    └── test_theme_extractor.py
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Core** | Python 3.10+ |
| **Data Processing** | pandas, numpy |
| **NLP** | nltk, scikit-learn, VADER, TextBlob |
| **Topic Modeling** | LDA (Latent Dirichlet Allocation) |
| **Visualization** | Plotly, Matplotlib, Seaborn, WordCloud |
| **Dashboard** | Streamlit |
| **Testing** | pytest |
| **Configuration** | python-dotenv |
| **Logging** | loguru |

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TIE-Trivin-Insight-Engine
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**
   ```python
   python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt')"
   ```

5. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

---

## ⚡ Quick Start

### 1. Generate Sample Data

```bash
python data/sample/generate_sample_data.py
```

### 2. Run the Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open at `http://localhost:8501`

### 3. Run Tests

```bash
pytest tests/ -v
```

---

## 📖 Usage

### Data Loading

```python
from src.data.loader import DataLoader
from src.config import Config

loader = DataLoader()
df = loader.load_csv(Config.get_data_file_path("survey_data.csv", "raw"))
```

### Data Cleaning

```python
from src.data.cleaner import DataCleaner

cleaner = DataCleaner()
cleaned_df = cleaner.clean(df)
```

### Sentiment Analysis

```python
from src.analysis.sentiment import SentimentAnalyzer

analyzer = SentimentAnalyzer()
df = analyzer.analyze_sentiment(df)
```

### Theme Extraction

```python
from src.analysis.theme_extractor import ThemeExtractor

extractor = ThemeExtractor(num_topics=5)
df = extractor.fit_transform(df)
themes = extractor.get_theme_labels()
```

### Visualization

```python
from src.visualization.charts import plot_dissatisfaction_by_dept

fig = plot_dissatisfaction_by_dept(df)
fig.show()
```

---

## 📚 Module Documentation

### `src/config.py`
Centralized configuration management. All paths, constants, and settings are defined here to avoid hardcoding.

### `src/data/loader.py`
Loads survey data from various formats (CSV, JSON, Excel, Parquet).

### `src/data/cleaner.py`
Handles null values, duplicates, date parsing, and data validation.

### `src/data/preprocessor.py`
Text preprocessing: lowercasing, tokenization, stopword removal, lemmatization.

### `src/analysis/sentiment.py`
VADER sentiment analysis with compound scores and label classification.

### `src/analysis/theme_extractor.py`
TF-IDF vectorization and LDA topic modeling for theme extraction.

### `src/analysis/dept_analyzer.py`
Department-level dissatisfaction metrics and theme analysis.

### `src/analysis/time_analyzer.py`
Time-series analysis, trend detection, and spike identification.

### `src/visualization/charts.py`
Plotly-based interactive charts (bar charts, line charts, heatmaps).

### `src/visualization/wordcloud_gen.py`
WordCloud generation for themes and departments.

### `dashboard/app.py`
Multi-page Streamlit dashboard with interactive filters.

---

## 🧪 Testing

Run all tests:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ --cov=src --cov-report=html
```

Run specific test file:
```bash
pytest tests/test_sentiment.py -v
```

---

## 📊 Dashboard Features

The Streamlit dashboard includes 4 pages:

1. **Overview** - KPI cards, satisfaction distribution
2. **Theme Analysis** - LDA themes, word clouds, theme filters
3. **Department Trends** - Department comparison, heatmaps
4. **Time Trends** - Time-series charts, trend analysis

**Sidebar Filters:**
- Department selector
- Date range picker
- Survey round filter

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Code Standards:**
- Follow PEP8 style guide
- Add type hints to all functions
- Include docstrings (Google style)
- Write unit tests for new features
- Use `loguru` for logging (no print statements)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Authors

**TIE Development Team**

---

## 🙏 Acknowledgments

- VADER Sentiment Analysis tool
- scikit-learn for topic modeling
- Plotly for interactive visualizations
- Streamlit for rapid dashboard development

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the development team

---

**Built with ❤️ for better employee engagement insights**
