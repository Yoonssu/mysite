from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #생성 내용 max 200자
    pub_date = models.DateTimeField('date published') #생성 날짜

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #선택에 해당하는 질문 (ForeignKey : 위의 Question이라는 모델을 참조하겠다.)
    #cascade는 Question 내용이 삭제되면 밑의 내용도 같이 삭제
    choice_text = models.CharField(max_length=200) # 선택 내용 = 문자
    votes = models.IntegerField(default=0) # 투표=숫자
