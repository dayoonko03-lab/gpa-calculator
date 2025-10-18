class Assessment:
    """
    creates an entire ecosystem of assessment

    === Instance Attributes ===
    name: the name or title of the assessments
    type: Assessment type, such as assignment, test, or quiz.
    grade: the graded mark of the assessments
    maximum grade: the possible maximum grades of the assessment
    weight: the weight of the assessment in percent; A greater weight has a larger impact on the total grade

    === Sample Usage ===
    >>>assessment = Assessment("Python Assignment", Assignment, 98, 100, 5.0)
    >>>assessment.name
    "Python Assignment
    >>>assessment.type == Assignment
    True
    >>>assessment.grade
    98
    >>>assessment.max_grade == 100
    True
    >>>assessment.weight == 6
    False
    """