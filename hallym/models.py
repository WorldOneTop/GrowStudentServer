from django.db import models

class User(models.Model):
    userId=models.CharField(max_length=32)
    userPw=models.CharField(max_length=64)

class UserInfo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    hp = models.IntegerField()
    speed = models.IntegerField()
    hpStr = models.CharField(max_length=10)
    _int = models.IntegerField()
    intStr = models.CharField(max_length=10)
    duty = models.IntegerField()
    dutyStr = models.CharField(max_length=10)

    # lateinit var id: String
    # var x: Float=0f //위치는 상단 왼쪽으로
    # var y: Float=0f //위치는 상단 왼쪽으로
    # var hp:Int=0 // 체력
    # var speed:Int=0 // 이속
    # lateinit var hpStr:String // 나타내는 값  ex: 421K, 12M
    # var int:Int=0 // 지능
    # lateinit var intStr:String // 나타내는 값
    # var duty:Int=0 // 효도 , 달마다 용돈 양
    # lateinit var dutyStr:String