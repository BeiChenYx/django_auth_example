from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    """
    UserCreationForm这个表单关联到了Django内置
    User模型, 因为内部类Meta的model属性, 它的
    值对应的是auth.User, 因此无法直接用于我们
    自定义的User模型, 可以通过继承的方式来修改.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        # 用来指定表单的字段
        # 密码和确认密码在UserCreationForm的属性中
        # 已经指定了, 希望在注册时提供邮箱
        # 所以在fields中增加email字段
        # 虽然model属性的值被指定为User,但一个是auth.User,
        # 一个是users.User
        fields = ('username', 'email')
