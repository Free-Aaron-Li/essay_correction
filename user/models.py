from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # 自增主键
    username = models.CharField(max_length=50, unique=True, null=False)  # 唯一用户名
    password = models.CharField(max_length=255, null=False)  # 密码（建议加密存储）
    avatar = models.CharField(max_length=255, null=True, blank=True)  # 头像路径
    email = models.EmailField(max_length=50, unique=True, null=False)  # 唯一邮箱
    phone = models.CharField(max_length=20, null=True, blank=True)  # 电话
    last_login_time = models.DateTimeField(null=True, blank=True)  # 最后登录时间
    status = models.SmallIntegerField(default=1)  # 状态（默认启用，0：禁用，1：启用）
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间，默认当前时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间，自动更新
    remark = models.CharField(max_length=255, null=True, blank=True)  # 备注
    user_type = models.SmallIntegerField(null=False)  # 用户类型（0：管理员，1: 学生，2: 教师）

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"  # 表名称对应数据库中的 users
        verbose_name = "用户"
        verbose_name_plural = "用户"
