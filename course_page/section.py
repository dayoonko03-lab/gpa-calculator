class Section:
    """

    === public attribute ===
    name: name of the assessment section
    obtained: obtained score
    total: total obtainable score
    weight: fraction of the weight from total

    >>> quiz_one = Section("Quiz One", 7.0, 10.0, 0.2)
    >>> quiz_one.obtained
    7
    >>> quiz_one.name
    'Quiz One'
    >>> quiz_one.get_percent()
    70.0
    """
    name: str
    obtained: float
    total: float
    weight: float

    pass
