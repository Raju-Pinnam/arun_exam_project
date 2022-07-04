from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Subject(models.Model):
    subject_name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.subject_name

class Question(models.Model):
    question = models.CharField(max_length=256)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    question_marks = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.question} - {self.subject} - {self.question_marks}"

class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Answer is for {self.question}"

class TestPaper(models.Model):
    number_of_questions = models.IntegerField()
    questions = models.ManyToManyField(Question)
    total_marks = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    setter = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="set_papers")
    checker = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               related_name="checked_papers",
                               blank=True,
                               null=True)
    examiner = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               related_name="examined_papers",
                               blank=True,
                               null=True)
    checker_review = models.TextField(blank=True,
                               null=True)
    examiner_review = models.TextField(blank=True,
                               null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Test Paper Created by {self.setter}"
