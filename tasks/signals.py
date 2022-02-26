from django.db.models.signals import pre_save
from django.dispatch import receiver
from tasks.models import Task, TaskHistory


@receiver(pre_save, sender=Task)
def update_task_history(sender, instance, **kwargs):
    if instance.id:
        old_task = Task.objects.get(id=instance.id)
        new_task = instance

        if old_task.status != new_task.status:
            TaskHistory.objects.create(
                task=instance,
                previous_status=old_task.status,
                current_status=new_task.status,
            )
