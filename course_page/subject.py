class Subject:
    """
    an individual subject

    === Instance Attributes ===
    name: the name of the subject
    code: the course code of the subject
    assessments: the assessments for each grade in the subject
    current grade: a total grade in the subject

    === Sample Usage ===
    >>> quiz_assessment = Assessment("Quiz")
    >>> subject = Subject("Computer Science", {Asssessment}, 95)
    >>>subject.name == "Computer Science"
    True
    >>>subject.assessments["Python Assignment"]
    98
    >>>subject.assessment["Test_1"] == 93
    False
    >>>subject.current_grade
    95
    """
    pass
