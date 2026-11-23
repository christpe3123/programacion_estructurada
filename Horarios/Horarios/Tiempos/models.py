from django.conf import settings
from django.db import models


class Docente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    codigo_docente = models.CharField(max_length=15, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"


class Curso(models.Model):
    codigo = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=150)
    creditos = models.PositiveSmallIntegerField(default=3)
    docentes_habilitados = models.ManyToManyField(Docente, related_name="cursos")

    def __str__(self):
        return f"[{self.codigo}] {self.nombre}"


class Aula(models.Model):
    codigo_aula = models.CharField(max_length=20, unique=True)
    pabellon = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return f"Aula {self.codigo_aula} ({self.pabellon})"


class BloqueHorario(models.Model):
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
    ]
    dia_semana = models.CharField(max_length=3, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        ordering = ['dia_semana', 'hora_inicio']
        constraints = [
            models.UniqueConstraint(
                fields=['dia_semana', 'hora_inicio', 'hora_fin'],
                name='bloque_horario_unico',
            )
        ]

    def __str__(self):
        return (
            f"{self.get_dia_semana_display()} "
            f"{self.hora_inicio:%H:%M}-{self.hora_fin:%H:%M}"
        )


class Horario(models.Model):
    curso = models.ForeignKey(
        Curso,
        on_delete=models.PROTECT,
        related_name="horarios",
    )
    docente = models.ForeignKey(
        Docente,
        on_delete=models.PROTECT,
        related_name="horarios",
    )
    aula = models.ForeignKey(
        Aula,
        on_delete=models.PROTECT,
        related_name="horarios",
    )
    bloque = models.ForeignKey(
        BloqueHorario,
        on_delete=models.PROTECT,
        related_name="horarios",
    )

    class Meta:
        ordering = ["bloque__dia_semana", "bloque__hora_inicio"]
        constraints = [
            models.UniqueConstraint(
                fields=["docente", "bloque"],
                name="horario_docente_bloque_unico",
            ),
            models.UniqueConstraint(
                fields=["aula", "bloque"],
                name="horario_aula_bloque_unico",
            ),
        ]

    def __str__(self):
        return f"{self.curso} - {self.docente} - {self.bloque}"