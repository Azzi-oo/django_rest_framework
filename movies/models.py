from django.db import models
from datetime import date
from . import enums


class Operation(models.Model):
    name = models.TextField(
        verbose_name="Наименование операции",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание операции",
    )
    cost = models.FloatField(
        verbose_name="Стоимость",
    )

    class Meta:
        db_table = 'operation'
        ordering = ['-date_created']
        verbose_name = "Операция"
        verbose_name_plural = "Операции"

    def __str__(self):
        return f"{self.name}"


class GoalType(models.TextChoices):
    """Тип модели"""

    SPENDING = "Трата"
    REFIL = "Пополнение"


class GoalManager(models.Manager):
    def goals(self):
        return self.filter(goal_type=GoalType.REFIL)

    def budgets(self):
        return self.filter(goal_type=enums.GoalType.SPENDING)


class Goal(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название цели",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Название цели",
    )
    goal_type = models.CharField(
        choices=enums.GoalType.choces,
        default=enums.GoalType.SPENDING,
        max_length=32,
        verbose_name="Тип операций цели",
    )
    start_date = models.DateField(
        default=date.today,
        verbose_name="Дата начала цели",
    )
    finish_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата окончания цели",
    )
    value = models.FloatField(
        verbose_name="Значение цели",
    )

    objects = GoalManager()

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

    class GoalManager(models.Manager):
        def goals(self):
            return self.filter(goal_type=GoalType.REFIL)
        
        def budgets(self):
            return self.filter(goal_type=enums.GoalType.SPENDING)
        

    
        
        
