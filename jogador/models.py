from django.db import models

class Clube(models.Model):
	nome = models.CharField(max_length=200)	

class Jogador(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    altura = models.DecimalField(max_digits=3, decimal_places=2)

    POSICOES = (
    	('ATA', 'Atacante'),
    	('MEI', 'Meio-Campo'),
    	('ZAG', 'Zagueiro'),
    	('LAT', 'Lateral'),
    )

    posicao = models.CharField(choices=POSICOES, max_length=3)
    clube = models.ForeignKey(Clube)
    ritmo = models.IntegerField() 
    chute = models.IntegerField()
    passe = models.IntegerField()
    drible = models.IntegerField()
    defesa = models.IntegerField() 
    fisico = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)

	