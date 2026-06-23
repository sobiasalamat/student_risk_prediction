from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .ml_model import predict_risk


def home(request):
    return HttpResponse("Welcome to Student Risk Prediction System")


def predict(request):
    if request.method == "POST":
        attendance = int(request.POST.get("attendance"))
        assignment = int(request.POST.get("assignment"))
        quiz = int(request.POST.get("quiz"))
        midterm = int(request.POST.get("midterm"))
        lms = int(request.POST.get("lms"))

        # match your model features (10 values example)
        sample_data = [
            attendance, assignment, quiz, midterm, lms,
            80, 75, 70, 65, 60   # dummy remaining features
        ]

        result = predict_risk(sample_data)

        # ✅ LABEL + COLOR MAPPING
        if result == 0:
            label = "High Risk"
            color = "red"

        elif result == 1:
            label = "Low Risk"
            color = "green"

        elif result == 2:
            label = "Medium Risk"
            color = "orange"

        else:
            label = "Invalid Prediction"
            color = "gray"

        return render(request, "predictor/result.html", {
            "prediction": label,
            "color": color,
            "raw_output": result
        })

    return render(request, "predictor/form.html")