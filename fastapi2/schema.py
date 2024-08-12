from pydantic import BaseModel
from typing import Dict, Optional
from enums import AnalysisStatus, FailureReason

class TranscriptAnalyticsPrompt(BaseModel):
    prompt_id: str
    prompt: str

class ReportPayload(BaseModel):
    session_id: str
    transcript: Dict
    transcript_analytics_prompt: TranscriptAnalyticsPrompt

class ReportResponse(BaseModel):
    session_id: str
    transcript_analytics: Optional[Dict] = None
    status: AnalysisStatus
    reason: Optional[FailureReason] = None
