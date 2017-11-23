from django.contrib.auth.forms import UserCreationForm

from .models import User

# 表单


class RegisterForm(UserCreationForm):
    """用户注册表单"""

    class Meta(UserCreationForm.Meta):
        """覆写Meta类使该表单关联自定义的 User 模型"""
        model = User
        fields = ('username', 'email')
