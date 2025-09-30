import os
import toml
from loguru import logger

def load_vercel_config():
    """Carrega configuração com suporte a variáveis de ambiente da Vercel"""
    
    # Configuração padrão
    config = {
        "app": {
            "video_source": os.getenv("VIDEO_SOURCE", "pexels"),
            "hide_config": os.getenv("HIDE_CONFIG", "false").lower() == "true",
            "pexels_api_keys": [key for key in [os.getenv("PEXELS_API_KEY")] if key],
            "pixabay_api_keys": [key for key in [os.getenv("PIXABAY_API_KEY")] if key],
            "llm_provider": os.getenv("LLM_PROVIDER", "g4f"),
            "subtitle_provider": os.getenv("SUBTITLE_PROVIDER", "edge"),
            "max_concurrent_tasks": int(os.getenv("MAX_CONCURRENT_TASKS", "3")),
            "material_directory": os.getenv("MATERIAL_DIRECTORY", ""),
            "enable_redis": os.getenv("ENABLE_REDIS", "false").lower() == "true",
            "redis_host": os.getenv("REDIS_HOST", "localhost"),
            "redis_port": int(os.getenv("REDIS_PORT", "6379")),
            "redis_db": int(os.getenv("REDIS_DB", "0")),
            "redis_password": os.getenv("REDIS_PASSWORD", ""),
        },
        "openai": {
            "api_key": os.getenv("OPENAI_API_KEY", ""),
            "base_url": os.getenv("OPENAI_BASE_URL", ""),
            "model_name": os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"),
        },
        "gemini": {
            "api_key": os.getenv("GEMINI_API_KEY", ""),
            "model_name": os.getenv("GEMINI_MODEL_NAME", "gemini-1.0-pro"),
        },
        "qwen": {
            "api_key": os.getenv("QWEN_API_KEY", ""),
            "model_name": os.getenv("QWEN_MODEL_NAME", "qwen-max"),
        },
        "deepseek": {
            "api_key": os.getenv("DEEPSEEK_API_KEY", ""),
            "base_url": os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
            "model_name": os.getenv("DEEPSEEK_MODEL_NAME", "deepseek-chat"),
        },
        "g4f": {
            "model_name": os.getenv("G4F_MODEL_NAME", "gpt-4o-mini"),
        },
        "azure": {
            "speech_key": os.getenv("SPEECH_KEY", ""),
            "speech_region": os.getenv("SPEECH_REGION", ""),
        },
        "siliconflow": {
            "api_key": os.getenv("SILICONFLOW_API_KEY", ""),
        },
        "whisper": {
            "model_size": os.getenv("WHISPER_MODEL_SIZE", "large-v3"),
            "device": os.getenv("WHISPER_DEVICE", "CPU"),
            "compute_type": os.getenv("WHISPER_COMPUTE_TYPE", "int8"),
        },
        "ui": {
            "hide_log": os.getenv("HIDE_LOG", "false").lower() == "true",
        }
    }
    
    # Log das configurações carregadas
    logger.info("Configuração carregada com variáveis de ambiente da Vercel")
    logger.info(f"LLM Provider: {config['app']['llm_provider']}")
    logger.info(f"Video Source: {config['app']['video_source']}")
    logger.info(f"Pexels API Key configurada: {'Sim' if config['app']['pexels_api_keys'] else 'Não'}")
    
    return config

# Carrega a configuração
vercel_config = load_vercel_config()
