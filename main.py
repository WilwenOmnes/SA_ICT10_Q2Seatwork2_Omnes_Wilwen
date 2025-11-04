from pyscript import display, document

def general_weighted_average(e):
    document.getElementById('student_info').innerHTML = ''
    document.getElementById('summary').innerHTML = ''
    document.getElementById('output').innerHTML = ''

    subjects = ['Science', 'Math', 'English', 'Filipino', 'SS', 'PE']
    ids = ['science', 'math', 'english', 'filipino', 'ss', 'pe']

    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()
    institution = document.getElementById('institution').value.strip()
    grade_section = document.getElementById('grade_section').value.strip()

    if not first_name or not last_name or not institution or not grade_section:
        display("Please fill in all personal information fields.", target="output")
        return

    grades = []
    for i in ids:
        value = document.getElementById(i).value.strip()
        if not value:
            display("Please fill in all grade fields before calculating.", target="output")
            return
        try:
            grade = float(value)
        except:
            display("Invalid input: please enter only numbers.", target="output")
            return
        if grade < 60 or grade > 100:
            display("Error: Grades must be between 60 and 100 only.", target="output")
            return
        grades.append(grade)

    weights = {'Science': 2.0, 'Math': 2.0, 'English': 2.0, 'Filipino': 1.0, 'SS': 1.0, 'PE': 0.5}
    weighted_sum = sum(g * weights[sub] for g, sub in zip(grades, subjects))
    gwa = weighted_sum / sum(weights.values())

    display(f"Name: {first_name} {last_name}", target="student_info")
    display(f"Institution: {institution}", target="student_info")
    display(f"Grade & Section: {grade_section}", target="student_info")
    display(f"GWA: {gwa:.2f}", target='output')
