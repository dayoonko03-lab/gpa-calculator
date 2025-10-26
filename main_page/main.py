ffrom typing import List
from course_page.subject import Subject

class Main:
    """
    a main page that handles overall subject addition, modification, and deletion

    >>> main_page = Main()
    >>> gr_10_math = Subject("Grade 10 Math")
    >>> main_page.sub_add(gr_10_math)
    >>> gr_10_chem = Subject("Grade 10 Chemistry")
    >>> main_page.sub_add(gr_10_chem)
    >>> gr_10_math in main_page.subject_lst
    True
    >>> gr_10_chem in main_page.subject_lst
    True
    """
    subject_lst: List[Subject]

    def __init__(self) -> None:
        self.subject_lst = []

    def sub_add(self, subject: Subject) -> None:
        """
        Adding a new subject that has not been added already to the Subject

        >>> main_page = Main()
        >>> gr_10_math = Subject("Grade 10 Math")
        >>> main_page.sub_add(gr_10_math)
        >>> gr_10_chem = Subject("Grade 10 Chemistry")
        >>> main_page.sub_add(gr_10_chem)
        >>> gr_10_math in main_page.subject_lst
        True
        >>> gr_10_chem in main_page.subject_lst
        True
        """
        if subject not in self.subject_lst:
            self.subject_lst.append(subject)

    def sub_delete(self, subject: Subject):
        """
        Remove <subject> if it exists in <self.subject_lst>

        >>> main_page = Main()
        >>> gr_10_math = Subject("Grade 10 Math")
        >>> main_page.sub_add(gr_10_math)
        >>> gr_10_chem = Subject("Grade 10 Chemistry")
        >>> main_page.sub_add(gr_10_chem)
        >>> gr_10_math in main_page.subject_lst
        True
        >>> gr_10_chem in main_page.subject_lst
        True
        >>> main_page.sub_delete(gr_10_math)
        >>> gr_10_math in main_page.subject_lst
        False
        """
        if subject in self.subject_lst:
            self.subject_lst.remove(subject)

if __name__ == "__main__":
    pass
