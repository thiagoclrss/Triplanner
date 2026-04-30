# Register your models here.
from django.db import models


class City(models.Model):
    slug = models.SlugField(
        primary_key=True, max_length=255, null=False, blank=False,
        help_text='Nome limpo para urls e paths',
    )
    name = models.CharField(
        max_length=255, null=False, blank=False, db_index=True,
        help_text='Nome da cidade',
    )

    IMPORTANCE_CHOICES = [(i, str(i)) for i in range(1, 11)]
    importance = models.SmallIntegerField(
        verbose_name='Importancia padrão', choices=IMPORTANCE_CHOICES,
        default=5, db_default=5, null=False,
    )
    routes = models.ManyToManyField(
        'self', through='nucleo.Route', through_fields=('src', 'dest'),
        related_name='+', symmetrical=False,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'


class Route(models.Model):
    src = models.ForeignKey(
        City, verbose_name='origem', on_delete=models.CASCADE,
        related_name='+',
    )
    dest = models.ForeignKey(
        City, verbose_name='destino', on_delete=models.CASCADE,
        related_name='rotas',
    )
    _NUMERO_DIGITOS_BILHAO = 12
    cost = models.DecimalField(
        verbose_name='custo', max_digits=_NUMERO_DIGITOS_BILHAO, decimal_places=2, null=False, blank=False,
        help_text='custo (em R$) para ir de origem a destino',
    )
    time = models.DurationField(
        verbose_name='tempo', null=False, blank=False,
        help_text='Tempo (em Horas) de viagem de origem a destino',
    )

    def __str__(self) -> str:
        return f'Rota de {self.src} para {self.dest}'

    class Meta:
        verbose_name = 'Rota'
        verbose_name_plural = 'Rotas'
        constraints = [
            models.UniqueConstraint(name='unique_route', fields=['src', 'dest'],),
            models.CheckConstraint(
                name='src_not_equal_dest',
                condition=~models.Q(src=models.F('dest')),
                violation_error_message='Origem não pode ser igual a destino',
            ),
        ]
