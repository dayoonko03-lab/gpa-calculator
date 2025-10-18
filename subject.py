class Subject:
    """
    an individual subject

    === Instance Attributes ===
    name: the name or code of the subject
    assessments: the assessments for each grade in the subject
    current grade: a total grade in the subject

    === Sample Usage ===
    >>>subject = Subject("Computer Science", {"Python Assignment": 98, "Test_1": 94, "Test_2": 93}, 95)
    >>>subject.name == "Computer Science"
    True
    >>>subject.assessments["Python Assignment"]
    98
    >>>subject.assessment["Test_1"] == 93
    False
    >>>subject.current_grade
    95
    """