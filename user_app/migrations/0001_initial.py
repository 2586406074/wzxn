# Generated by Django 4.0.1 on 2022-05-07 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_pwd', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=30)),
                ('ident', models.IntegerField(choices=[(1, '已激活'), (2, '未激活')], default=1)),
                ('power', models.IntegerField(choices=[(1, '普通用户'), (2, '会员'), (3, '超级会员')], default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_name', models.CharField(max_length=36)),
                ('shopping_img', models.ImageField(upload_to='')),
                ('shopping_price', models.CharField(max_length=32)),
                ('shopping_des', models.CharField(max_length=64)),
                ('shopping_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.userlogin')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('code', models.IntegerField()),
                ('iphone', models.CharField(max_length=11)),
                ('is_default', models.IntegerField(default=1)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.userlogin')),
            ],
        ),
    ]
