class Article(models.Model):
  titre=models.CharField(max_length=100)
  auteur=models.CharField(max_length=42)
  contenu=models.TextField(null=True)
  categorie=models.ForeignKey('Categorie', on_delete=models.CASCADE)

  def __str__(self):
    return self.titre
 
class Categorie (models.Model):
  nom=models.CharField(max_length=30)
  def __str__(self):
    return self.nom
