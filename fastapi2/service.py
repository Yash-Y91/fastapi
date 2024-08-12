from enums import ServiceName, AnalysisStatus, FailureReason
from schema import ReportPayload, ReportResponse

class GenAIParent:
    _registry = {}

    def __init_subclass__(cls, key=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if key is None:
            raise ValueError(f"Subclasses of {cls.__name__} must define a 'key' when inheriting")
        if key in cls._registry:
            raise ValueError(f"Key {key} already exists in registry")
        cls._key = key  # Set the key at the class level
        cls._registry[key] = cls
        print(f"Registered subclass {cls.__name__} with key {key}")

    @property
    def key(self):
        return self._key

    @classmethod
    def get_class(cls, key):
        if key not in cls._registry:
            raise ValueError(f'Key {key} not found in registry')
        return cls._registry[key]

    def execute(self, payload):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses automatically registered through __init_subclass__

class OpenAI(GenAIParent, key=ServiceName.OPENAI):
    def execute(self, payload):
        print(f"Executing OpenAI with payload: {payload}")
        # Dummy processing logic
        return {"tone": "neutral", "topics": ["order support"]}

class Phi(GenAIParent, key=ServiceName.PHI):
    def execute(self, payload):
        print(f"Executing Phi with payload: {payload}")
        # Dummy processing logic
        return {"tone": "positive", "topics": ["account management"]}

class Llama(GenAIParent, key=ServiceName.LLAMA):
    def execute(self, payload):
        print(f"Executing Llama with payload: {payload}")
        # Dummy processing logic
        return {"tone": "negative", "topics": ["technical support"]}
