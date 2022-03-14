# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Group
# from .models import Doctor

# # def doctor_profile(sender,instance,created, **kwargs):
# #     print("sender:",sender,"ins:",instance,"creat",created,"kwrgs:",kwargs)
# #     if created:
# #         group,created = Group.objects.get_or_create(name='doctor')
# #         instance.groups.add(group)

# #         Doctor.objects.create(
# #             user=instance,
# #             name = instance.username
# #         )
# #         print('Doctor profile Created !!!')

# # post_save.connect(doctor_profile,sender = User)
