"""
Configuration Management Module
Centralizes all project settings, paths, and constants.
"""

import os
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """
    Centralized configuration class for TIE project.
    All paths and constants are managed here to avoid hardcoding.
    """
    
    # ==================== PROJECT INFO ====================
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "TIE")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION", "1.0.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # ==================== BASE PATHS ====================
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    SRC_DIR: Path = BASE_DIR / "src"
    DATA_DIR: Path = BASE_DIR / "data"
    OUTPUTS_DIR: Path = BASE_DIR / "outputs"
    TESTS_DIR: Path = BASE_DIR / "tests"
    NOTEBOOKS_DIR: Path = BASE_DIR / "notebooks"
    DASHBOARD_DIR: Path = BASE_DIR / "dashboard"
    
    # ==================== DATA PATHS ====================
    RAW_DATA_PATH: Path = DATA_DIR / os.getenv("RAW_DATA_PATH", "raw")
    PROCESSED_DATA_PATH: Path = DATA_DIR / os.getenv("PROCESSED_DATA_PATH", "processed")
    SAMPLE_DATA_PATH: Path = DATA_DIR / os.getenv("SAMPLE_DATA_PATH", "sample")
    
    # ==================== OUTPUT PATHS ====================
    FIGURES_OUTPUT_PATH: Path = OUTPUTS_DIR / "figures"
    REPORTS_OUTPUT_PATH: Path = OUTPUTS_DIR / "reports"
    EXPORTS_OUTPUT_PATH: Path = OUTPUTS_DIR / "exports"
    
    # ==================== ANALYSIS PARAMETERS ====================
    # Satisfaction scoring
    SATISFACTION_THRESHOLD: int = int(os.getenv("SATISFACTION_THRESHOLD", "2"))
    SATISFACTION_MIN: int = 1
    SATISFACTION_MAX: int = 5
    
    # Topic modeling
    NUM_TOPICS: int = int(os.getenv("NUM_TOPICS", "5"))
    MIN_TOPIC_WORDS: int = int(os.getenv("MIN_TOPIC_WORDS", "10"))
    MAX_TOPIC_WORDS: int = int(os.getenv("MAX_TOPIC_WORDS", "20"))
    
    # TF-IDF parameters
    TFIDF_MAX_FEATURES: int = 1000
    TFIDF_MIN_DF: int = 2
    TFIDF_MAX_DF: float = 0.8
    TFIDF_NGRAM_RANGE: tuple = (1, 2)
    
    # LDA parameters
    LDA_MAX_ITER: int = 50
    LDA_RANDOM_STATE: int = 42
    LDA_N_JOBS: int = -1
    
    # ==================== NLP SETTINGS ====================
    STOPWORDS_LANGUAGE: str = "english"
    LEMMATIZE: bool = True
    MIN_WORD_LENGTH: int = 3
    
    # ==================== SENTIMENT ANALYSIS ====================
    SENTIMENT_THRESHOLD_POSITIVE: float = 0.05
    SENTIMENT_THRESHOLD_NEGATIVE: float = -0.05
    
    # ==================== VISUALIZATION SETTINGS ====================
    # Color schemes
    COLOR_PALETTE: list = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ]
    
    DISSATISFACTION_COLOR: str = '#d62728'
    SATISFACTION_COLOR: str = '#2ca02c'
    NEUTRAL_COLOR: str = '#ff7f0e'
    
    # Chart defaults
    CHART_HEIGHT: int = 500
    CHART_WIDTH: int = 800
    CHART_TEMPLATE: str = "plotly_white"
    
    # WordCloud settings
    WORDCLOUD_WIDTH: int = 1200
    WORDCLOUD_HEIGHT: int = 600
    WORDCLOUD_BACKGROUND: str = 'white'
    WORDCLOUD_COLORMAP: str = 'viridis'
    WORDCLOUD_MAX_WORDS: int = 100
    
    # ==================== DASHBOARD SETTINGS ====================
    DASHBOARD_PORT: int = int(os.getenv("DASHBOARD_PORT", "8501"))
    DASHBOARD_HOST: str = os.getenv("DASHBOARD_HOST", "localhost")
    DASHBOARD_TITLE: str = "TIE - Trivin Insight Engine"
    DASHBOARD_LAYOUT: str = "wide"
    
    # ==================== LOGGING ====================
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: Path = OUTPUTS_DIR / "app.log"
    LOG_FORMAT: str = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
    LOG_ROTATION: str = "10 MB"
    LOG_RETENTION: str = "30 days"
    
    # ==================== DATA GENERATION ====================
    # Sample data generation settings
    SAMPLE_NUM_EMPLOYEES: int = 500
    SAMPLE_NUM_RESPONSES: int = 2000
    SAMPLE_START_DATE: str = "2023-01-01"
    SAMPLE_END_DATE: str = "2024-12-31"
    SAMPLE_SURVEY_ROUNDS: int = 4
    
    # Departments
    DEPARTMENTS: list = [
        "Engineering",
        "Sales",
        "Marketing",
        "HR",
        "Finance",
        "Operations",
        "Customer Support",
        "Product"
    ]
    
    # Age groups
    AGE_GROUPS: list = ["18-25", "26-35", "36-45", "46-55", "56+"]
    
    # Dissatisfaction themes for sample data generation
    DISSATISFACTION_THEMES: Dict[str, list] = {
        "workload": [
            "too much work", "overworked", "long hours", "work-life balance",
            "burnout", "unrealistic deadlines", "overwhelming workload"
        ],
        "management": [
            "poor management", "lack of support", "micromanagement",
            "bad leadership", "unclear direction", "poor communication from managers"
        ],
        "growth": [
            "no career growth", "limited opportunities", "stagnant role",
            "no promotion", "lack of development", "need more training"
        ],
        "compensation": [
            "low pay", "unfair salary", "poor benefits", "no raise",
            "compensation issues", "underpaid compared to market"
        ],
        "culture": [
            "toxic culture", "no work-life balance", "lack of recognition",
            "poor team dynamics", "no appreciation", "negative environment"
        ],
        "resources": [
            "outdated tools", "lack of resources", "insufficient budget",
            "need better equipment", "technical debt", "inadequate infrastructure"
        ]
    }
    
    # ==================== FILE FORMATS ====================
    SUPPORTED_DATA_FORMATS: list = [".csv", ".json", ".xlsx", ".parquet"]
    DEFAULT_EXPORT_FORMAT: str = "csv"
    DATE_FORMAT: str = "%Y-%m-%d"
    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    
    # ==================== VALIDATION RULES ====================
    REQUIRED_COLUMNS: list = [
        "response_id",
        "employee_id",
        "department",
        "survey_date",
        "satisfaction_score",
        "response_text"
    ]
    
    OPTIONAL_COLUMNS: list = [
        "survey_round",
        "age_group",
        "tenure_years"
    ]
    
    # ==================== METHODS ====================
    @classmethod
    def ensure_directories(cls) -> None:
        """
        Create all necessary directories if they don't exist.
        
        Returns:
            None
        """
        directories = [
            cls.RAW_DATA_PATH,
            cls.PROCESSED_DATA_PATH,
            cls.SAMPLE_DATA_PATH,
            cls.FIGURES_OUTPUT_PATH,
            cls.REPORTS_OUTPUT_PATH,
            cls.EXPORTS_OUTPUT_PATH,
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def get_config_dict(cls) -> Dict[str, Any]:
        """
        Return all configuration as a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary containing all configuration values
        """
        return {
            key: value for key, value in cls.__dict__.items()
            if not key.startswith('_') and not callable(value)
        }
    
    @classmethod
    def validate_paths(cls) -> bool:
        """
        Validate that all critical paths exist or can be created.
        
        Returns:
            bool: True if all paths are valid, False otherwise
        """
        try:
            cls.ensure_directories()
            return True
        except Exception as e:
            print(f"Path validation failed: {e}")
            return False
    
    @classmethod
    def get_data_file_path(cls, filename: str, data_type: str = "raw") -> Path:
        """
        Get the full path for a data file.
        
        Args:
            filename: Name of the data file
            data_type: Type of data ('raw', 'processed', 'sample')
            
        Returns:
            Path: Full path to the data file
        """
        data_paths = {
            "raw": cls.RAW_DATA_PATH,
            "processed": cls.PROCESSED_DATA_PATH,
            "sample": cls.SAMPLE_DATA_PATH
        }
        
        if data_type not in data_paths:
            raise ValueError(f"Invalid data_type: {data_type}. Must be one of {list(data_paths.keys())}")
        
        return data_paths[data_type] / filename
    
    @classmethod
    def get_output_file_path(cls, filename: str, output_type: str = "figures") -> Path:
        """
        Get the full path for an output file.
        
        Args:
            filename: Name of the output file
            output_type: Type of output ('figures', 'reports', 'exports')
            
        Returns:
            Path: Full path to the output file
        """
        output_paths = {
            "figures": cls.FIGURES_OUTPUT_PATH,
            "reports": cls.REPORTS_OUTPUT_PATH,
            "exports": cls.EXPORTS_OUTPUT_PATH
        }
        
        if output_type not in output_paths:
            raise ValueError(f"Invalid output_type: {output_type}. Must be one of {list(output_paths.keys())}")
        
        return output_paths[output_type] / filename


# Initialize directories on import
Config.ensure_directories()
