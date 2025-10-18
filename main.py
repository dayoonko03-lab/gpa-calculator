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
