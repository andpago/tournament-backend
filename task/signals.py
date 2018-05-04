from django.db.models.signals import pre_save
from django.dispatch import receiver

from task.models import Solution


@receiver(pre_save, sender=Solution)
def on_save(instance: Solution, **kwargs):
    print("SIGNAL SAVE")
    instance.correct = instance.check_solution()
