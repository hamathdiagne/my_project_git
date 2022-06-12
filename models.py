class Article(modèles.Model):
  titre=models.CharField(max_length=100)
  auteur=models.CharField(max_length=42)
  contenu=models.TextField(null=True)
