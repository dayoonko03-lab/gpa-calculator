from typing import List
from course_page.section import Section

class Assessment:
    """

    >>> quiz = Assessment("Quiz", 0.20)
    >>> quiz_one = Section("Quiz - 1", 8.0, 10.0, 0.05)
    >>> quiz_two = Section("Quiz - 2", 10.0, 10.0, 0.15)
    >>> quiz.add_section(quiz_one)
    >>> quiz.add_section(quiz_two)
    >>> quiz.get_average()
    95.0
    """
    name: str
    weight_from_total: float
    section_lst: List[Section]
