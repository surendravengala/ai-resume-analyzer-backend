from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeSerializer
from .utils.parser import extract_text
from .utils.ai_service import analyze_with_ai
from .utils.matcher import calculate_match

class AnalyzeResumeView(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            resume_file = serializer.validated_data['resume']
            job_desc = serializer.validated_data['job_description']

            # Step 1: Extract text
            resume_text = extract_text(resume_file)

            # Step 2: AI extraction
            ai_result = analyze_with_ai(resume_text, job_desc)

            # Step 3: Matching logic
            final_result = calculate_match(ai_result, resume_text)
            return Response({
                "message": "Analysis complete ✅",
                "data": final_result
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)