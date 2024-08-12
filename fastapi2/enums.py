from enum import Enum

class ServiceName(str, Enum):
    OPENAI = "openai"
    PHI = "phi"
    LLAMA = "llama"

class AnalysisStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

class FailureReason(str, Enum):
    INVALID_PROMPT = "INVALID_PROMPT"
    TRANSCRIPT_ERROR = "TRANSCRIPT_ERROR"
    PROCESSING_ERROR = "PROCESSING_ERROR"
