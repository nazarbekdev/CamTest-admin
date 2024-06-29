import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_code', models.IntegerField()),
                ('answers', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CallNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CTUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('limit', models.IntegerField(default=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenerateTestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.CharField(max_length=50)),
                ('subject2', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('number_books', models.IntegerField()),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.IntegerField()),
                ('language_id', models.IntegerField()),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ctuser')),
            ],
        ),
        migrations.CreateModel(
            name='GenerateTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_books', models.IntegerField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language', to='api.language')),
                ('subject1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_1', to='api.subject')),
                ('subject2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_2', to='api.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='document/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.language')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject')),
            ],
        ),
        migrations.CreateModel(
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ctuser')),
            ],
        ),
    ]
