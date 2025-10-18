class Main:
    """
    a main page that handles overall subject addition, modification, and deletion

    """
    def sub_add(subect):
        """
        Adding a new subject that has not been added already to the Subject
        >>>list(Subject)
        ["Computer Science", "Chemistry", "Physics"]
        >>>sub_add("Biology")
        >>>list(Subject)
        ["Computer Science", "Chemistry", "Physics", "Biology"]
        """


    def sub_modify(subject, new_name):
        """
        modifying the subject's name
        >>>list(Subject)
        ["Computer Science", "Chemistry", "Physics"]
        >>>print(subject("Chemistry"))
        ["Chemistry", {"Unit 1 Test": 94, "Lab Report Assignment": 100}, 97]
        >>>sub_modify_name("Chemistry", "SCH4U")
        >>>list(Subject)
        ["Computer Science", "SCH4U", "Physics"]
        >>>print(subject("SCH4U"))
        ["SCH4U", {"Unit 1 Test": 94, "Lab Report Assignment": 100}, 97]
        """


    def sub_delete(subect):
        """
        removing an existing subject and its following grades and assessments
        >>>list(Subject)
        ["Computer Science", "SCH4U", "Physics"]
        >>>sub_delete("SCH4U")
        >>>list(Subject)
        ["Computer Science", "Physics", "Biology"]
        """


class Predictor:
    """
    helps predict the final score based on current progress by using the Calculator

    """

class Simulator:
    """
    uses Calculator and Predictor to simulate various situations and approximate grades

    """

class Calculator:
    """
    helps computations of each Subject and uses the Assessment for calculations
    calculates depending on the weight of each Assessment

    """

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