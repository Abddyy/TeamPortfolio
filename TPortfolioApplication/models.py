from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    url = models.URLField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    # photo =
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.job_title}'
