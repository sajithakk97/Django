from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Class, Attendance
from .forms import AttendanceMarkForm
from django.http import HttpResponse

def attendance_view(request, class_id):
    class_session = get_object_or_404(Class, id=class_id)
    students = Student.objects.all()
    attendance_records = Attendance.objects.filter(class_session=class_session, date=request.GET.get('date', None))

    if request.method == "POST":
        for student in students:
            is_present = request.POST.get(f'is_present_{student.id}', 'off') == 'on'
            Attendance.objects.update_or_create(
                student=student,
                class_session=class_session,
                date=request.POST.get('date'),
                defaults={'is_present': is_present}
            )
        return redirect('attendance_success')  # Replace with your success URL

    return render(request, 'attendance.html', {
        'class_session': class_session,
        'students': students,
        'attendance_records': attendance_records
    })
