import json
import os
from pathlib import Path
from configs.app_config import DEFAULT_LANGUAGE

class I18n:
    _translations = {}
    _fallback_translations = {}
    _current_lang = DEFAULT_LANGUAGE
    
    # Root directory of the project
    _base_dir = Path(__file__).parent.parent

    @classmethod
    def _get_lang_path(cls, lang):
        return cls._base_dir / "configs" / "languages" / f"{lang}.json"

    @classmethod
    def load_language(cls, lang=None):
        if lang:
            cls._current_lang = lang
            
        file_path = cls._get_lang_path(cls._current_lang)
        
        # Load main language
        success = cls._load_into(cls._translations, file_path)
        
        # Load fallback language if it's different from current
        if cls._current_lang != DEFAULT_LANGUAGE:
            fallback_path = cls._get_lang_path(DEFAULT_LANGUAGE)
            cls._load_into(cls._fallback_translations, fallback_path)
            
        return success

    @classmethod
    def _load_into(cls, target_dict, file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    target_dict.clear()
                    target_dict.update(content)
                return True
            except Exception as e:
                print(f"Error loading language file {file_path}: {e}")
        return False

    @classmethod
    def set_language(cls, lang):
        if cls.load_language(lang):
            return True
        return False

    @classmethod
    def t(cls, key_path):
        if not cls._translations:
            cls.load_language()
            
        # Try current language
        val = cls._get_value(cls._translations, key_path)
        if val is not None:
            return val
            
        # Try fallback language
        if cls._fallback_translations:
            val = cls._get_value(cls._fallback_translations, key_path)
            if val is not None:
                return val
                
        return f"[{key_path}]"

    @classmethod
    def _get_value(cls, data, key_path):
        keys = key_path.split('.')
        value = data
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return None
