from __future__ import unicode_literals

from django.db import models


class Prospects(models.Model):
    prospect_session = models.CharField(max_length=100, primary_key=True)



class Forms(models.Model):
    question_text1 = models.CharField(max_length=100)
    question_text2 = models.CharField(max_length=100)
    question_text3 = models.CharField(max_length=100)
    question_text4 = models.CharField(max_length=100)
    question_text5 = models.CharField(max_length=100)
    question_text6 = models.CharField(max_length=100)
    question_text7 = models.CharField(max_length=100)
    question_text8 = models.CharField(max_length=100)
    question_text9 = models.CharField(max_length=100)
    question_text10 = models.CharField(max_length=100)
    question_text = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    def getQuestionsMap(self):
        questionsMap = {}
        questionsMap['question1'] = self.question_text1
        questionsMap['question2'] = self.question_text2
        questionsMap['question3'] = self.question_text3
        questionsMap['question4'] = self.question_text4
        questionsMap['question5'] = self.question_text5
        questionsMap['question6'] = self.question_text6
        questionsMap['question7'] = self.question_text7
        questionsMap['question8'] = self.question_text8
        questionsMap['question9'] = self.question_text9
        questionsMap['question10'] = self.question_text10 
        return questionsMap


    def getName(self):
        return self.name

    def getForm(self):
        return {self.getName():self.getQuestionsMap()}


class FormResults(models.Model):
    SUBMIT_STATUS = (('T', 'Done'),('F', 'Dont'),)
    prospect = models.ForeignKey(Prospects)
    form    = models.ForeignKey(Forms)
    question_result1 = models.CharField(max_length = 100) 
    question_result2 = models.CharField(max_length = 100)
    question_result3 = models.CharField(max_length = 100)
    question_result4 = models.CharField(max_length = 100)
    question_result5 = models.CharField(max_length = 100)
    question_result6 = models.CharField(max_length = 100)
    question_result7 = models.CharField(max_length = 100)
    question_result8 = models.CharField(max_length = 100)
    question_result9 = models.CharField(max_length = 100)
    question_result10 = models.CharField(max_length = 100)
    submited = models.CharField(max_length=1, choices= SUBMIT_STATUS, default='F')

    def getResultMap(self):
        import Forms
        formName = Forms.objects.filter(id=self.form).getName()
        resultMap = {}
        resultMap['question1'] = self.question_text1
        resultMap['question2'] = self.question_text2
        resultMap['question3'] = self.question_text3
        resultMap['question4'] = self.question_text4
        resultMap['question5'] = self.question_text5
        resultMap['question6'] = self.question_text6
        resultMap['question7'] = self.question_text7
        resultMap['question8'] = self.question_text8
        resultMap['question9'] = self.question_text9
        resultMap['question10'] = self.question_text10

    def getPercentCompleted(self):
