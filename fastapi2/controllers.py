from fastapi import FastAPI, HTTPException
from schema import ReportPayload, ReportResponse
from service import GenAIParent
from enums import ServiceName, AnalysisStatus, FailureReason

app = FastAPI()

@app.post("/genAI/{service_name}/reports", response_model=ReportResponse)
async def generate_report(service_name: ServiceName, report_payload: ReportPayload):
    try:
        service_class = GenAIParent.get_class(service_name)
        transcript_analytics = service_class().execute(report_payload.transcript)
        return ReportResponse(
            session_id=report_payload.session_id,
            transcript_analytics=transcript_analytics,
            status=AnalysisStatus.SUCCESS
        )
    except ValueError as e:
        return ReportResponse(
            session_id=report_payload.session_id,
            status=AnalysisStatus.FAILURE,
            reason=FailureReason.PROCESSING_ERROR
        )
