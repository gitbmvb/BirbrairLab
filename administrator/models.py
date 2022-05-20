from django.db import models


class User(models.Model):
    pass


class Directions(models.Model):
    text = models.TextField(blank=False, max_length=500)
    map = models.CharField(blank=True, max_length=1000)
    last_edit = models.ForeignKey(User, on_delete=models.CASCADE)
#    socialNetwork


# class Donate(models.Model):
#    text = models.TextField(blank=False, max_length=500)
#    donators = models.ForeignKey()


class Meet(models.Model):
    about = models.TextField(blank=False, max_length=500)
    biography = models.TextField(blank=False, max_length=1200)
    curriculum = models.FileField(blank=True, upload_to="")
    profilePicture = models.ImageField(blank=False, upload_to="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class News(models.Model):
    date = models.DateField(blank=False)
    title = models.CharField(blank=False, max_length=100)
    url = models.URLField(blank=False, max_length=100)


class Opportunities(models.Model):
    image = models.ImageField(blank=False, upload_to="")
    text = models.TextField(blank=False, max_length=500)


class Publications(models.Model):
    authors = models.CharField(blank=False, max_length=100)
    title = models.CharField(blank=False, max_length=100)
    date = models.DateField(blank=False, )
    journal = models.CharField(blank=False, max_length=100)
    doi = models.URLField(blank=False, max_length=1000)
    pmid = models.IntegerField(blank=False, max_length=10)


class Research(models.Model):
    visibilityChoices = (
        ("v", "Visible"),
        ("i", "Invisible"),
    )

    description = models.TextField(blank=False, max_length=1200)
    image = models.ImageField(blank=False, upload_to="")
    image_subtitle = models.CharField(blank=False, max_length=200)
    title = models.CharField(blank=False, max_length=200)
    visibility = models.CharField(blank=False, choices=visibilityChoices, max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Team(models.Model):
    memberChoices = (
        ("Mas", "Master Student"),
        ("PhD", "PhD Student"),
        ("Pos", "Post-doctoral fellow"),
        ("PrI", "Principal Investigator"),
        ("Und", "Undergraduate Student"),
        ("Spe", "Specialist"),
        ("Tec", "Technician"),
    )
    statusChoices = (
        ("ac", "Active Member"),
        ("al", "Alumni"),
    )
    email = models.EmailField(blank=False, max_length=100)
    fullName = models.CharField(blank=False, max_length=100)
    lattes = models.CharField(blank=False, max_length=100)
    memberType = models.CharField(blank=False, choices=memberChoices, max_length=3)
    profilePicture = models.ImageField(blank=False, upload_to="")
    status = models.CharField(blank=False, choices=statusChoices, max_length=2)


